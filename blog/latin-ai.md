---
layout: post
title: AI prompt for Henle Latin conversation chart
date: 2025-06-07
tags: latin
---

Does Henle Latin fill you with joy?

For me, not exactly. It's taken me a while to figure out why. As a linguist and language learner it's clear that Henle is a grammar-translation based text and I think is a fine example thereof. 

The main issue is that grammar-translation is an indirect route to language acquisition because languages aren't learned, they are acquired by our brains through exposure to meaningful and comprehensible input. 

This means that memorizing a bunch of words and grammar rules leads to acquisition after the student has struggled to figure out how to translate difficult sentences that probably don't relate to their lives or things they want to talk about. The brain therefore may not see this as helpful information and not "learn" it very quickly. In any case this method is less pleasant for the student. 

This is language acquisition through the back door. 

But, what if we could go directly through the front door?

Well we can. 

This is what more and more modern Latin classrooms are doing. They are using more grammar and smaller sets of vocabulary and doing activities aimed at engaging students in processing meaningful and comprehensible language. This requires(1)  a teacher who knows Latin well enough to speak or write it in class with students and (2) requires materials that students can read or listen to that they can understand at their level. 

Point (2) is not that difficult. There are more and more people producing easy to read Latin material for beginners like [Magister P's novellas](https://magisterp.com/novellas/) and [Carla Hurt](https://foundinantiquity.com/comprehensible-input-resources/) (see especially her "The Lover's Curse", probably better for more advanced students). There are also numerous older texts that are public domain and probably relatively comprehensible for beginners after they have some Latin under their belts (see [Carolus et Maria](https://archive.org/details/fay-marjorie-carolus-et-maria) and [Cornelia](https://archive.org/details/maxey-mima-cornelia-1933) for example). Of course there is also [Lingua Latina per se Illustrata](https://www.amazon.com/Lingua-Latina-Illustrata-Pars-Familia/dp/1585104205), which is fantastic, but not public domain.

Point (1) is more difficult. 

I'm a Classical Conversations director for Challenge B. I directed A last year. My Latin is not great. I've read bits of the texts mentioned above, but I'm far better in Koine Greek than Latin. I assume most new Challenge directors, like me, aren't Latin teachers who have learned to speak or write the language with any fluency. Also, we are required to teach using Henle following a set curriculum.

Enter AI. Below you will find a rather long prompt you can paste into the AI of your choice along with the list of vocabulary for the week (I usually use Claude, Gemini, or Grok; Claude is probably the best at this point).  

It then generates a table that can be used to build stories and conversations with the students using the assigned vocabulary. This activity fills the slot where most directors would be playing some kind of Latin vocab game. So we're still teaching from Henle as required, and still covering the required materials for the week. But, we're doing so in a way that directly promotes language acquisition through the front door.


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

# VOCAB LIST
  
```

# Method to the madness

Teaching Proficiency through Reading and Storytelling (TPRS) is the method underlying this madness (YouTube is full of videos about it) with the addition of some of Tony Marsh's ideas on using AI tools to generate conversation charts (see [here](https://youtu.be/-eb2gsF51E4?si=KFkBLd5sIKv8rApG)). 

In TPRS one of the principles is personalized question asking. In other words, develop a story using on the of students names' as the name of the character (with their permission of course). 

So, here's how I'd use the chart.

*Prep*

1. Use the prompt + vocab list to generate a chart from AI. Take a minute to think about what other words you might need to be able to build a story or conversation using this chart. Skim the explanation for yourself, but you probably don't need to give it to the students.
2. Copy the chart into a document.
3. Ask AI how to say the extra words you need and add them to your chart/document. 
4. Bring in a questions poster to hang on the board with the following questions:
  - Quid agit? 'What is he/she/it doing?'
  - Quis agit? 'Who does (it)?'
  - Ubi agit? 'Where did he/she/it do (it)?'
  - Cūr agit? 'Why did he/she/it do it?'
  - Quō mōdo agit? 'How did he/she/it do it?'
  - Quid deinde accidit? 'What happens next?'
  - Quid diende agit? 'What does he/she/it do next?'

I'd also recommend adding the following words from Magister P's list of [52 Most Important Latin Verbs](https://docs.google.com/document/d/1Aq0cKM5j_qPrwuZCggNPuBV8KsX1Eaa80k6vHZ7c75M/edit?tab=t.0):


---

| 1st SG | 3rd SG | Inf | English |
|---|---|---|---|
| dō | dat | dare | give |
| pōnō | pōnit | pōnere | put down |
| videō | videt | vidēre | see |
| possum | potest | posse | be able |
| audiō | audit | audīre | listen |
| veniō | venit | venīre | arrive |
| ferō | fert | ferre | carry |
| discēdō | discēdit | discēdere | depart |
| eō | it | īre | to go |
| volō | vult | velle | to wish, to want |
| mihi placeet | eī placet | placēre | to please |


Why these words? They facilitate discussion and narration. Why 1st and 3rd person, and infinitives?  These allow us to answer for ourselves and narrate what someone else is doing. Also, the infinitive tells us what conjugation the word belongs to so we can figure out other forms as needed by referring to a grammar chart. 

You can get away without them as you'll see in the example below, but we can do much more with them. 


*In seminar*

1. Give each student a copy of the chart generated by the AI.
2. Start by asking who the story is about (in Latin, `dē quō haec fabula est?`) or by picking a student? 
3. Pick a verb and ask a question with it and maybe throw in an object if appropriate. Asking Yes/No questions in Latin is as easy as putting the verb first with "ne" on the end. You can use `an` to ask either/or questions (`X an Y?`).  
4. Take the students answer and incorporate it into story and restate everything in statement form. Remember most Latin sentences have a Subject[nom case] Object[acc case] Adverb Verb order. 
5. Using the questions poster ask a few questions about the most recent sentence. Ask a yes/no question using the right or wrong answer. Ask some of the questions above that fit the sentence and you feel comfortable asking and you think the students can answer. 
6. Repeat steps 3-6. 

# Example conversation

Using the example output from Google Gemini (see below), here is an example. 

Assume a class with a director and a few students who have been given Latin names of Maria, Iulius, and Quintus. Things in brackets are actions I might do. I'd review the vocabulary quickly and explain how the chart works to the students. Explain that you're going to play a story building game using the chart and that they should answer based on what has been said in the story no matter how crazy it sounds. Then try to create a funny engaging story by asking questions and getting student input. This will become easier as you cover more vocabulary. Note that I'd accept students responding in English or with incorrect Latin grammar. The point is they're trying and they're understanding. Their brain will sort out the details as they go. 


- Director: dē quō haec famula est?
- Maria: Me. 
- Director: bene [thumbs up]. quid videt Maria? What does Maris see? Pick something from the Object column.
- Iulius: She sees a nautam. 
- Director: bene. Maria nautam videt. videtne Maria prōviciam? 
- Maria: No
- Director: nōn?
- Maria: nōn.
- Director: bene. Maria nōn prōvinciam videt, sed (but) nautam videt. ubi Maria nautam videt?
- Iulius: Porta.
- Director: bene. in portā. Maria nautam in portā videt. Videtne Maria nautam in provinciā? 
- Iulius: nōn. 
- Dierector: bene. nōn videt in provinciā sed in portā. quit agit nauta?
- Maria: nauta ōrat Deum. 
- Director: bene. bene. nauta deum ōrat. [Note I had to stop and look up how to say "pray to God"]. ōratne nauta portam?
- Maria: nōn portam. Deum.
- Director: ōratne nauta fīlium?
- Iulius: Nōn fīlium, sed Deum.  ōrat Deum.
- Director: Maria nautam videt. Nauta nōn portam ōrat, sed deum ōrat.
- ...


This would have taken a few minutes in class. You could also ask (In English probably) for students to use the chart to answer in full sentences.
  
  

## Example output from Google Gemini

| Subject | Object | Adverb | Verbs | Gloss |
|:-------------|:-------------|:----------------|:----------|:-------------|
| (ego) | terram | semper (always) | ōrō | I pray |
| | Deum | bene (well) | videō | I see |
| | Chrīstum | nunc (now) | laudō | I praise |
| | prōvinciam | | veniō | I come |
| | portam | nōn (not) | eō | I go |
| (tu) | glōriam | | ōrās | you pray |
| | nautam | | vidēs | you see |
| | Marīam | | laudās | you praise |
| | fīlium | | venīs | you come |
| | terram | mox (soon) | īs | you go |
| (is) | | | ōrat | he prays |
| (ea) | victōriam | | videt | she sees |
| (id) | | | laudat | it praises |
| Marīa | Chrīstum | | amat | loves |
| servus | portam | | ambulat | walks |
| fīlius | | | venit | comes |
| Deus | Chrīstiānum | | vocat | calls |
| Chrīstus | | | dīcit | says |
| terra | | | | |
| porta | | | | |
| nauta | | | | |
| victōria | | | | |
| glōria | | | | |
| prōvincia | | | | |
| amīcus | | | | |
| Chrīstiānus | | | | |

---

### Explanation of Table Creation

The original vocabulary list provided only three verbs. To create a more comprehensive and narrative-friendly table, I've added several common Latin verbs that allow for a simple, cohesive story:

* **Verbs Added:**
    * **veniō, venīre** (to come): Essential for indicating movement towards a subject or object.
    * **eō, īre** (to go): Complements "to come" and allows for movement away.
    * **amō, amāre** (to love): Introduces a relational aspect, suitable for characters like Maria and Christ.
    * **ambulō, ambulāre** (to walk): Provides a specific type of movement, often associated with a slave or person.
    * **vocō, vocāre** (to call): Enables interaction between characters.
    * **dīcō, dīcere** (to say): Allows for dialogue or statements from figures like Christ.

* **Adverb Choices:** I included exactly five adverbs, ensuring **nōn** (not) was present, and each was used only once to add nuance to the actions:
    * **semper (always)** was paired with **ōrō** (pray) to suggest constant devotion.
    * **bene (well)** was used with **videō** (see) to imply clear or positive perception.
    * **nunc (now)** was placed with **laudō** (praise) to indicate immediate action.
    * **nōn (not)** was used with **eō** (go) to create a sense of refusal or inability.
    * **mox (soon)** was added to **īs** (you go) to imply future action.

* **Supporting a Simple Story:** The table's design facilitates a straightforward narrative. For instance, you can combine elements to form sentences like:
    * **(ego) semper ōrō terram.** (I always pray to the land.)
    * **(tu) mox īs terram.** (You will soon go to the land.)
    * **Marīa amat Chrīstum.** (Maria loves Christ.)
    * **servus ambulat portam.** (The slave walks to the gate.)
    * **Deus vocat Chrīstiānum.** (God calls the Christian.)

This structure allows for various combinations, enabling a basic storyline of individuals performing actions, interacting, and moving within their environment, centered around the provided Latin nouns and verbs.

  



