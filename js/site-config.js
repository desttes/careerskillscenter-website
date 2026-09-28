/* ==========================================================================
   Career Skills Center — site configuration & feature flags
   --------------------------------------------------------------------------
   Single source of truth for copy-sensitive switches and numbers. Loaded on
   every page BEFORE js/main.js. Plain global object (the static host does not
   use ES modules); read it as window.SITE_CONFIG or the alias CSC.

   Flip these flags and the copy that reads them changes automatically. Course-
   mode copy may be pre-written behind SITE_MODE / COURSES_LIVE, but must never
   render while they are off. See docs/GUIDE_MODE_SPEC.md and
   docs/COURSE_CONTENT_REGISTER.md.
   ========================================================================== */
(function (root) {
  'use strict';

  var CONFIG = {
    /* ---- Guide mode / course mode switches (GUIDE_MODE_SPEC §5) ---- */
    SITE_MODE: "guide",                 // "guide" now; "courses" once any course is live
    COURSES_LIVE: { healthcare: false, it: false, trades: false },

    /* ---- Funding / provider compliance flags (BUILD_BRIEF §6) ---- */
    FUNDING_ETPL_APPROVED: false,       // true only after the ETPL listing is live
    EXPRESS_PROVIDER_LISTED: false,     // true only after CommCorp approves the provider + courses

    /* ---- Express Program figures — CommCorp Express Program Guidelines ---- */
    EXPRESS_MAX_PER_PERSON_PER_COURSE: 3000,  // confirmed 2026-09-28 (CommCorp Express Guidelines: $3,000/employee/course)
    EXPRESS_MAX_PER_INSTRUCTIONAL_HOUR: 300,  // confirmed 2026-09-28 (CommCorp Express Guidelines: $300/instructional hour)
    EXPRESS_ANNUAL_CAP_PER_COMPANY: 15000,    // confirmed by Emilio 2026-09-28 (up to $15k/yr, reusable across trainings)
    EXPRESS_SMALL_EMPLOYER_MAX: 100,          // confirmed by Emilio 2026-09-28 (100 or fewer W-2 employees)
    EXPRESS_RATE_SMALL: 1.00,                 // confirmed 2026-09-28 (up to 100% for eligible employers with <=100 MA W-2 employees)
    EXPRESS_APPLICATION_WEEKS: 3,             // confirmed by Emilio 2026-09-28 (application -> acceptance ~3 weeks)
    ESOL_PAID_TIME_MIN_SHARE: 0.50,           // VERIFY

    /* ---- Massachusetts Registered Apprentice Tax Credit ----
       Source: mass.gov Division of Apprentice Standards (Apply for a Registered
       Apprentice Tax Credit; DAS Issuance TY2026 32-07012026). Checked 2026-09-28. */
    APPRENTICE_TAX_CREDIT_WAGE_SHARE: 0.50,          // 50% of the apprentice's wages
    APPRENTICE_TAX_CREDIT_MAX_PER_APPRENTICE: 4800,  // per apprentice, per year
    APPRENTICE_TAX_CREDIT_MAX_PER_EMPLOYER: 100000,  // per employer (sponsor), per year
    APPRENTICE_TAX_CREDIT_YEARS: 2,                  // up to 2 consecutive tax years per apprentice
    APPRENTICE_MIN_DAYS: 180,                        // apprentice must work >= 180 days in the tax year

    /* ---- Official outward destinations (GUIDE_MODE_SPEC; verified) ---- */
    MASSHIRE_LOCATOR: "https://www.mass.gov/info-details/masshire-career-center-locations",
    JOBQUEST: "https://jobquest.mass.gov",

    /* ---- Contact ---- */
    PHONE: "(617) 544-7155",
    EMAIL: "info@careerskillscenter.com"
  };

  root.SITE_CONFIG = CONFIG;
  root.CSC = CONFIG; // short alias
})(typeof window !== "undefined" ? window : this);
