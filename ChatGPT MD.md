# ChatGPT MD

🚀 A seamless integration of ChatGPT, OpenRouter.ai and local LLMs via Ollama into Obsidian.

![Chatting with links about vacation plans](https://raw.githubusercontent.com/bramses/chatgpt-md/HEAD/images/chat-with-link.gif)

## What's New in v2.8.0 🚀

### 🆕 GPT-5 Model Support

- **Latest OpenAI Models**: Full support for OpenAI's newest GPT-5 family:
    - `gpt-5` - The flagship model with enhanced reasoning capabilities
    - `gpt-5-mini` - Optimized for speed and efficiency
    - `gpt-5-nano` - Ultra-lightweight for quick responses
    - `gpt-5-chat-latest` - Always-updated chat model
- **Smart Token Management**: Enhanced handling of token limit responses for more reliable interactions
- **Performance Optimizations**: Refined message service architecture and improved API integration

## A simple and quick Start 🏁

Get started in just a few simple steps:

1. **Install ChatGPT MD**: Go to `Settings > Community Plugins > Browse`, search for `ChatGPT MD` and click `Install`.
2. **Add your OpenAI API key**: In the plugin settings, add your OpenAI API key and/or install Ollama and local LLMs of your choice.
3. **Start chatting**: Use the `ChatGPT MD: Chat` command (`cmd + p` or `ctrl + p`) to start a conversation from any note.

💡 _Pro tip_: Set up a hotkey for the best experience! Go to `Settings > Hotkeys`, search for `ChatGPT MD: Chat` and add your preferred keybinding (e.g., `cmd + j`).

Start chatting, don't worry too much about the more advanced features. They will come naturally :-)

## Local LLM Setup (Ollama & LM Studio) 🏠

Want to keep your conversations private and avoid API costs? Use local LLMs with ChatGPT MD!

### Ollama Setup

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/) and install on your system
2. **Download a model**: Run in terminal:
    
    ```bash
    ollama pull llama3.2    # or any model of your choice
    ollama pull qwen2.5     # another popular option
    ```
    
3. **Configure ChatGPT MD**:
    - Go to `Settings > ChatGPT MD > Ollama Defaults`
    - The Ollama URL should already be set to `http://localhost:11434`
    - Set your default model in the settings (e.g., `ollama@llama3.2`)
4. **Start chatting**: Use the `ChatGPT MD: Chat` command to start conversations with your configured default model, or override it in individual notes:
    
    ```yaml
    ---
    model: ollama@llama3.2  # Override default if needed
    temperature: 0.7
    ---
    ```
    

### LM Studio Setup

1. **Install LM Studio**: Download from [lmstudio.ai](https://lmstudio.ai/)
2. **Download and load a model** in LM Studio
3. **Start the server**: In LM Studio, go to Local Server and start it
4. **Configure ChatGPT MD**:
    - Go to `Settings > ChatGPT MD > LM Studio Defaults`
    - The LM Studio URL should be set to `http://localhost:1234`
    - Set your default model in the settings (e.g., `lmstudio@your-model-name`)
5. **Start chatting**: Use the `ChatGPT MD: Chat` command to start conversations with your configured default model, or override it in individual notes:
    
    ```yaml
    ---
    model: lmstudio@your-model-name  # Override default if needed
    temperature: 0.7
    ---
    ```
    

### Finding Your Model Names

- **Ollama**: Run `ollama list` in terminal to see installed models
- **LM Studio**: Check the model name in LM Studio's interface when the model is loaded

### Important Notes for Local LLMs

- **Default Model Configuration**: Set your preferred local model as the default in settings - it works just like cloud services
- **Per-Note Overrides**: You can override the default model in individual notes using frontmatter, same as with other providers
- **Model Discovery**: Use `ollama list` (Ollama) or check LM Studio interface to find your available model names for configuration

## Features

- **Interactive conversations**:
    - Engage directly with ChatGPT, OpenRouter.ai models, and Ollama from any Markdown note, edit questions or responses on-the-fly, and continue the chat seamlessly.
- **Privacy & Zero API Costs:**
    - Use local LLMs via Ollama, keeping your chats on your computer and avoiding API costs.
- **Web Access Models:**
    - Get real-time information from the web with OpenAI's `gpt-4o-search-preview` and Perplexity's `openrouter@perplexity/llama-3.1-sonar-small-128k-online` (via openrouter.ai).
- **Multiple AI Providers:**
    - Choose from OpenAI, OpenRouter.ai (with access to models like Gemini, Claude, DeepSeek, Llama, Perplexity), or local models via Ollama.
- **System Commands:**
    - Instruct the LLM via system commands to get the best possible answers.
- **Link context**:
    - Provide links to any other note in your vault for added context during conversations with Markdown or Wiki links.
- **Per-note Configuration:**
    - Overwrite default settings via frontmatter for individual notes using params from [OpenAI API](https://platform.openai.com/docs/api-reference/chat), [OpenRouter.ai](https://openrouter.ai/docs), or [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion).
- **Markdown Support:**
    - Enjoy full rendering of lists, code blocks, and more from all responses.
- **Minimal Setup:**
    - Utilize your OpenAI API key, OpenRouter.ai API key, or install any LLM locally via Ollama.
- **Comment Blocks:**
    - Ignore parts of your notes using comment blocks.
- **Chat Templates**:
    - Use and share frontmatter templates for recurring scenarios. Explore [chatgpt-md-templates](https://github.com/bramses/chatgpt-md-templates).

## Privacy and Security

ChatGPT MD is

- only storing data locally in your vault, with zero tracking and no 3rd party integrations except direct calls to the AI APIs (OpenAI, OpenRouter.ai).
- allowing you to use Ollama, a local LLM installation for offline conversation-based knowledge exploration.

### Default Configuration

The plugin comes with a well-balanced pre-configuration to get you started immediately.  
You can change the global settings or use the local parameters in any note via frontmatter  
(start typing `---` in the first line of your note to add properties)

```
---
system_commands: ['You are a helpful assistant.']
temperature: 0.3
top_p: 1
max_tokens: 300
presence_penalty: 0.5
frequency_penalty: 0.5
stream: true
stop: null
n: 1
model: gpt-5-mini

# Service-specific URLs (optional, will use global settings if not specified)
openaiUrl: https://api.openai.com
# openrouterUrl: https://openrouter.ai
# ollamaUrl: http://localhost:11434
---
```

💡 Pro tip: Increasing `max_tokens` to a higher value e.g. `4096` for more complex tasks like reasoning, coding or text creation.  
The default model `gpt-5-mini` is optimized for speed and efficiency. Upgrade to `gpt-5` for enhanced reasoning capabilities or use `gpt-5-nano` for ultra-lightweight responses.

### Multi Model Chats

You can set and change the model for each request in your note.  
Specify the `model` property via frontmatter:

for OpenAI models (including the latest GPT-5 family)

```
---
model: gpt-5  # or gpt-5-mini, gpt-5-nano, gpt-5-chat-latest
system_commands: [act as a senior javascript developer]
---
```

prefix it with `ollama@` for Ollama models or `lmstudio@` for LM Studio models.

```
---
model: ollama@gemma2:27b
temperature: 1
---
```

The AI responses will keep the used model name in the response title for future reference.  
You can find the list of your installed Ollama model names from your terminal via `ollama list` or the available openAI model names online on this [openAI models](https://platform.openai.com/docs/models) page.

### Service URLs

Each AI service has its own dedicated URL parameter that can be configured globally in settings or per-note via frontmatter:

```
---
# For OpenAI
openaiUrl: https://api.openai.com

# For OpenRouter
openrouterUrl: https://openrouter.ai

# For Ollama
ollamaUrl: http://localhost:11434
---
```

The default URLs are:

- OpenAI: `https://api.openai.com`
- OpenRouter: `https://openrouter.ai`
- Ollama: `http://localhost:11434`

Note: Previous versions used a single `url` parameter which is now deprecated. Please update your templates and notes to use the service-specific URL parameters.

### Commands 👨‍💻

Run commands from Obsidian's command pallet via `cmd + p` or `ctrl + p` and start typing `chatgpt` or set hotkeys  
(a chat command hotkey is highly recommended for effortless chats (I use `cmd + j`, which works fantastic, because your index finger is already resting on that key)).

#### Main Command

- **Chat**: Parse the file and interact with ChatGPT. Assign a hotkey, e.g. `cmd + j`.

#### Creation Commands

- **New Chat with Highlighted Text**: Start a chat using highlighted text and default frontmatter in `Chat Folder`.
- **New Chat From Template**: Create chats from templates in `Chat Template Folder`.

#### Utility Commands

- **Infer Title**: Automatically generate a note title based on the notes content. Configurable to auto-run after 4+ messages.
- **Add Comment Block**: Insert comment blocks for parts of your note that should be ignored.
- **Select Model**: Choose from all available LLMs (OpenAI, OpenRouter.ai, Ollama) and set the current model for your note.

#### Maintenance Commands

- **Clear Chat**: Remove all messages while retaining frontmatter.
- **Stop Streaming (Desktop Only)**: Halt ongoing streams if necessary.

#### Formatting Tools

- **Add Divider**: Insert horizontal rulers to organize content visually.

## Beta Testing 🧪

Want to try the latest features before they're officially released? You can beta test ChatGPT MD using the [BRAT (Beta Reviewer's Auto-update Tool)](https://github.com/TfTHacker/obsidian42-brat) community plugin:

1. Install the BRAT plugin from Obsidian's Community Plugins
2. Open BRAT settings and add `bramses/chatgpt-md` as a beta plugin
3. Select "latest version" from the dropdown in the BRAT plugin settings
4. Enable the ChatGPT MD plugin in your community plugins list

This gives you early access to new features while they're still being developed and tested.

⚠️ **WARNING**: Beta testing is dangerous and happens at your own risk. Always test beta versions on a new empty vault, not on your main vault. Beta features can break and possibly lead to data loss.

## FAQs ❓

#### How do I start chatting with ChatGPT MD?

Use the `ChatGPT MD: Chat` command from the Obsidian command Palette (`cmd + p` or `ctrl + p`) to start a conversation from any note.

#### Can I set up a hotkey for the `ChatGPT MD: Chat` command?

Yes, you should! Go to `Settings > Hotkeys`, search for `ChatGPT MD: Chat` and add your preferred keybinding (e.g., `cmd + j`).

#### How do I use chat and reasoning models?

You can use OpenAI's GPT 3 and 4 models, various models through OpenRouter.ai (like Claude, Gemini, DeepSeek, Llama, Perplexity), or any model you have installed via Ollama.  
DeepSeek-r1:7b works great for reasoning locally via Ollama.

#### How do I use a custom endpoint?

Ensure your custom API adheres to OpenAI's specifications, such as Azure's hosted endpoints. Consult your provider for API key management details.

#### Where should I add my OpenAI API key?

In the plugin settings, add your OpenAI API key and/or install Ollama and local LLMs of your choice.

#### What happened to the 'url' parameter in the frontmatter?

The single 'url' parameter is now deprecated. In v2.2.0 and higher, we've introduced service-specific URL parameters: `openaiUrl`, `openrouterUrl`, and `ollamaUrl`. This allows for more flexibility and clarity when configuring different services. Please update your templates and notes accordingly.

🤖 Enjoy exploring the power of ChatGPT MD in your Obsidian vault!🚀

## Contributions Welcome 🤝

Pull requests, bug reports, and all other forms of contribution are welcomed and highly encouraged!* :octocat:

## About the Developers ✍️

Bram created ChatGPT MD in March 2023 lives in NYC and is building [Your Commonbase](https://bramses.notion.site/Your-Commonbase-ALPHA-10b034182ddd8038b9ffe11cc2833713) (A Self Organizing Scrapbook with Zero Stress Storing, Searching, and Sharing). His personal website and newsletter is located at [bramadams.dev](https://www.bramadams.dev/)

Deniz joined Bram in 2024 to continue development. He is working in a gaming company in Germany and uses AI heavily in his work and private life. Say "hi" on Bluesky: [Deniz](https://bsky.app/profile/denizokcu.bsky.social)

Happy writing with ChatGPT MD! 💻 🎉