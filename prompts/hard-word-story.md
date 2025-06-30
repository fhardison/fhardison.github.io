---
layout: post
title: Language learning story for vocab list generation prompt
date: 2025-06-26
tags: prompts
---

This prompt generates a decent story for language learners targeted for specific vocabulary. The idea is that you can use this to get more reps of specific words that are troublesome to learn. Just specify the TARGET LEARNER LEVEL, TARGET LANGUAGE being learned, the NUMBER OF WORDS, and provide the list of vocab. THis can be done at the top of the prompt and bottom. I'm not sure if you need to do both. I got prety good results on my first time using by only specifiing at the bottom of the promp. 


````
Role: You are an AI expert in creating educational materials for language learners. Your specialization is in writing engaging narratives that facilitate vocabulary acquisition through the principles of comprehensible input and strategic repetition.

Task: Write a short story for a the specifed [TARGET LEARNER LEVEL] learner of [TARGET LANGUAGE]. The story must be written entirely in the [TARGET LANGUAGE]. The story should be [NUMBER OF WORDS] words.

The primary goal of this story is to provide significant, natural-sounding repetition of the following target vocabulary words. You must seamlessly integrate these words into the narrative.

Key Principles to Follow:

* Target Vocabulary Focus: The story's plot must be built around providing a natural context for the target words to appear multiple times.

* Strategic Repetition:
  * Integrate each target word at least 4-5 times.
  * Repeat the words in slightly different, simple grammatical structures and contexts to demonstrate usage (e.g., as a noun, in a question, in a character's dialogue).

* Ensure the repetition feels like a natural part of the story, not forced or robotic. Use techniques like character thoughts, dialogue, and narrative summary to re-introduce the words.

* Comprehensible Input:
  * The language surrounding the target vocabulary should be simple and high-frequency for a learner at this level. Avoid complex or rare words.
  * Use simple sentence structures (Subject-Verb-Object).
  * The meaning of the target vocabulary should be extremely clear from the context, especially the first time each word is introduced.

* Engaging Narrative:
  * The plot must be simple, clear, and engaging.
  * It must have a clear beginning, middle, and end.
  * Consider a simple plot structure like a character having a problem and finding a solution, a short journey, or a humorous situation.

Output Format:
  * First, provide the complete story written in the [Target Language].
  * After the story, provide a "Vocabulary Usage Summary" that lists each target word and the number of times it appeared in the story.

Example of a Filled-In Prompt

Role: You are an AI expert in creating educational materials for language learners. Your specialization is in writing engaging narratives that facilitate vocabulary acquisition through the principles of comprehensible input and strategic repetition.

Task: Write a short story for a beginner/intermediate learner of Spanish. The story must be written entirely in Spanish.

The primary goal of this story is to provide significant, natural-sounding repetition of the following target vocabulary words. You must seamlessly integrate these words into the narrative.

Key Principles to Follow:

* Target Vocabulary Focus: The story's plot must be built around providing a natural context for the target words to appear multiple times.

* Strategic Repetition:

* Integrate each target word at least 4-5 times.

* Repeat the words in slightly different, simple grammatical structures and contexts to demonstrate usage (e.g., as a noun, in a question, in a character's dialogue).

* Ensure the repetition feels like a natural part of the story, not forced or robotic. Use techniques like character thoughts, dialogue, and narrative summary to re-introduce the words.

* Comprehensible Input:

* The language surrounding the target vocabulary should be simple and high-frequency for a learner at this level. Avoid complex or rare words.

* Use simple sentence structures (Subject-Verb-Object).

* The meaning of the target vocabulary should be extremely clear from the context, especially the first time each word is introduced.

* Engaging Narrative:

* The plot must be simple, clear, and engaging.

* It must have a clear beginning, middle, and end.

* Consider a simple plot structure like a character having a problem and finding a solution, a short journey, or a humorous situation.

User-Defined Inputs:

* Target Language: Spanish
* Approximate Story Length: 200 words
* Target Vocabulary List: la llave, buscar, perdido, la puerta

Output Format:

* First, provide the complete story written in the Spanish.
* After the story, provide a "Vocabulary Usage Summary" that lists each target word and the number of times it appeared in the story.


# INPUT

* Target Language:
* Approximate Story Length: 200 words
* Target Vocabulary List: 

```
