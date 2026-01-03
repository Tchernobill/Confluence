---
type: translation-workflow
passes: 2
status: active
---

# TRANSLATION WORKFLOW

## PASS 1 — Semantic & Voice Translation

**Goal:** Faithful, raw, voice-accurate draft.

### Prompt (PASS 1)

> You are a professional literary translator.
>
> Translate the following chapter from English to French.
>
> Rules:
> - Follow the Translation Style Sheet exactly.
> - Preserve voice, tone, rhythm.
> - Do not polish or embellish.
> - Do not add explanations.
>
> Output:
> - French text only.
>
> Text:
> ```
> {{chapter_english}}
> ```

---

## PASS 2 — Literary Polish

**Goal:** Native-level French literary prose.

### Prompt (PASS 2)

> You are a French-language novelist and stylist.
>
> Polish the following French translation so it reads as original French fiction.
>
> Rules:
> - Preserve meaning and voice.
> - Improve rhythm and idiomatic flow.
> - Tighten dialogue where needed.
> - Do not add or remove content.
>
> Output:
> - Revised French text only.
>
> Text:
> ```
> {{chapter_pass_1}}
> ```

---

## Optional PASS 3 — Dialogue Pass

Use only for emotionally dense scenes.

> Revise dialogue only for oral realism and register accuracy.
