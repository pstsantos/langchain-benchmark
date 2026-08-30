## Factual (expected_behavior: answer)

Expected behavior:
- Correct & supported: right answer, grounded in gold_pages content

Red flags / Further study or tests:
- Correct abstention: N/A (a real, findable answer always exists, so declining is never correct)
- Fabrication: wrong or hallucinated answer, or an unsupported claim
- Wrong abstention: says "not found" when the answer was actually retrievable


## Not_in_doc (expected_behavior: abstain)

Expected behavior:
- Correct abstention: correctly states the info isn't in the docs

Red flags / Further study or tests:
- Correct & supported: N/A (there is no real answer to find; gold_pages is empty by definition)
- Fabrication: confidently answers something that doesn't exist in the corpus
- Wrong abstention: N/A (abstaining is always correct here, so there's no wrong version of declining)


## Ambiguous (expected_behavior: disambiguate)

Expected behavior:
- Correct & supported: proactively addresses both readings correctly, grounded in the right pages for each
- Correct abstention: recognizes the ambiguity and asks a clarifying question instead of guessing

Red flags / Further study or tests:
- Fabrication: confidently answers from only one reading without acknowledging the other
- Wrong abstention: refuses to answer at all, without attempting to clarify or acknowledge the ambiguity


## Stale (expected_behavior: flag_change)

Expected behavior:
- Correct & supported: gives the current correct answer AND flags that it changed
- Correct abstention: acknowledges the behavior may be version-dependent and points to checking current docs, without confidently asserting a state it isn't sure of

Red flags / Further study or tests:
- Fabrication: confidently gives the outdated answer, or the current one without flagging the change
- Wrong abstention: refuses to answer at all despite the current answer being available and supported