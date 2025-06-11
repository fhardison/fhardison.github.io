
---
layout: post
title: Prompt for Challenge A/B Latin converstaion table
date: 2025-06-11
tags: prompts
---


This prompt generates a converstion sheet for Latin language learning based on a vocab list. It's designed for helping to generate a learning activity for Classical Conversations Challenge Latin seminars that use the Henle Latin text book. See [this blog post](../blog/latin-ai.html) for more info


```
  
Create a Latin conversation table based on a provided vocabulary list, formatted in markdown with pipe syntax, matching the structure and rules of the example table below. The table must have five columns: Subject, Object, Adverb, Verbs, Gloss. Follow these requirements:

- Vocabulary List: Use the nouns and verbs from the provided vocabulary list. If the list has fewer than five verbs, add common Latin verbs that relate to the vocabulary to enable a simple, cohesive story (e.g., actions involving the nouns). Include English glosses for any added verbs in the Gloss column. Always add 'to come' and 'to go' in the verb list
- Subjects: Include nouns from the vocabulary list and pronouns (ego, tu, is, ea) as subjects. Place pronouns in parentheses (e.g., (ego)) as they are optional. Align subjects with the correct verb forms for 1st, 2nd, and 3rd person singular. Group verbs by person (1st: ego, 2nd: tu, 3rd: is/ea/id/nouns). 
- Objects: Select nouns from the vocabulary list as objects, placed in the accusative case where appropriate for transitive verbs. Objects do not need to agree with verb forms. Leave some rows without objects if suitable.
- Verbs: Use verbs from the vocabulary list, supplemented with added verbs if needed. Conjugate verbs for 1st, 2nd, and 3rd person singular to match the subject. Include the English gloss for each verb (from the vocabulary or added).
- Adverbs: Include exactly five adverbs, one of which must be nōn (not). Each adverb must appear only once in the Adverb column, with its English gloss in parentheses (e.g., semper (always)). Place adverbs in rows where they complement the verb and context (e.g., "always" with praying, "now" with seeing). Leave some rows without adverbs if necessary.
- Story Potential: Ensure the table supports a simple narrative (e.g., characters performing actions like praying, seeing, or moving, involving the nouns). Distribute verbs, adverbs, and objects to enable coherent sentences.



Example Table (use this structure and style as a template):


| Subject       | Object      | Adverb          | Verbs     | Gloss        |
|:-------------|:-------------|:----------------|:----------|:-------------|
| (ego)        | terram       | semper (always) | ōrō       | I pray       |
|              | servum       |  bene (well)    | videō     | I see        |
|              | Deum         |  nunc (now)     | laudō     | I praise     |
|              | Chrīstum     |  nōn (not)      | amō       | I love       |
|              | prōvinciam   |  forte (by chance) | eō     | I go         |
| (tu)         | glōriam      |                 | ōrās      | you pray     |
|              | nautam       |                 | vidēs     | you see      |
|              | Marīam       |                 | laudās    | you praise   |
|              | amīcum       |                 | vocās     | you call     |
|              | portam       |                 | īs        | you go       |
| (is)         |              |                 | ōrat      | he prays     |
| (ea)         |              |                 | videt     | she sees     |
| (id)         |              |                 | laudat    | he praises   |
| Marīa        | Chrīstum     |                 | amat      | loves        |
| servus       | portam       |                 | ambulat   | walks        |
| Deus         |              |                 | venit     | comes        |
| Chrīstus     |              |                 | vocat     | calls        |
| porta        |              |                 |           |              |
| victōria     |              |                 |           |              |
| glōria       |              |                 |           |              |
| nauta        |              |                 |           |              |
| prōvincia    |              |                 |           |              |
| amīcus       |              |                 |           |              |
| Chrīstiānus  |              |                 |           |              |



# Prompt Instructions:

When provided with a new vocabulary list, generate a table following the above rules and structure.
- Ensure all nouns from the list appear as subjects (even if without verbs), and select appropriate objects from the list.
- Choose five distinct adverbs (including nōn) that fit the verbs and context, using each only once.
- If additional verbs are needed, select common Latin verbs that support a simple story with the nouns (e.g., movement or interaction verbs).
- Provide a brief explanation after the table, noting which verbs (if any) were added, how adverbs were chosen, and how the table supports a simple story.

# VOCAB LIST```
