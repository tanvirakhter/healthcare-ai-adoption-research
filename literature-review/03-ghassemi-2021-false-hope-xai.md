# Paper Summary 03

**Ghassemi, M., Oakden-Rayner, L., & Beam, A. L. (2021). The false hope of current approaches to explainable artificial intelligence in health care. *The Lancet Digital Health*, 3(11), e745-e750.**

## Why this paper

The strongest published counter-argument to the assumption underlying half of this field: that explainability builds appropriate trust. The thesis must engage this critique or RQ2 is naive.

## Summary

Ghassemi and colleagues argue that current explainability methods (saliency maps, LIME, SHAP, and similar post-hoc techniques) do not deliver what clinicians and regulators expect from them. Their case: (1) post-hoc explanations are approximations of model behaviour, not faithful accounts of it, and can be unstable or contradictory for the same prediction; (2) humans are prone to confirmation bias when reading explanations, finding plausible narratives in them whether or not the model's reasoning was sound; (3) explanations can therefore *increase* unwarranted trust rather than calibrate it. They conclude that for individual clinical decisions, rigorous internal and external validation (treating the model like a drug, evaluated by outcomes) is a better trust basis than per-prediction explanation, and that explainability should be reserved for model development, audit, and debugging.

## Key claims

- Post-hoc XAI ≠ faithful model reasoning
- Explanations can manufacture false confidence (a persuasion tool, not a safeguard)
- Validation-based trust > explanation-based trust for deployment decisions

## Relevance to this research

Directly motivates the conditional framing of RQ2 ("under what conditions does explainability fail to help or actively mislead"). For generative AI the critique sharpens: an LLM's natural-language self-explanation is itself a generated output, subject to the same hallucination risk as the answer it explains. This suggests a testable hypothesis (H2c in `research-questions/`): self-generated reasoning traces increase trust without increasing accuracy of trust, whereas verifiable mechanisms (source citation, retrieval grounding, uncertainty flags) support calibration. The survey separates these explainability forms (Q12-Q13) rather than treating "explainability" as one construct, which is a design decision this paper forces.

## Critique / gaps

- Argued from the predictive/imaging paradigm; does not address retrieval-grounded or citation-based explainability, which may escape the unfaithfulness critique.
- Normative position ("don't rely on XAI") is contested; subsequent empirical work shows mixed effects of explanation on trust in both directions, so the question is empirical, which is exactly the space this thesis occupies.

## Status

Read in full. Anchor for RQ2 and hypothesis H2c. Feeds: survey Q12-Q13, interview guide Q8.
