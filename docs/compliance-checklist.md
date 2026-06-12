# Compliance & Regulatory Checklist

> **Not legal advice.** Obtain a written legal opinion on SaMD status and DPDP posture
> before launch. This consolidates the regulatory landscape into actionable gates.

The core strategy: position the product as a **non-clinical wellness / psychoeducation
companion** (no diagnosis, treatment, or prescribing claims) to stay inside the CDSCO
wellness carve-out and outside the Telemedicine Guidelines' RMP/AI-prescribing
prohibition — while fully complying with DPDP 2025 and ICMR AI ethics.

---

## 1. Positioning (the cleanest compliance path)

- [ ] Explicit, prominent disclaimers: **"wellness/psychoeducation, not a medical
      device, not therapy or diagnosis."**
- [ ] No therapeutic/diagnostic/predictive claims anywhere in product or marketing.
- [ ] No diagnosis, no prescribing, no treatment recommendations in-product (enforced
      by the system prompt + output guardrail).

## 2. CDSCO / Software as a Medical Device (MDR 2017)

- Software with a medical purpose can be regulated as SaMD (Class A–D).
- **CDSCO Draft Guidance on Medical Device Software (21 Oct 2025)** keeps **"lifestyle,
  wellness and fitness applications" outside** the MDR regime — *provided no
  therapeutic/diagnostic claims are made.*
- [ ] Written legal opinion confirming the product does **not** trigger SaMD.
- [ ] ⚠️ **Caveat:** this is **draft** guidance — monitor for final notification; if the
      wellness carve-out narrows, re-run this review (see trigger below).

## 3. Telemedicine Practice Guidelines 2020

- Apply only to Registered Medical Practitioners; state that AI/ML **must not** counsel
  or prescribe — AI may only *assist* an RMP.
- [ ] Product never counsels/prescribes in a way reserved to RMPs; it supports and
      refers only.

## 4. DPDP Act 2023 + **Rules 2025 (notified 13 Nov 2025)**

Full obligations and user-facing copy in `consent/dpdp-consent-notice.md`. Gate items:

- [ ] Granular, itemized, plain-language consent + easy withdrawal.
- [ ] Anonymous-use option; data minimization; "prefer not to say" everywhere.
- [ ] Retention & erasure schedule; honor erasure requests.
- [ ] Under-18: **verifiable parental consent** (Rule 10); **no profiling/behavioural
      tracking/targeted ads** for children.
- [ ] Security: encryption, masking/tokenization, access controls, logs ≥1 year (Rule 6).
- [ ] **72-hour** breach notification to Data Principals + immediate Board notice (Rule 7).
- [ ] Grievance/complaint mechanism + contact.
- [ ] If a **Significant Data Fiduciary**: DPIA/audits, algorithmic due diligence,
      India-based DPO, notified localization handling.
- Penalty exposure: up to **₹250 crore** for failure to maintain reasonable safeguards.

## 5. Mental Healthcare Act 2017

- §115: a person attempting suicide is presumed under severe stress; **not to be tried
  or punished** under IPC 309; government owes care/treatment/rehabilitation.
- Reinforced by **Bharatiya Nyaya Sanhita 2023** — no successor to IPC 309 (abetment of
  suicide remains an offence).
- Applies to the J&K UT post the J&K Reorganisation Act 2019.
- [ ] Crisis copy reassures users they will not be punished for disclosing suicidality.

## 6. ICMR Ethical Guidelines for AI in Biomedical Research & Healthcare (2023)

Ethical (de facto national standard), explicitly covers behavioural/mental healthcare.
Ten principles to evidence:

- [ ] **Autonomy** — human oversight; user can reject AI / reach a human.
- [ ] **Safety & risk minimization** — crisis layer, red-team gate.
- [ ] **Trustworthiness / data security** — see DPDP items.
- [ ] **Accountability & liability** — clear ownership; audit logs.
- [ ] **Data privacy** — anonymous-use, minimization.
- [ ] **Validity** — evaluated performance, including by language.
- [ ] **Non-discrimination & fairness** — no language/demographic lags materially.
- [ ] **Accessibility & equity** — 2G/offline, multilingual (see `language-access.md`).

## 7. Liability patchwork

No single statute for wellness apps: MDR (if SaMD triggered) + Telemedicine Guidelines
+ ICMR ethics + DPDP 2023 + **Consumer Protection Act 2019** (deficiency of service /
misleading claims). Mitigation: avoid clinical claims, comply with DPDP, robust
crisis-escalation/referral, accuracy of all stated claims (esp. helpline details).

## Re-review triggers

- CDSCO **finalizes** Medical Device Software guidance and **narrows** the wellness
  carve-out → re-run SaMD analysis before continuing.
- DPDP **Significant Data Fiduciary localization categories** are notified → assess
  localization, DPIA, DPO obligations.
- Any change introducing diagnostic/therapeutic features → full regulatory re-review.
