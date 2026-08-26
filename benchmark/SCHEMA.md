# Benchmark Item Schema

Each line in `questions.jsonl` is a single JSON object representing one benchmark item. This file is the authoritative schema definition — version-controlled here rather than tracked only in Notion or a spreadsheet.

## Fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier, e.g. `"Q001"`. |
| `question` | string | The question text, phrased as a real developer would ask it. |
| `category` | string | One of `factual` \| `not_in_doc` \| `ambiguous` \| `stale`. |
| `gold_pages` | list[string] | Filename(s) of the corpus page(s) containing the answer. Empty list `[]` for `not_in_doc`. |
| `gold_section` | string | The section/heading on the gold page where the answer is found, if it can be pinned down. May be empty. |
| `reference_answer` | string | The correct answer, verified against the gold page(s) before being logged. |
| `expected_behavior` | string | The behavior a correct agent response should exhibit. One of `answer` \| `abstain` \| `disambiguate` \| `flag_change`. |
| `source` | string | One of `original` \| `adapted_from_langchain_dataset`. |
| `notes` | string | Free-text notes — verification status, provenance, caveats. |

## category → expected_behavior mapping

| category | expected_behavior |
|---|---|
| `factual` | `answer` |
| `not_in_doc` | `abstain` |
| `ambiguous` | `disambiguate` |
| `stale` | `flag_change` |

## Corpus tier rule

`gold_pages` must be drawn from the 18 Core corpus pages only. Background pages (the remaining 70 files) are never gold pages — they exist solely as retrieval distractors.

**Exception:** absence for `not_in_doc` items must be verified against the full 88-file corpus (Core + Background), since that is the full search space the evaluated agent operates over — not just the 18 Core pages.

## Versioning

The corpus is frozen and versioned (`corpus-v1`; see per-file front matter: `source_url`, `retrieval_date`, `doc_version`). This item schema is versioned the same way — changes to field definitions should be made here and committed, not silently changed in a spreadsheet.