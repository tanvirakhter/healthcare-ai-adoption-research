# Trust, Explainability, and Adoption of Generative AI Systems in Healthcare Organisations

Doctoral research repository. Working documents for literature review, research design, and data collection instruments.

## Research background

Generative AI systems (large language models and related architectures) are moving into healthcare faster than the evidence base supporting their adoption. Documented and piloted use cases include clinical documentation and ambient scribing, patient communication drafting, discharge summaries, triage support, and information retrieval. Unlike earlier predictive AI (risk scores, imaging classifiers), generative systems produce open-ended natural language output, can hallucinate plausible but false clinical content, and resist the post-hoc explainability techniques developed for discriminative models.

The adoption literature for healthcare AI is well developed for predictive systems: trust is repeatedly identified as the primary barrier, and explainability is widely (but not unproblematically) proposed as the mechanism for building it. Whether those findings transfer to generative AI is an open question. Generative systems differ in failure mode (confident fabrication rather than misclassification), in interaction style (conversational, prompt-dependent), and in the locus of accountability (output quality depends partly on the clinician's prompting). The organisational dimension is also underexplored: most existing studies measure individual clinician attitudes, while adoption decisions in practice are made by healthcare organisations under regulatory, procurement, and governance constraints.

## Problem statement

Healthcare organisations are deploying generative AI systems without a validated understanding of how trust forms in these systems, what role explainability actually plays in that process, and which organisational factors convert individual willingness into sustained institutional adoption. Existing trust and acceptance models (TAM, UTAUT, healthcare-specific instruments such as TrAAIT) were built for deterministic or predictive technologies and may not capture the distinctive properties of generative systems: probabilistic output, hallucination risk, prompt dependence, and conversational interaction. This gap leaves organisations choosing between uncritical adoption and blanket restriction, with no evidence-based middle path.

## Research questions

**RQ1.** How do healthcare professionals form, calibrate, and lose trust in generative AI systems, and how does this process differ from trust formation in predictive AI?

**RQ2.** What forms of explainability (e.g. source attribution, uncertainty communication, reasoning traces) influence trust and intention to use generative AI in clinical and administrative workflows, and under what conditions does explainability fail to help or actively mislead?

**RQ3.** Which organisational factors (governance structures, leadership stance, training, regulatory interpretation, peer norms) mediate the relationship between individual trust and organisational adoption of generative AI in healthcare settings?

Full elaboration, sub-questions, and hypotheses: `research-questions/research-questions.md`.

## Methodology

Mixed-methods, sequential explanatory design.

1. **Phase 1 - Systematic literature review.** Trust, explainability, and adoption of AI in healthcare, with a coded distinction between predictive and generative systems. PRISMA-guided. Output: conceptual framework and hypothesis set.
2. **Phase 2 - Quantitative survey.** Cross-sectional survey of healthcare professionals and managers (target n ≥ 200), measuring trust, perceived explainability, performance and effort expectancy, risk perception, and behavioural intention. Constructs adapted from UTAUT and TrAAIT, extended with generative-AI-specific items (hallucination concern, prompt confidence). Analysis: PLS-SEM. Draft instrument: `survey-design/survey-draft-v0.1.md`.
3. **Phase 3 - Qualitative interviews.** Semi-structured interviews (target n = 15-25) with clinicians, clinical safety officers, and digital/IT leaders across 3-5 organisations, to explain and extend the survey findings. Thematic analysis (reflexive TA, Braun & Clarke). Draft guide: `interview-guide/interview-guide-v0.1.md`.
4. **Integration.** Joint display of quantitative paths and qualitative themes; refinement of the trust-explainability-adoption framework for generative AI.

Jurisdictional note: if NHS staff or premises are involved, HRA approval via IRAS is likely required in addition to university ethics; staff-only attitudinal research may qualify for proportionate review. Tracked in `ethics/`.

## Expected contribution

1. **Theoretical.** An extended trust-and-adoption model specific to generative AI in healthcare, identifying where established models (TAM, UTAUT, TrAAIT) hold and where generative properties (hallucination, prompt dependence, conversational interaction) require new constructs.
2. **Methodological.** A validated survey instrument for measuring trust and adoption readiness for generative AI among healthcare professionals.
3. **Practical.** An evidence-based framework healthcare organisations can use to design governance, training, and explainability requirements for generative AI procurement and deployment.

## Timeline

| Period | Milestone |
|---|---|
| Months 1-6 | Systematic literature review; conceptual framework; confirm RQs |
| Months 7-9 | Survey instrument development, expert review, pilot (n ≈ 20) |
| Months 10-12 | Ethics approval (university; HRA/IRAS if NHS); survey deployment |
| Months 13-15 | Quantitative analysis; interim findings paper |
| Months 16-21 | Interviews and thematic analysis |
| Months 22-27 | Integration; framework refinement; second paper |
| Months 28-36 | Thesis writing, submission, viva preparation |

## Repository structure

```
literature-review/    Paper summaries and synthesis notes
research-questions/   RQs, sub-questions, hypotheses
survey-design/        Survey instrument drafts and construct mapping
interview-guide/      Interview protocols
frameworks/           Theoretical models under consideration
ethics/               Ethics applications, consent forms, data management plan
```
