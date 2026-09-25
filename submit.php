<?php
/**
 * Career Skills Center — form mailer
 * -----------------------------------
 * Receives a POST from any form on the site and emails it to the school.
 * No database, no dependencies — plain PHP mail() on the cPanel host.
 *
 * Every form must post a hidden `source` field (see docs/BUILD_BRIEF.md rule 2b)
 * and, via JavaScript, a `page` field. A hidden honeypot field named
 * `company_website` catches bots: if it is filled, we silently accept and drop.
 *
 * Deploy: upload to the docroot (~/careerskillscenter.com/submit.php), chmod 644.
 * Forms post to "submit.php" (relative), which resolves to the site root.
 *
 * Deliverability note: FROM is an address ON this domain so SPF/DKIM pass.
 * `info@careerskillscenter.com` already exists, so it is the safe default.
 * You may create a dedicated `no-reply@careerskillscenter.com` mailbox/alias
 * and change FROM to it; the visitor's address is always set as Reply-To.
 */
declare(strict_types=1);

const CSC_RECIPIENT    = 'vcanal@careerskillscenter.com'; // where lead notifications are delivered
const CSC_FROM         = 'info@careerskillscenter.com';  // on-domain sender so SPF/DKIM pass (keep as an address on this domain)
const CSC_PUBLIC_EMAIL = 'info@careerskillscenter.com';  // address shown to visitors (never expose the internal recipient)
const CSC_SITE      = 'Career Skills Center';
const CSC_MAX_LEN   = 5000; // per-field cap, to blunt abuse

/** Strip CR/LF (and encoded variants) so user input can't inject mail headers. */
function csc_clean_header(string $s): string
{
    return trim(str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D"], ' ', $s));
}

/** Human labels for known fields; anything else is title-cased from its name. */
function csc_label(string $key): string
{
    static $labels = [
        'name'       => 'Name',
        'email'      => 'Email',
        'phone'      => 'Phone',
        'program'    => 'Program of interest',
        'language'   => 'Preferred language',
        'pay_method' => 'How would you likely pay',
        'company'    => 'Company',
        'city'       => 'City',
        'employees'  => '# of MA employees',
        'message'    => 'Message',
        'consent'    => 'SMS consent',
        'source'     => 'Source',
        'page'       => 'Page',
    ];
    return $labels[$key] ?? ucfirst(str_replace('_', ' ', $key));
}

/**
 * Decide what to do with a submission. Pure function (no mail(), no output),
 * so it can be unit-tested. Returns one of:
 *   ['action' => 'drop',  'status' => 200, 'json' => [...]]
 *   ['action' => 'error', 'status' => 4xx, 'json' => [...]]
 *   ['action' => 'send',  'status' => 200, 'mail' => ['to','subject','body','headers'],
 *                         'redirect' => string|null]
 */
function csc_process(array $post, array $server): array
{
    if (($server['REQUEST_METHOD'] ?? '') !== 'POST') {
        return ['action' => 'error', 'status' => 405,
                'json' => ['ok' => false, 'error' => 'Method not allowed']];
    }

    // Honeypot: real people never see or fill this. Pretend success.
    if (trim((string)($post['company_website'] ?? '')) !== '') {
        return ['action' => 'drop', 'status' => 200, 'json' => ['ok' => true]];
    }

    // Collect string fields, trimmed and length-capped.
    $data = [];
    foreach ($post as $key => $val) {
        if (!is_string($val) || $key === 'company_website') {
            continue;
        }
        $data[$key] = mb_substr(trim($val), 0, CSC_MAX_LEN);
    }

    // Required + validation.
    $name  = $data['name'] ?? '';
    $email = $data['email'] ?? '';
    $bad   = [];
    if ($name === '') {
        $bad[] = 'name';
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $bad[] = 'email';
    }
    if ($bad) {
        return ['action' => 'error', 'status' => 422,
                'json' => ['ok' => false, 'error' => 'Please provide your name and a valid email.',
                           'fields' => $bad]];
    }

    $name   = csc_clean_header($name);
    $email  = csc_clean_header($email);
    $source = csc_clean_header($data['source'] ?? 'unknown');
    $page   = csc_clean_header($data['page'] ?? '');

    // Body: every non-empty field, known ones first in a friendly order.
    $order = ['name', 'email', 'phone', 'program', 'company', 'city', 'employees',
              'language', 'pay_method', 'consent', 'message'];
    $seen  = [];
    $lines = [];
    foreach ($order as $k) {
        if (isset($data[$k]) && $data[$k] !== '') {
            $lines[] = csc_label($k) . ': ' . $data[$k];
            $seen[$k] = true;
        }
    }
    foreach ($data as $k => $v) {
        if ($v === '' || isset($seen[$k]) || in_array($k, ['source', 'page', '_redirect'], true)) {
            continue;
        }
        $lines[] = csc_label($k) . ': ' . $v;
    }

    $body  = "New submission from the \"{$source}\" form on " . CSC_SITE . ".\n\n";
    $body .= implode("\n", $lines) . "\n\n";
    $body .= "----\n";
    $body .= "Source: {$source}\n";
    if ($page !== '') {
        $body .= "Page: {$page}\n";
    }
    $body .= 'Submitted: ' . date('Y-m-d H:i:s T') . "\n";
    $body .= 'IP: ' . ($server['REMOTE_ADDR'] ?? 'unknown') . "\n";

    $subject = '[' . $source . '] Website inquiry from ' . $name;

    $headers = implode("\r\n", [
        'From: ' . CSC_SITE . ' <' . CSC_FROM . '>',
        'Reply-To: ' . $name . ' <' . $email . '>',
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=utf-8',
        'X-Mailer: CSC-form',
    ]);

    $redirect = isset($data['_redirect']) && $data['_redirect'] !== ''
        ? csc_clean_header($data['_redirect'])
        : null;

    return ['action' => 'send', 'status' => 200, 'redirect' => $redirect,
            'mail' => ['to' => CSC_RECIPIENT, 'subject' => $subject,
                       'body' => $body, 'headers' => $headers]];
}

/** Web entry point: run the plan, send the mail, respond. */
function csc_main(): void
{
    $result = csc_process($_POST, $_SERVER);
    http_response_code($result['status']);

    if ($result['action'] === 'send') {
        $m  = $result['mail'];
        $ok = @mail($m['to'], $m['subject'], $m['body'], $m['headers']);

        if (!empty($result['redirect'])) {
            $sep = str_contains($result['redirect'], '?') ? '&' : '?';
            header('Location: ' . $result['redirect'] . $sep . 'sent=' . ($ok ? '1' : '0'));
            return;
        }

        header('Content-Type: application/json; charset=utf-8');
        if ($ok) {
            echo json_encode(['ok' => true]);
        } else {
            http_response_code(500);
            echo json_encode(['ok' => false,
                'error' => 'Sorry, we could not send that just now. Please email ' . CSC_PUBLIC_EMAIL . '.']);
        }
        return;
    }

    // drop or error
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($result['json']);
}

// Only run for real web requests; under the CLI SAPI the file just defines
// functions so tests can include it and call csc_process() directly.
if (PHP_SAPI !== 'cli') {
    csc_main();
}
