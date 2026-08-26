# langchain-benchmark

Benchmark task for evaluating agent retrieval and factual correctness against a locked LangChain documentation corpus.

> **Status:** v2 in progress. Corpus has been expanded; question set and task definition updates are next.

## Task

Given a user question, the agent system must retrieve the relevant passage from the corpus and produce a factually correct answer, including recognizing when a question can't be answered from the corpus, when it maps to multiple conflicting pages, or when it relates to information that has since changed.

An answer is correct if it is traceable to a specific page in the corpus.

## Corpus

- **Source:** LangChain (Python) documentation — Build section, core components, and advanced usage — plus LangGraph, including related frontend/UI integration pages.
- **Location:** [`corpus/`](corpus/)
- **Size:** 88 files, ~644,227 tokens 
- **Locked/frozen:** August 10, 2026, 12:00 PM 


Count tokens with:

```bash
pip install tiktoken
python3 count_tokens.py
```

## Trap Categories

- **Not in doc** — question has no answer anywhere in the corpus; tests whether the agent admits uncertainty instead of fabricating a response.
- **Ambiguous** — question maps to two related-but-distinct pages; tests whether the agent distinguishes them instead of merging them.
- **Stale/versioned** — question concerns something the documentation itself shows has changed over time.

## Question Set

100–120 questions total, roughly 1 per original corpus page, spanning normal retrieval and all three trap categories.