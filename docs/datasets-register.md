# Datasets & License Register

**License-critical.** Several widely-used mental-health dialogue datasets are
**non-commercial** or **no-derivatives**, which constrains fine-tuning and any
commercial deployment. Treat the table below as the authority before training on
anything. A production (potentially commercial) launch must source **separately
licensed or self-generated** data.

---

## Counseling / support dialogue datasets

| Dataset | Source / Repo | License | Commercial / derivative use | Size / Notes |
|---|---|---|---|---|
| **ESConv** (Liu et al. 2021) | HF `thu-coai/esconv` | **CC-BY-NC-4.0** | ❌ non-commercial | 1,300 strategy-annotated multi-turn dialogues |
| **MentalChat16K** (KDD 2025) | HF `ShenLab/MentalChat16K` | research use | ⚠️ research only | 16,113 QA (6,338 real PISCES + 9,775 synthetic) |
| **CounselChat** | Bertagnolli; HF mirrors | research/open | ⚠️ check | ~3.6k Q&A |
| **Psych8k** (ChatPsychiatrist) | Liu et al. 2023 | research use | ⚠️ research only | ~8k pairs from 260 real recordings |
| **EmpatheticDialogues** | `facebookresearch/EmpatheticDialogues` | research/open | ⚠️ check | ~25k empathetic conversations |
| **KokoroChat** (ACL 2025) | HF `UEC-InabaLab/KokoroChat` | **CC-BY-NC-ND-4.0** | ❌❌ **no derivatives** | 6,589 Japanese counseling dialogues — **cannot be used to fine-tune a derivative** |
| **MentalManip** (ACL 2024) | HF `audreyeleven/MentalManip` | **CC-BY-NC-4.0** | ❌ non-commercial | 4,000 annotated dialogues; manipulation-technique taxonomy (useful for coercive-control module) |
| **EmoCare** | referenced in Mentalic Net eval | research | ⚠️ research only | counseling-style data |

### Methodological references (Chinese-language work — design lessons, not training data)

- **PsyQA** (Sun 2021): 22K Q / 56K structured answers; strategy-annotated.
- **SoulChat / SoulChatCorpus** (Chen 2023): 2M+ empathetic conversations.
- **SMILE / SmileChat** (Qiu 2024): PsyQA single→multi-turn expansion.
- **CPsyCoun / CPsyCounD** (Zhang, ACL 2024): report-based multi-turn reconstruction.
- **EmoLLM** (SmartFlowAI): open Chinese mental-health LLM suite (MIT code/models).

> **Safety lesson baked into our spec:** a 2025 evaluation found SoulChat and EmoLLM
> produced very short replies and scored poorly on risk assessment (<0.09); **EmoLLM
> scored 0.00 on external intervention** (never referred to professional help). Both
> Chinese and Japanese (KokoroChat) work flag **family-dynamics scenarios** as a weak
> spot — directly relevant to Kashmiri joint-family contexts. → see
> `safety/crisis-classifier-spec.md`.

## Kashmiri / Urdu language resources

See `docs/language-access.md`. Key point: **IndicTrans2 / Bhashini** cover Kashmiri,
but **no Kashmiri mental-health corpus exists** — commission/self-generate it.

## Decision rules

1. **Do not** use CC-BY-NC datasets (ESConv, MentalManip) to train a commercial model.
2. **Never** use **KokoroChat** to fine-tune anything — the **ND** clause forbids
   derivatives outright.
3. Use the permissively-licensed/research subset for **research and evaluation** only.
4. For production, build a **separately licensed or self-generated** Kashmiri/Urdu
   counseling corpus (ideally with a partner such as Kashmir Lifeline / Healing Minds
   Foundation, whose providers are Kashmiri and trauma-informed).
5. Keep a per-dataset provenance + license record in any training pipeline.
