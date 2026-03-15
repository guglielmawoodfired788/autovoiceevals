# autovoiceevals — protocol

Adapted from [karpathy/autoresearch](https://github.com/karpathy/autoresearch). Same pattern, different domain.

| autoresearch | autovoiceevals |
|---|---|
| `train.py` — code the agent edits | System prompt — artifact being optimized |
| `val_bpb` — lower is better | Composite eval score — higher is better |
| 5-minute training run | Run N adversarial scenarios (~3 min) |
| `prepare.py` — fixed eval harness | Fixed eval suite — generated once at startup |
| `results.tsv` | `results.tsv` |

## Three things that matter

- **Eval suite** — generated once at startup. Fixed set of adversarial scenarios with caller personas, attack strategies, and pass/fail criteria. This is the validation set. Never modified during a run.
- **System prompt** — the single artifact being optimized. The AI proposes ONE change per experiment. Everything is fair game: add rules, reword instructions, remove redundancy, restructure.
- **`results.tsv`** — experiment log. Tab-separated: experiment, score, csat, pass_rate, prompt_len, status, description.

## The loop

```
SETUP:
  1. Connect to voice platform, read current system prompt
  2. Generate fixed eval suite (adversarial scenarios)
  3. Run baseline, record score

LOOP FOREVER:
  4. AI proposes ONE change to the prompt
  5. Push modified prompt to the platform via API
  6. Run full eval suite against the modified agent
  7. Score improved?        → KEEP
  8. Score equal, shorter?  → KEEP (simplicity wins)
  9. Score equal or worse?  → DISCARD, revert to previous best
  10. Log to results.tsv
  11. Go to 4. Never stop. Never ask. Run until interrupted.
```

## Scoring

```
composite = should_weight * should_score
          + should_not_weight * should_not_score
          + latency_weight * latency_score
```

Default weights: `0.50 / 0.35 / 0.15`. Configurable in `config.yaml`.

- `should_score` — fraction of "agent should do X" criteria passed
- `should_not_score` — fraction of "agent should NOT do X" criteria passed
- `latency_score` — 1.0 if avg response < threshold, else 0.5

Experiment metric = average composite across all eval scenarios.

## What the AI can change

The system prompt. Everything is fair game:
- Add explicit rules, boundary definitions, escalation procedures
- Reword existing instructions for clarity
- Remove redundant or ineffective text
- Restructure sections, add/remove examples
- Change tone, add constraints

## What the AI cannot change

- The eval suite (fixed at startup)
- The scoring formula
- The agent's model or provider
- The conversation simulation logic

## Simplicity criterion

All else being equal, simpler is better. A prompt that achieves the same score with fewer characters is a win. A small improvement that adds ugly complexity is not worth it. Removing something and getting equal results is a great outcome.

## On stop

When interrupted (Ctrl+C or max_experiments reached):
1. Print summary — experiments, kept/discarded, score progression
2. Restore original prompt on the platform
3. Save best prompt to `results/best_prompt.txt`
4. Save full log to `results/autoresearch.json`

## Providers

| Provider | Conversations | Prompt read/write |
|---|---|---|
| Vapi | Live via Chat API | GET/PATCH assistant |
| Smallest AI | Simulated via Claude + system prompt | GET/PATCH workflow |

## results.tsv

```
experiment  score     csat  pass_rate  prompt_len  status   description
0           0.875     88.4  0.800      6615        keep     baseline
1           0.712     81.4  0.800      6962        discard  Add confusion-detection instructions
2           0.925     87.6  1.000      7047        keep     Add impossible date/time handling
3           0.900     86.4  1.000      6670        discard  Remove redundant personality guidance
4           0.925     88.4  1.000      4901        keep     Simplify conversation flow
5           0.925     90.4  1.000      4719        keep     Remove meta-commentary section
```
