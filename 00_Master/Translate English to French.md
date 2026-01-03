## 🧠 Core Translation Prompt (Literary / Chapter-Level)

**Task:** 

Act as a **professional literary translator specializing in fiction**.  
Translate with attention to **voice equivalence**, not sentence equivalence.  
When necessary, restructure sentences to preserve **emotional impact and pacing** in French.

**Requirements:**

- Preserve the **author’s voice, tone, and rhythm**.
- Maintain **natural, idiomatic French** rather than literal translation.
- Respect **narrative perspective**, **tense**, and **stylistic quirks** (sentence length, fragments, internal monologue).
- Keep **dialogue authentic and spoken**, with appropriate register.
- Do **not simplify** or sanitize emotionally charged language.
- Preserve **subtext, metaphor, and symbolic meaning**.
- Keep names, invented terms, and world-specific vocabulary unchanged unless clearly translatable.
- Ensure **consistency** with previous chapters if applicable.
- Use **international French with a subtle Québécois sensibility**.
- Avoid heavy joual unless explicitly present in dialogue.
- Allow light Québécois turns of phrase **only in spoken dialogue**, not in narration.
- Keep the prose elegant and readable for a broad Francophone audience.

**Genre Constraints:**

- Respect **cyberpunk / speculative fiction tone**.
- Preserve technical terms, slang, and invented jargon.
- Avoid over-formalization of futuristic dialogue.    
- Maintain the sense of **grit, immediacy, and embodied perception**.

**Continuity Rules:**

- Maintain consistent translation choices for recurring terms, metaphors, and character voices.
- If a term has no perfect equivalent, choose one translation and reuse it consistently.
- Flag (silently, without notes) rhythm or tone shifts only if required by context.

**Output:**

- Provide **only the translated French text**, formatted as a novel chapter.
- Do not include explanations or commentary.

---


# TWO-PASS TRANSLATION WORKFLOW

This is where quality jumps.

## PASS 1 — _Semantic & Voice-Accurate Translation_

### Prompt: PASS 1

**Role:**  
You are a **professional literary translator**.

**Task:**  
Translate the following chapter from **English to French**.

**Rules:**

- Follow the **Translation Style Sheet** exactly.
- Prioritize **voice equivalence and emotional accuracy** over literal wording.
- Preserve sentence rhythm, fragments, and pacing.
- Do not polish, embellish, or improve style yet.
- Do not add explanations or notes.

**Output:**

- Provide the **full translated chapter in French only**. 

**Goal:**  
A faithful, voice-accurate, slightly raw draft.

---

## PASS 2 — _Literary Polish & French Naturalization_

### Prompt: PASS 2

**Role:**  
You are a **French-language novelist and stylist**.

**Task:**  
Polish the following French translation to read as **original French literary fiction**.

**Rules:**

- Preserve **meaning, tone, and character voice** exactly.
- Improve flow, rhythm, and idiomatic naturalness.
- Tighten dialogue where needed.
- Enhance readability **without altering intent**.
- Do not add content.
- Do not remove emotional roughness.

**Checks:**

- Sentence music
- Dialogue realism
- POV integrity
- Emotional pacing

**Output:**

- Provide only the **revised French chapter**.

**Goal:**  
Make it indistinguishable from a native French novel.

