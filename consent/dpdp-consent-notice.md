# Consent & Privacy Notice (DPDP Rules 2025-aligned) — DRAFT COPY

> Draft user-facing copy and the obligations behind it. **Not legal advice** — obtain a
> written legal opinion before launch (see `docs/compliance-checklist.md`). The DPDP
> **Rules 2025 were notified on 13 Nov 2025** with a phased ~18-month runway, so these
> are live obligations, not future ones.

This app is a **Data Fiduciary** under the Digital Personal Data Protection Act 2023.
Conversation content in a mental-health context is highly sensitive personal data and
must be treated as such.

---

## Design principles (mirror Tele-MANAS)

- **Anonymous by default.** No name or identifying detail required to get help.
- **Data minimization.** Collect only what is necessary; "prefer not to say" always
  available for any demographic field.
- **Honesty over reassurance.** Never claim "fully confidential" if logs are retained.
  State plainly what is stored, why, for how long, and how to withdraw.

## Itemized notice — what a standalone consent screen must list

Consent must be **free, specific, informed, unconditional, and given by clear
affirmative action**, with an equally easy way to withdraw.

1. **What we collect** — message content; coarse technical metadata needed to operate
   (e.g. language preference); *no* requirement to provide name/phone for support.
2. **Why** — to provide emotional support and psychoeducation, to route you to verified
   human help, and to keep the service safe (crisis detection/audit). Purpose-limited.
3. **What we do NOT do** — we do **not** sell your data, and for **users under 18** we
   do **not** profile, behaviorally monitor, or target advertising (DPDP Rule 10 +
   children's-data prohibitions).
4. **Retention & erasure** — stored only as long as needed for the stated purposes,
   then deleted on a published schedule; you can request erasure at any time.
5. **Your rights** — access, correction, erasure, grievance redressal, and consent
   withdrawal, via a clearly linked mechanism.
6. **Security** — encryption, masking/tokenization, access controls, and security logs
   retained ≥1 year (DPDP Rule 6).
7. **Breach** — if your data is involved in a breach, we notify you within **72 hours**
   and notify the Data Protection Board immediately (DPDP Rule 7).
8. **Contact** — grievance/complaint link and the data-protection contact.

## Minors

- **Verifiable parental consent** required for under-18s (DPDP Rule 10), via an
  approved verification method (e.g. DigiLocker).
- **No tracking, behavioural monitoring, profiling, or targeted advertising** directed
  at children. This is a hard product constraint for a youth-facing Kashmir tool, not a
  toggle.

## Operational obligations checklist (for the build)

- [ ] Standalone, itemized, plain-language consent screen (Koshur/Urdu/English).
- [ ] Easy, always-available consent **withdrawal** link.
- [ ] Anonymous-use path that does not degrade safety/crisis features.
- [ ] Published **retention & erasure** schedule; automated deletion.
- [ ] Under-18 verifiable parental consent + profiling/tracking disabled.
- [ ] Encryption at rest/in transit; tokenization of any identifiers; access controls.
- [ ] Security logs retained ≥1 year.
- [ ] **72-hour** Data-Principal breach-notification workflow + immediate Board
      notification; runbook tested.
- [ ] Grievance/complaint mechanism with named contact.
- [ ] If classified a **Significant Data Fiduciary**: annual DPIA/audit, algorithmic
      due diligence, India-based DPO, and any notified localization handling.

## Draft microcopy (to localize)

> **Before we begin.** I'm an AI support companion — not a doctor or therapist, and not
> a medical device. You can talk to me **without giving your name**. I keep what you
> share private and use it only to support you and to connect you with help; I don't
> sell it. I store messages only as long as needed, and you can ask me to delete them
> anytime. If you're ever in danger, I'll always share free, confidential human
> helplines like **Tele-MANAS 14416**. Is it okay to continue?  **[Yes, continue]
> [Tell me more] [No]**
