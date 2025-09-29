---
title: "{{#if name}}{{name}}{{else}}Claude Conversation - {{formatDate created_at}}{{/if}}"
created: {{formatDate created_at}}
updated: {{formatDate updated_at}}
conversation_id: "{{uuid}}"
tags:
  - Claude.ai
  - AI-conversation
cssclasses:
  - claude-conversation
---

# {{#if name}}{{name}}{{else}}Claude Conversation - {{formatDate created_at}}{{/if}}

**Conversation ID:** {{uuid}}  
**Created:** {{formatDate created_at}}  
**Updated:** {{formatDate updated_at}}  
**Messages:** {{chat_messages.length}}

---

## Conversation

{{#if chat_messages}}
{{#each chat_messages}}
{{#if (eq this.sender 'human')}}
### 🙋 Human
{{#each this.content}}
{{#if this.text}}
{{this.text}}
{{/if}}
{{/each}}

{{else}}
### 🤖 Claude
{{#each this.content}}
{{#if this.text}}
{{this.text}}
{{/if}}
{{/each}}

{{/if}}
{{#unless @last}}

---

{{/unless}}
{{/each}}
{{else}}
*No messages found in this conversation.*
{{/if}}