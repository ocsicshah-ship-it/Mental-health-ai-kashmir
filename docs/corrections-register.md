# Corrections Register — must never regress

These eight corrections override earlier blueprint assumptions. Each has been encoded
into the relevant artifact; a regression here is a **safety or compliance defect**, not
a cosmetic one. Re-verify before any release.

---

| # | Correction | Why it matters | Encoded in |
|---|---|---|---|
| 1 | **Kashmir Lifeline is run by the Healing Minds Foundation, NOT Médecins Sans Frontières.** (MSF's role was the 2015 survey.) | Mis-attribution undermines trust and is factually wrong. | `config/crisis-resources.json` |
| 2 | **Kashmir Lifeline = 1800-180-7020, Sun–Thu 10am–5pm only — NOT 24/7.** | **Direct safety impact:** presenting it as after-hours crisis support sends a person in crisis to a closed line. Time-gated in config + prompt. | `config/crisis-resources.json`, `prompts/system-prompt.md` |
| 3 | **KIRAN (1800-599-0019) is merged into Tele-MANAS — do NOT present as a standalone active line.** Route to **14416**. | Citing a possibly-unanswered line risks a dropped crisis contact. Listed under `_meta.do_not_cite`. | `config/crisis-resources.json` |
| 4 | **Tele-MANAS J&K** is run by **IMHANS-K at GMC Srinagar** (nodal Dr Arshid Hussain); chatbot **9797600601**; numbers **14416 / 1-800-891-4416** verified. | The authoritative primary line — must be exactly right. | `config/crisis-resources.json`, `prompts/system-prompt.md` |
| 5 | **DPDP Rules 2025 are NOTIFIED (13 Nov 2025)** — compliance is a live obligation, not a future "pending rules" item. | Verifiable parental consent, no profiling of minors, 72-hour breach notice, erasure schedules are required *now*. | `consent/dpdp-consent-notice.md`, `docs/compliance-checklist.md` |
| 6 | **Suicide decriminalization is reinforced by BNS 2023** (no IPC 309 successor) in addition to MHCA §115. | Lets the bot honestly reassure users they won't be punished for disclosing. | `prompts/system-prompt.md`, `docs/compliance-checklist.md` |
| 7 | **Dataset licenses:** ESConv, MentalManip = CC-BY-NC; **KokoroChat = CC-BY-NC-ND (no derivatives).** Treat as research-only; source separate data for commercial/derivative use. | Using these to fine-tune a product is a license violation. | `docs/datasets-register.md` |
| 8 | **Regulatory posture:** position as non-clinical wellness/psychoeducation (no diagnosis/treatment claims) to stay in the CDSCO wellness carve-out and outside the Telemedicine RMP/AI-prescribing prohibition. | Wrong positioning pulls the product into SaMD/RMP regimes. | `docs/compliance-checklist.md`, `prompts/system-prompt.md` |

## Open items to verify before hard-coding (caveats)

- J&K Police women's-helpline number, a dedicated J&K ANTF helpline, and **current OSC
  count** (the 19-OSC figure is April 2022) — verify against jkpolice.gov.in and the
  live Mission Shakti dashboard.
- **Urdu coverage** is confirmed for Tele-MANAS and Vandrevala; **not** confirmed for
  Childline 1098, iCall, or AASRA — do not promise Urdu for those.
- CDSCO wellness carve-out rests on **draft** guidance (21 Oct 2025) — monitor for final
  notification.
- Tele-MANAS J&K call-volume figures are **point-in-time** news reporting of NHM data —
  cite as such, never as current totals.
- KIRAN→Tele-MANAS merger **date** is uncertain (likely late-2023/early-2024); the
  operational conclusion (route to Tele-MANAS) is unaffected.
