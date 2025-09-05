# 🧠 Jarvis – Local Voice-Controlled AI Assistant

**Jarvis** is a voice-activated, conversational AI assistant powered by a local LLM (Qwen via Ollama). It listens for a wake word, processes spoken commands using a local language model with LangChain, and responds out loud via TTS. It supports tool-calling for dynamic functions like checking the current time.

---

## 🚀 Features

- 🗣 Voice-activated with wake word **"Jarvis"**
- 🧠 Local language model (Qwen 3 via Ollama)
- 🔧 Tool-calling with LangChain
- 🔊 Text-to-speech responses via `pyttsx3`
- 🌍 Multiple tools: Time, Screenshots, OCR, Web Search, Network Scan, Matrix Mode
- 🔐 Optional support for OpenAI API integration

---

## ▶️ How It Works (`main.py`)

1. **Startup & local LLM Setup**
   - Initializes a local Ollama model (`qwen3:1.7b`) via `ChatOllama`
   - Registers tools using LangChain

2. **Wake Word Listening**
   - Listens via microphone
   - If it hears the word **"Jarvis"**, it enters "conversation mode"

3. **Voice Command Handling**
   - Records the user's spoken command
   - Passes the command to the LLM, which may invoke tools
   - Responds using `pyttsx3` text-to-speech

4. **Timeout**
   - If the user is inactive for more than 30 seconds in conversation mode, it resets to wait for the wake word again.

---

## 🛠️ Prerequisites

### 1. Install Ollama
First, install Ollama on your system:

**macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Or download from:** https://ollama.ai/download

### 2. Install the Qwen Model
```bash
ollama pull qwen3:1.7b
```

### 3. Install Tesseract (for OCR functionality)
**macOS:**
```bash
brew install tesseract
```

### 4. Optional: Install cmatrix (for Matrix mode)
**macOS:**
```bash
brew install cmatrix
```

---

## 🚀 Installation & Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)
Edit the `.env` file if you want to customize settings:
```bash
# Optional: If you want to use OpenAI instead of local Ollama
# OPENAI_API_KEY=your_openai_api_key_here
# OPENAI_ORG_ID=your_org_id_here

# Microphone settings (optional)
# MIC_INDEX=0

# Wake word (optional - defaults to "jarvis")
# TRIGGER_WORD=jarvis
```

### 3. Test Your Microphone
Make sure your microphone is working and accessible to Python. You might need to grant microphone permissions to your terminal/IDE.

---

## 🎯 Running Jarvis

### Start the Assistant
```bash
python main.py
```

### Usage
1. **Wake Word**: Say "Jarvis" to activate
2. **Commands**: Once activated, speak your commands naturally
3. **Examples**:
   - "What time is it in Tokyo?"
   - "Take a screenshot"
   - "Search for the latest AI news"
   - "Show me devices on my network"
   - "Enter matrix mode"
   - "Read the screen"

---

## 🔧 Available Tools

| Tool | Description | Example Commands |
|------|-------------|------------------|
| **Time** | Get current time in different cities | "What time is it in London?" |
| **Screenshot** | Capture screen to ~/screenshots/ | "Take a screenshot" |
| **OCR** | Read text from screenshots | "Read the screen", "What does the image say?" |
| **Web Search** | DuckDuckGo search | "Search for Python tutorials" |
| **Network Scan** | ARP scan for network devices | "Show devices on my network" |
| **Matrix Mode** | Fun matrix terminal effect | "Enter matrix mode" |

---

## 🔧 Troubleshooting

### Common Issues

1. **Microphone Not Working**
   - Check microphone permissions
   - Try specifying MIC_INDEX in .env file
   - Test with: `python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"`

2. **Ollama Connection Error**
   - Make sure Ollama is running: `ollama serve`
   - Verify model is installed: `ollama list`
   - Pull model if missing: `ollama pull qwen3:1.7b`

3. **TTS Not Working**
   - On macOS, make sure you have system voices installed
   - Try different voice settings in the code

4. **OCR Not Working**
   - Install Tesseract: `brew install tesseract`
   - Take a screenshot first before trying to read it

---

## 🎨 Customization

### Change Wake Word
Edit the `TRIGGER_WORD` variable in `main.py` or set it in `.env`:
```python
TRIGGER_WORD = "computer"  # or "hey jarvis", "assistant", etc.
```

### Add Custom Tools
1. Create a new file in the `tools/` directory
2. Use the `@tool` decorator from LangChain
3. Import and add to the tools list in `main.py`

### Switch to OpenAI
Uncomment the OpenAI lines in `main.py` and add your API key to `.env`

---

## 📁 Project Structure

```
VanGuard-Starter/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
├── README.md              # This file
└── tools/                 # Tool modules
    ├── __init__.py
    ├── time.py            # Time zone tool
    ├── screenshot.py      # Screen capture tool
    ├── ocr.py            # Text extraction tool
    ├── duckduckgo.py     # Web search tool
    ├── arp_scan.py       # Network scanning tool
    └── matrix.py         # Matrix mode effect
```

---

## 🤝 Contributing

Feel free to add more tools or improve existing functionality! Each tool is a separate module in the `tools/` directory.

---

## 📝 License

This project is open source. Feel free to modify and distribute as needed.
