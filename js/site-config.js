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

    /* ---- Express Program figures — ALL VERIFY with express@commcorp.org ---- */
    EXPRESS_MAX_PER_PERSON_PER_COURSE: 3000,  // VERIFY
    EXPRESS_MAX_PER_INSTRUCTIONAL_HOUR: 300,  // VERIFY
    EXPRESS_ANNUAL_CAP_PER_COMPANY: 15000,    // VERIFY (some sources say $30k)
    EXPRESS_SMALL_EMPLOYER_MAX: 100,          // VERIFY
    EXPRESS_RATE_SMALL: 1.00,                 // VERIFY — up to 100% for small employers
    EXPRESS_RATE_LARGE: 0.50,                 // VERIFY — DCS Info 26-102 opened Express to any size at 50%
    EXPRESS_AGREEMENT_AUTOSTART_DAYS: 21,     // VERIFY
    ESOL_PAID_TIME_MIN_SHARE: 0.50,           // VERIFY

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
