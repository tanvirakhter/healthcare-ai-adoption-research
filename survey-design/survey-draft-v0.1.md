# Survey Draft v0.1 - Trust, Explainability, and Adoption of Generative AI in Healthcare

Status: working draft. Not for deployment. Requires supervisor review, expert panel review, pilot (n ≈ 20), and ethics approval before any data collection.

Target population: healthcare professionals and managers in UK healthcare organisations.
Response scale unless stated: 5-point Likert (1 = Strongly disagree, 5 = Strongly agree), plus "Not applicable".
Estimated completion time: 8-10 minutes including demographics.

Design note: 15 substantive questions is deliberately lean for a v0.1. The validated instrument will need 3-4 items per construct for acceptable reliability (Cronbach's alpha / composite reliability), so expect the deployed version to run 30-40 items. This draft establishes one to two best items per construct.

---

## Screening and context (not counted in the 15)

- S1. Do you currently work in a healthcare organisation in a clinical, clinical-support, or managerial role? (Yes/No; No → exit)
- S2. Have you used a generative AI tool (e.g. a chatbot or AI assistant that produces text) for any work-related task in the last 12 months? (Yes, sanctioned by my organisation / Yes, on my own initiative / No, but aware of them / No, and unfamiliar)

S2 is analytically load-bearing: it operationalises shadow adoption (RQ3b).

---

## Section A - Performance and effort expectancy (UTAUT)

**Q1.** Using generative AI tools would improve the quality of my work outputs (e.g. documentation, correspondence, summaries).
*Construct: performance expectancy.*

**Q2.** Using generative AI tools would save me meaningful time in a typical working week.
*Construct: performance expectancy (efficiency facet).*

**Q3.** Learning to use generative AI tools effectively, including writing good prompts, would be easy for me.
*Construct: effort expectancy, extended with prompt dependence.*

## Section B - Social and organisational influence (UTAUT / Lambert)

**Q4.** Colleagues whose clinical or professional judgement I respect use, or speak positively about, generative AI tools.
*Construct: social influence.*

## Section C - Trust and risk (Asan / TrAAIT)

**Q5.** I trust the factual accuracy of the content generative AI tools produce.
*Construct: trust - information credibility.*

**Q6.** Generative AI tools perform consistently: similar inputs produce similarly reliable outputs.
*Construct: trust - reliability.*

**Q7.** Generative AI tools add real value to tasks in my role, beyond what existing tools provide.
*Construct: trust - perceived application value.*

**Q8.** I am confident I could detect it if a generative AI tool produced plausible but incorrect clinical or professional content.
*Construct: trust calibration / self-assessed detection ability. Analysed against AI literacy for overconfidence patterns.*

**Q9.** The risk that a generative AI tool fabricates information ("hallucination") makes me unwilling to rely on it for clinically significant tasks.
*Construct: generative-specific risk perception. (Reverse-keyed against trust.)*

**Q10.** If a generative AI tool gave me one clearly wrong answer, I would stop using it for that type of task altogether.
*Construct: trust fragility / recalibration style (RQ1b, H1b).*

**Q11.** I would trust a generative AI tool more if my organisation had formally assessed and approved it.
*Construct: institutional trust transfer (bridges RQ1 and RQ3).*

## Section D - Explainability (Ghassemi / RQ2)

**Q12.** I would trust a generative AI output more if it cited the specific sources its answer was based on, so I could verify them.
*Construct: verifiable explainability (source attribution).*

**Q13.** I would trust a generative AI output more if the tool explained its reasoning in plain language.
*Construct: narrative explainability. Q12 vs Q13 contrast operationalises H2c: verifiable vs self-generated explanation.*

## Section E - Organisational context (Lambert / RQ3)

**Q14.** My organisation provides clear guidance, training, or policy on whether and how I may use generative AI tools in my work.
*Construct: facilitating conditions / governance clarity.*

**Q15.** Within the next 12 months, I intend to use generative AI tools in my work where permitted.
*Construct: behavioural intention (primary dependent variable).*

---

## Demographics (end of survey)

Role category (doctor / nurse / AHP / pharmacist / manager / digital-IT / other); years in profession; organisation type (NHS acute / NHS primary or community / private / other); age band; self-rated AI literacy (1-5); prior formal AI training (Y/N).

## Known weaknesses to fix in v0.2

1. Single-item constructs throughout; unacceptable for SEM, fine for piloting wording.
2. Q9 and Q10 may load on the same factor; pilot will tell.
3. No attention-check item yet.
4. Social desirability risk on Q8 and on shadow-use disclosure (S2); consider indirect wording or guaranteed-anonymity framing.
5. Needs translation of construct mapping into a formal table with source instruments and item provenance.
