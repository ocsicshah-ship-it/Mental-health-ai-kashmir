# Language & Access Engineering

The design constraint that dominates everything: **Kashmir is among the world's most
internet-shutdown-affected regions** (552 days of disruption around 2019–21; the
world's longest democratic shutdown). The system must be usable in low-bandwidth,
intermittent, and offline conditions, in the languages people actually speak.

---

## Languages

| Language | Script(s) | Notes |
|---|---|---|
| **Koshur (Kashmiri)** | Perso-Arabic (standard); Roman code-switching common in SMS/informal | Low-resource; **no Kashmiri mental-health NLP corpus exists** |
| **Urdu** | Perso-Arabic (shared with Kashmiri) | Verified support in Tele-MANAS, Vandrevala; Roman-Urdu resources exist |
| **English** | Latin | Baseline |

- Honor **code-switching** and **Roman-script** input. Roman-Koshur is extremely
  scarce in resources but common in real use — handle gracefully; when unsure of a
  Kashmiri term, prefer clear Urdu/English over a wrong word.

### Tooling for Kashmiri

- **AI4Bharat IndicTrans2** — first open-source NMT covering all 22 scheduled Indic
  languages **including Kashmiri**; models on GitHub/HF (e.g. `indictrans2-en-indic-1B`),
  trained on the Bharat Parallel Corpus Collection (BPCC). https://github.com/AI4Bharat/IndicTrans2
- **Bhashini** — national platform incorporating IndicTrans2; supports Kashmiri.
- **Kashmiri ASR** models exist (AI4Bharat / AIKosh) for any future voice channel.
- **BhashaVerse** (IIIT-Hyderabad) — multilingual model covering 36 subcontinental
  languages incl. Kashmiri in multiple scripts.

> **Gap to plan around:** there is no Kashmiri mental-health corpus. Production-quality
> Koshur counseling content must be **commissioned / self-generated and separately
> licensed** (see `docs/datasets-register.md`).

## Access engineering

- **Text-first, 2G-tolerant.** Optimize payloads for slow, intermittent links. Avoid
  heavy media on the critical path.
- **SMS / WhatsApp-style channel.** Pakistani lines (Umang, Taskeen's 24/7 chatbot)
  demonstrate Urdu-language chat/WhatsApp crisis support at scale — a viable model.
- **Offline-cached crisis block.** `config/crisis-resources.json` must be bundled and
  render **without connectivity**. Life-safety information is never gated on the
  network.
- **Asynchronous-friendly.** Harsh winters ("wande") increase isolation and impede
  travel to services, favoring remote/async support — but this collides with shutdown
  risk, which is exactly why offline capability matters.
- **Benchmark:** usable round-trip latency and full crisis-block rendering on a
  simulated 2G connection, and full crisis-block rendering with the network disabled.
