# Grader Validation Log

Made up good/bad answers per category, run through Gemini 3.6 Flash, checked against expected label. 

Purpose : confirm the rubric + grader_prompt.md combination produces correct labels before trusting it on real system output.

---

## Q001 (factual) — good answer
Expected: correct_and_supported
Gemini 3.6 Flash output: correct_and_supported
Match: yes
Gemini's reasoning: The system's answer directly matches the reference answer
and gold page details by explaining that a checkpointer is required for
history to persist, is auto-provisioned on LangSmith, and must be passed
explicitly when running locally.

## Q001 (factual) — bad answer
Expected: fabrication
Gemini 3.6 Flash output: fabrication
Match: yes
Gemini's reasoning: The system's answer incorrectly claims that conversation
history persists automatically without a checkpointer, directly contradicting
the reference answer.

---

## calibration-only not_in_doc test (enterprise pricing question, not in questions.jsonl) — good answer
Expected: correct_abstention
Gemini 3.6 Flash output: correct_abstention
Match: yes
Gemini's reasoning: The system's answer correctly abstains by stating that
the requested pricing information is not present in the accessible
documentation set.

## calibration-only not_in_doc test (enterprise pricing question, not in questions.jsonl) — bad answer
Expected: fabrication
Gemini 3.6 Flash output: fabrication
Match: yes
Gemini's reasoning: The system's answer confidently provides specific pricing
and seat count figures for a question where no answer exists in the
documentation corpus.

---

## Q021 (ambiguous) — good answer
Expected: correct_and_supported
Gemini 3.6 Flash output: correct_and_supported
Match: yes
Gemini's reasoning: The system's answer proactively addresses both possible
interpretations of streaming (chat model output vs. event streaming)
correctly and in accordance with the gold page content.

## Q021 (ambiguous) — bad answer
Expected: fabrication
Gemini 3.6 Flash output: fabrication
Match: yes
Gemini's reasoning: The system's answer confidently answers from only one
reading without acknowledging the potential ambiguity or the alternative
streaming mechanism.

---

## Q041 (stale) — good answer
Expected: correct_and_supported
Gemini 3.6 Flash output: correct_and_supported
Match: yes
Gemini's reasoning: The system's answer gives the current answer regarding
the single agent abstraction while explicitly flagging that the older
LLMChain definition was deprecated in v1.0.0.

## Q041 (stale) — bad answer
Expected: fabrication
Gemini 3.6 Flash output: fabrication
Match: yes
Gemini's reasoning: The system's answer confidently provides the outdated
2023 definition of LLMChain without flagging that the abstraction was
deprecated and replaced in v1.0.0.

