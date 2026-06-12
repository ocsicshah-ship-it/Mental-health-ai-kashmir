# Mental Health AI — Kashmir

A culturally-grounded, conflict-aware, faith-respecting **non-clinical wellness &
psychoeducation** companion for the Kashmir Valley. Urdu / Koshur / English,
low-bandwidth (2G-tolerant) by design, with **hard-coded, offline-cacheable crisis
resources** and a **non-bypassable crisis-escalation path** to professional help.

> **This is not a medical device, not therapy, and not a diagnostic or prescribing
> tool.** It provides emotional support, psychoeducation, and verified referral to
> human services. It never diagnoses, never prescribes, and always routes
> risk-of-harm situations to professionals.

---

## Why this exists

The Kashmir Valley carries an exceptional mental-health burden against a thin
clinical workforce:

- **~45% adult prevalence of mental distress** (peer-reviewed Kashmir Mental Health
  Survey 2015 — 5,428 households, all 10 districts): ~41% probable depression, ~26%
  anxiety, ~19% PTSD.
- **~70,000 youth substance users (~50,000 on heroin)** per the J&K government's
  2022 survey (reported to the Assembly, Feb 2026).
- The **world's longest democratic internet shutdown** (552 days of disruption
  around 2019–21; high-speed 4G restored 5 Feb 2021) — the single strongest reason
  to design **offline-capable, 2G-tolerant, text-first**.
- Deep **stigma / izzat** dynamics, joint-family power structures, and faith-healing
  as a common first point of contact.

See `docs/conflict-context.md` and `docs/cultural-safety.md` for the full grounding.

---

## Status

**Specification + working prototype.** This repository contains the safety-critical
foundation and project specification (`config/`, `prompts/`, `safety/`, `consent/`,
`docs/`), plus a runnable FastAPI + Claude API prototype ("Sukoon", under `app/` and
`static/`). The prototype is a development sandbox — it does **not** yet implement
the Stage-0 non-negotiables below and must not be exposed to real users.

---

## Repository layout

```
README.md                          You are here
config/
  crisis-resources.json            ⭐ VERIFIED crisis/support contacts (offline-cacheable, hard-coded)
  crisis-resources.schema.json     JSON Schema for the above
prompts/
  system-prompt.md                 ⭐ Safety-critical production system prompt
safety/
  crisis-classifier-spec.md        Non-bypassable crisis detection + mandatory-referral spec + red-team plan
consent/
  dpdp-consent-notice.md           DPDP Rules 2025-aligned consent / privacy notice copy
docs/
  language-access.md               Koshur/Urdu/English + 2G/offline access engineering
  datasets-register.md             Training datasets + LICENSE register (commercial-use caveats)
  compliance-checklist.md          DPDP 2025 / MHCA 2017 / CDSCO / ICMR / Telemedicine
  corrections-register.md          The 8 blueprint corrections that must not regress
  cultural-safety.md               Family systems, izzat/stigma, faith integration, coercive control
  conflict-context.md              Trauma prevalence, post-2019, addiction crisis, workforce
app/                               Prototype: FastAPI backend calling the Claude API
static/index.html                  Prototype: zero-build chat UI
tests/                             Prototype: pytest suite (runs without an API key)
CLAUDE.md                          Instructions for Claude Code
```

## The non-negotiables (Stage 0 — blocking)

These ship **before any user touches the system**. See `safety/crisis-classifier-spec.md`.

1. **Verified crisis block, offline-cached** — Tele-MANAS **14416 / 1-800-891-4416**
   (24/7), ERSS **112**, Childline **1098** (minors), Women Helpline **181** / Sakhi
   OSC, Kashmir Lifeline **1800-180-7020** (Sun–Thu 10am–5pm **only — time-gated**).
2. **Non-bypassable suicide/self-harm/abuse classifier** with **mandatory referral**.
   The anti-pattern to avoid: a 2025 evaluation found the EmoLLM model scored **0.00
   on external intervention** — it never once referred a crisis user to professional
   help. We do the opposite, by construction.
3. **Ship-gate:** if red-team false-negative rate on suicidal-ideation prompts
   exceeds **~2%**, do not ship.

## Corrections that must never regress

See `docs/corrections-register.md`. The two with the most direct safety impact:

- **Kashmir Lifeline** is run by the **Healing Minds Foundation** (NOT MSF), number
  **1800-180-7020**, **Sun–Thu 10am–5pm only** — never present it as an after-hours
  crisis line.
- **KIRAN (1800-599-0019)** has been **merged into Tele-MANAS** — never present it as
  a standalone active line. Route to **14416**.

## Running the prototype (Sukoon)

```bash
pip install -r requirements.txt
cp .env.example .env   # add your ANTHROPIC_API_KEY (console.anthropic.com)
uvicorn app.main:app --reload   # http://localhost:8000
pytest                          # tests run without an API key
```

## License & data note

Code license: TBD. Several candidate training datasets are **non-commercial**
(ESConv, MentalManip: CC-BY-NC) or **no-derivatives** (KokoroChat: CC-BY-NC-ND) and
cannot be used to fine-tune a derivative/commercial product — see
`docs/datasets-register.md`. A production launch needs a separately licensed or
self-generated Kashmiri/Urdu corpus.
