# 🌸 HARSHGPT!! 💕

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Groq](https://img.shields.io/badge/Groq-API-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Your intelligent AI companion for every conversation ✨**

[Live Demo](https://harshgpt.streamlit.app/) | [Report Bug](https://github.com/yourusername/harshgpt/issues) | [Request Feature](https://github.com/yourusername/harshgpt/issues)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png" alt="Robot" width="100" height="100" />

</div>

---

## 🎯 About The Project

**HARSHGPT** is a beautiful, feature-rich AI chatbot application built with Streamlit and powered by Groq's LLaMA 3.3 70B model. Experience intelligent conversations with a stunning, modern UI that includes glassmorphism effects, smooth animations, and an aesthetic design that makes every interaction delightful.

### ✨ Key Highlights

- 🎨 **Modern Glassmorphism UI** - Beautiful frosted glass effects with animated gradients
- 🤖 **Powered by LLaMA 3.3 70B** - Advanced AI responses through Groq API
- 🌍 **Multi-language Support** - English, Hindi, Telugu with auto-detection
- 🎭 **Multiple Personalities** - Teacher, Coder, Philosopher, Friendly Chat
- 🔊 **Text-to-Speech** - Listen to AI responses in your preferred language
- 💾 **Chat History** - Save and retrieve conversations by date
- 📊 **Smart Summarization** - Get quick summaries of long conversations
- 📥 **Export Conversations** - Download your chats as text files
- ✨ **Animated Typing Effect** - Eye-catching welcome header with typing animation

---

## 🚀 Features

### 🎨 Visual Experience
- **Animated Gradient Background** - Smooth color-shifting animation
- **Typing Animation Header** - "Welcome to Harsh's Custom GPT" with blinking cursor
- **Floating Effects** - Gentle animations throughout the interface
- **Glassmorphism Design** - Modern frosted glass aesthetic
- **Smooth Chat Bubbles** - Slide-in animations with gradient backgrounds

### 🧠 AI Capabilities
- **Context-Aware Conversations** - Maintains chat history for coherent dialogues
- **Personality Modes** - Choose from 4 different AI personalities
- **Language Detection** - Automatically detects and responds in your language
- **Smart Responses** - Powered by LLaMA 3.3 70B for accurate answers

### 💾 Data Management
- **Date-wise History** - Organize conversations by date
- **Persistent Storage** - Never lose your conversations
- **Quick Summaries** - AI-generated chat summaries
- **Export Functionality** - Download conversations as TXT files

### 🔊 Audio Features
- **Text-to-Speech** - Listen to AI responses
- **Multi-language TTS** - Support for English, Hindi, and Telugu
- **In-browser Audio Player** - No external apps needed

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web framework for the UI |
| **Groq API** | AI model inference (LLaMA 3.3 70B) |
| **gTTS** | Text-to-speech conversion |
| **LangDetect** | Language detection |
| **Python 3.8+** | Core programming language |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get it here](https://console.groq.com/))

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/harshgpt.git
cd harshgpt
```

2. **Install dependencies**
```bash
pip install streamlit groq langdetect gtts
```

3. **Configure API Key**

Open the Python file and replace:
```python
client = Groq(api_key="YOUR_API_KEY_HERE")
```

With your actual Groq API key:
```python
client = Groq(api_key="your-actual-api-key")
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**

Navigate to `http://localhost:8501`

---

## 🎮 Usage

### Starting a Conversation

1. **Select Settings** (Sidebar)
   - Choose AI personality (Teacher/Coder/Philosopher/Friendly)
   - Select preferred language
   - Enable/disable Text-to-Speech

2. **Type Your Message**
   - Enter your question or message in the text area
   - Click "💌 Send Message"

3. **View Response**
   - See the AI's response in a beautiful chat bubble
   - Listen to audio (if TTS enabled)

### Managing Conversations

- **Switch Dates**: Use the date selector in the sidebar to view past conversations
- **Summarize Chat**: Click "🧾 Summarize Chat" for a quick summary
- **Download Chat**: Export your conversation as a text file

---

## 🎭 Personality Modes

| Mode | Description | Best For |
|------|-------------|----------|
| 🎓 **Teacher** | Patient and clear explanations | Learning new concepts |
| 🧠 **Coder** | Precise code and technical details | Programming help |
| 🧙 **Philosopher** | Deep, thoughtful responses | Philosophical discussions |
| 😄 **Friendly Chat** | Cheerful and casual | Casual conversations |

---

## 🌍 Supported Languages

- 🇬🇧 **English**
- 🇮🇳 **Hindi** (हिंदी)
- 🇮🇳 **Telugu** (తెలుగు)
- 🔍 **Auto-Detect** - Automatically identifies and responds in your language

---

## 📸 Screenshots

<div align="center">

### Main Interface
*Beautiful glassmorphism design with animated typing header*

### Chat Interface
*Smooth gradient chat bubbles with slide-in animations*

### Settings Panel
*Easy-to-use sidebar with all customization options*

</div>

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**Harsh** - Creator & Developer

Project Link: [https://harshgpt.streamlit.app/](https://harshgpt.streamlit.app/)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing web framework
- [Groq](https://groq.com/) - Lightning-fast AI inference
- [LLaMA 3.3](https://ai.meta.com/llama/) - Powerful language model
- [gTTS](https://github.com/pndurette/gTTS) - Text-to-speech library
- All the amazing open-source contributors!

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

Made with ❤️ by Harsh

</div>
