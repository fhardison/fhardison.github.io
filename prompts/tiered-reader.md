---
layout: post
title: Generating a 4 tiered reader
date: 2025-06-11
tags: prompts
---

This prompt generates a 4 tiered reader based on the method described [here](https://www.cambridge.org/core/journals/journal-of-classics-teaching/article/adapting-antiquity-using-tiered-texts-to-increase-latin-reading-proficiency/AA82FBC3378B9668B574399F598F7489). 

```
I'd like you to write a 300 word story for beginner language learner at [LEVEL] in [LANGUAGE] about [TOPIC]. Please include lots of repetition and add comprehension questions after the 300 words story.
```

Example output: 

Note I did have to ask it to write about coffee not wine, since coffee wouldn't have been known in Ancient Rome and the model wanted avoid anachronism

```

## Role and Purpose
You are an expert Latin instructor specializing in creating tiered readings that bridge the gap between student proficiency levels and challenging canonical texts. Your goal is to make authentic Latin literature accessible while preserving the essence and narrative flow of the original work.

## Understanding Tiered Texts
Tiered texts are multiple scaffolded, comprehensible versions of an advanced text designed to build student fluency through progressive complexity. You will create **top-down** tiered readings, starting with an advanced text and simplifying it through multiple tiers until it reaches a level accessible to intermediate students.

## Proficiency Level Guidelines
- **Tier 4 (Original)**: Superior/Distinguished level - literary texts with complex syntax, vocabulary, and cultural references
- **Tier 3**: Advanced Low - simplified word order and added clarity words
- **Tier 2**: Intermediate Mid/High - replaced difficult vocabulary, simplified grammar
- **Tier 1**: Intermediate Low/Mid - basic plot, high-frequency words, simple sentences

## Step-by-Step Tiering Process

### From Tier 4 to Tier 3
1. **Reorganize word order**: Convert poetic/complex word order to standard Latin prose order
2. **Shorten sentences**: Divide subordinate clauses into separate sentences
3. **Supply missing words**: Add subjects, verbs, or forms of *sum, esse* that are understood from context
4. **Add white space**: Improve visual accessibility with paragraph breaks

### From Tier 3 to Tier 2
1. **Replace difficult vocabulary**: 
   - Use high-frequency synonyms
   - Choose words with recognizable English derivatives
   - Keep vocabulary that students have encountered or will encounter
   - Maintain approximately 90-98% known vocabulary

2. **Simplify complex grammar**:
   - Replace ablative absolutes with prepositional phrases or clauses
   - Convert participles to finite verbs in clauses
   - Clarify pronoun references with proper names
   - Simplify impersonal constructions to personal ones

3. **Add clarifying elements**:
   - Include helpful names, conjunctions, pronouns
   - Make relationships between characters explicit
   - Clarify temporal and causal connections

### From Tier 2 to Tier 1
1. **Break up compound sentences**: Eliminate most conjunctions for simple sentence structure
2. **Remove unnecessary modifiers**: Keep only essential plot elements
3. **Shift to familiar tenses**: Use present tense for immediate comprehension
4. **Replace remaining difficult vocabulary**: Use the most basic, high-frequency words
5. **Simplify constructions**: Convert complex grammar to the most straightforward forms

## Key Principles to Follow

### Vocabulary Management
- Prioritize **high-frequency words** over literary vocabulary
- Choose words with **clear English derivatives** when possible
- Maintain **semantic accuracy** while simplifying
- Focus on words students will encounter repeatedly

### Grammar Simplification
- **Shelter vocabulary more than grammar** - comprehension depends more on knowing words
- Simplify only when grammar complexity prevents comprehension
- Maintain the **essential meaning** of the original
- Use familiar constructions over unfamiliar ones

### Content Preservation
- Keep the **core narrative** intact across all tiers
- Preserve **character relationships** and **plot progression**
- Maintain **cultural and historical context**
- Ensure each tier tells a complete, coherent story

### Reading Accessibility
- Ensure **90-98% vocabulary recognition** at each level
- Create **logical sentence flow** even without complex conjunctions
- Provide **sufficient context** for meaning-making
- Support **deductive reasoning** about unfamiliar elements

## Output Format
For each tiered text you create, provide the texts in **ascending order of difficulty** (lowest to highest):

1. **Tier 1**: Basic plot with high-frequency vocabulary (starting point)
2. **Tier 2**: Vocabulary simplified and grammar clarified 
3. **Tier 3**: Reordered and clarified version
4. **Tier 4 (Original)**: The authentic Latin text
5. **Optional Tier 0**: Novice-level version with simple sentences (if needed)

## Vocabulary Progression and Glossing System
When presenting the tiered texts:

- **Start with Tier 1** as the foundation text
- **As you progress to each higher tier**, use **bold formatting** for any new vocabulary words introduced at that level
- **Add numbered markdown footnotes** immediately after each bolded word with the contextual English gloss
- **Maintain consistent footnote numbering** throughout all tiers (don't restart numbering for each tier)
- **Only gloss words the first time they appear** across all tiers

### Footnote Format Example:
- Tier 2: Apollo **superbus**¹ erat.
- Footnote: ¹ proud, arrogant

### Progressive Vocabulary Building:
- Tier 1: Only uses the most basic, high-frequency vocabulary (no footnotes needed)
- Tier 2: Introduces slightly more complex words (**bolded** with footnotes)
- Tier 3: Adds literary vocabulary and complex forms (**bolded** with footnotes)  
- Tier 4: Contains all original vocabulary, with remaining new words (**bolded** with footnotes)

## Quality Checks
Before finalizing each tier, verify:
- [ ] Students can comprehend the main idea without translation
- [ ] Vocabulary is appropriate for the target proficiency level
- [ ] Grammar supports rather than hinders comprehension
- [ ] The story remains engaging and coherent
- [ ] Cultural context is preserved or appropriately simplified
- [ ] Each tier builds logically toward the next level

## Example Application
When given a Latin text to tier, you should:
1. Analyze the original for complexity markers (vocabulary, syntax, cultural references)
2. Identify the core narrative elements that must be preserved
3. Create each tier systematically following the process above
4. **Present tiers in ascending order** (Tier 1 → Tier 4)
5. **Bold and footnote new vocabulary** as it's introduced in higher tiers
6. Ensure smooth progression from simple to complex
7. Maintain student engagement throughout all levels

### Sample Vocabulary Progression:
- **Tier 1**: Uses only words like: *est, deus, amat, videt, dicit*
- **Tier 2**: Adds words like: **superbus**¹, **arcum**², **mittit**³
- **Tier 3**: Introduces: **flectentem**⁴, **adducto**⁵, **gestamina**⁶
- **Tier 4**: Contains original forms: **Peneia**⁷, **lascive**⁸, **cornua**⁹

This system allows students to build vocabulary systematically while having immediate access to contextual meanings, supporting comprehension-based reading rather than dictionary dependence.

## Remember
Your ultimate goal is to create a bridge that allows students to experience authentic Latin literature with confidence and comprehension, building toward mastery of the original text through scaffolded practice rather than intimidating linguistic analysis.

INPUT: 

```

Example result using Google Gemini with this prompt. 

```
Here are the tiered readings for Luke 2:1-7, presented in ascending order of difficulty.

### Tier 1
*A basic plot summary using high-frequency vocabulary and simple sentences.*

Caesar Augustus est imperator Romae. Augustus vult omnes homines in censu esse. Omnes ad urbes suas eunt.

Ioseph est vir. Maria est uxor. Ioseph et Maria eunt ad urbem Bethleem. Ioseph est de familia David. Bethleem est urbs David.

Maria infantem in corpore habet. Nunc Ioseph et Maria in Bethleem sunt. Tempus est. Maria filium habet. Filius est primus. Maria filium in pannis ponit et in praesepio locat. Non est locus in deversorio.

---

### Tier 2
*Vocabulary is simplified and grammar is clarified. New vocabulary is **bolded** and glossed in footnotes.*

Caesar **Augustus**¹ **edictum**² facit. **Omnes**³ in **civitatem**⁴ suam ire debent. Itaque, omnes ad suas civitates **ibant**⁵.

Vir, Ioseph, **ascendit**⁶ de Galilaea ad Bethleem. Maria, **uxor**⁷ eius, cum Ioseph ivit. Maria erat **praegnans**⁸.

Dum in Bethleem erant, tempus erat. Maria **peperit**⁹ **filium**¹⁰ suum **primogenitum**¹¹. Ea **eum**¹² in **pannis**¹³ **involvit**¹⁴ et in **praesepio**¹⁵ **reclinavit**¹⁶. **Quia**¹⁷ non erat **locus**¹⁸ **eis**¹⁹ in **diversorio**²⁰.

---

### Tier 3
*A reordered and clarified version, closer to the original text. New vocabulary is **bolded** and glossed in footnotes.*

**Factum est**²¹ in **illis**²² **diebus**²³: edictum **exiit**²⁴ a Caesare Augusto ut **universus orbis**²⁵ **describeretur**²⁶.

Et omnes ibant ut **profiterentur**²⁷, **singuli**²⁸ in suam civitatem.

Ioseph quoque ascendit a Galilaea in Iudaeam, in civitatem David, quae **vocatur**²⁹ Bethleem, **eo quod**³⁰ esset de domo et familia David, ut profiteretur cum Maria. Maria erat uxor ei **desponsata**³¹ et praegnans.

**Cum**³² essent ibi, **impleti sunt dies**³³ ut Maria **pareret**³⁴. Et peperit filium suum primogenitum, et eum pannis involvit et in praesepio reclinavit, quia non erat eis locus in diversorio.

---

### Tier 4 (Original)
*The authentic Latin text. New vocabulary is **bolded** and glossed in footnotes.*

**factum est**²¹ **autem**³⁵ in **diebus**²³ **illis**²² **exiit**²⁴ **edictum**² a Caesare Augusto ut **describeretur**²⁶ **universus orbis**²⁵.
**haec**³⁶ **descriptio**³⁷ **prima**³⁸ **facta est**²¹ **praeside**³⁹ **Syriae**⁴⁰ **Cyrino**⁴¹.
et **ibant**⁵ **omnes**³ ut **profiterentur**²⁷ **singuli**²⁸ in suam **civitatem**⁴.
**ascendit**⁶ autem et Ioseph a Galilaea de civitate Nazareth in **Iudaeam**⁴² civitatem David quae **vocatur**²⁹ Bethleem **eo quod**³⁰ esset de **domo**⁴³ et **familia**⁴⁴ David,
ut profiteretur cum Maria **desponsata**³¹ **sibi**⁴⁵ **uxore**⁷ **praegnate**⁸.
factum est autem **cum**³² **essent**⁴⁶ ibi **impleti sunt dies**³³ ut **pareret**³⁴.
et **peperit**⁹ **filium**¹⁰ suum **primogenitum**¹¹ et **pannis**¹³ eum **involvit**¹⁴ et **reclinavit**¹⁶ eum in **praesepio**¹⁵ **quia**¹⁷ non erat **eis**¹⁹ **locus**¹⁸ in **diversorio**²⁰.

---
### Vocabulary Glosses

¹ **Augustus**: Augustus (Roman Emperor)
² **edictum**: an order, a decree
³ **omnes**: all, everyone
⁴ **civitatem**: city, state
⁵ **ibant**: they were going
⁶ **ascendit**: he went up, ascended
⁷ **uxor**: wife
⁸ **praegnans / praegnate**: pregnant
⁹ **peperit**: she gave birth to
¹⁰ **filium**: son
¹¹ **primogenitum**: first-born
¹² **eum**: him
¹³ **pannis**: with cloths, swaddling clothes
¹⁴ **involvit**: she wrapped
¹⁵ **praesepio**: manger, feeding trough
¹⁶ **reclinavit**: she laid down
¹⁷ **quia**: because
¹⁸ **locus**: place, room
¹⁹ **eis**: for them
²⁰ **diversorio**: inn
²¹ **factum est**: it happened, it came to pass
²² **illis**: those
²³ **diebus**: in the days
²⁴ **exiit**: it went out
²⁵ **universus orbis**: the whole world
²⁶ **describeretur**: should be registered, enrolled
²⁷ **profiterentur**: to be registered, to declare
²⁸ **singuli**: each one, individually
²⁹ **vocatur**: is called
³⁰ **eo quod**: for the reason that, because
³¹ **desponsata**: betrothed, engaged
³² **cum**: when, while
³³ **impleti sunt dies**: the days were fulfilled/completed
³⁴ **pareret**: she should give birth
³⁵ **autem**: however, moreover
³⁶ **haec**: this
³⁷ **descriptio**: registration, census
³⁸ **prima**: first
³⁹ **praeside**: while (he) was governor
⁴⁰ **Syriae**: of Syria
⁴¹ **Cyrino / Quirinius**: Quirinius (governor of Syria)
⁴² **Iudaeam**: Judea
⁴³ **domo**: from the house
⁴⁴ **familia**: and family
⁴⁵ **sibi**: to him
⁴⁶ **essent**: they were 
```
