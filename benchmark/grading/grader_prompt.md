# Grader Prompt Template

You are grading one answer from an AI system against a benchmark question.
You are NOT the model that produced this answer -- you are an independent
grader. Apply the rubric below exactly; do not use outside knowledge to
second-guess whether the reference answer itself is right.

Question: {question}
Category: {category}
Gold pages: {gold_pages}
Reference answer: {reference_answer}
Expected behavior: {expected_behavior}

System's answer to grade: {system_answer}

---

> Note: the rubric text below is manually copied from `rubric.md` for each
> test case during this initial manual-validation phase (see
> `grader_validation.md`). Once the actual multi-agent system exists and
> grading needs to run at scale, this will be automated - a script will
> read `rubric.md` directly and insert the relevant category's section
> here, rather than this being pasted by hand. `rubric.md` remains the
> single source of truth for rubric definitions either way.

Rubric for this category:

Expected behavior (these count as success):
{paste the "Expected behavior" bullets for this category from rubric.md}

Red flags / further study or tests (these count as failure):
{paste the "Red flags" bullets for this category from rubric.md, excluding any marked N/A}

---

Using only the rubric above, output exactly one label:
correct_and_supported | correct_abstention | fabrication | wrong_abstention

Then, on a new line, give one sentence explaining which specific part of
the rubric justifies that label.