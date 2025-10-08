import streamlit as st
from groq import Groq
from langdetect import detect
from gtts import gTTS
import base64
import random
import io
import json
from datetime import datetime
import os

# ------------------ CONFIG ------------------
client = Groq(api_key="YOUR_API_KEY_HERE")  # 🔒 Replace with your valid Groq API key
st.set_page_config(page_title="HARSHGPT!! 💕", page_icon="🌸", layout="wide")

# ------------------ ADVANCED CUSTOM CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

body {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.main {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 25px;
    padding: 2rem;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}

/* Animated Typing Header */
.typing-container {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 3rem 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    text-align: center;
}

.typing-text {
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(45deg, #ff6b6b, #ee5a6f, #c44569, #ff6348);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { filter: drop-shadow(0 0 10px rgba(255, 107, 107, 0.5)); }
    to { filter: drop-shadow(0 0 20px rgba(255, 107, 107, 0.8)); }
}

.typing-cursor {
    display: inline-block;
    width: 3px;
    height: 3rem;
    background: #ff6b6b;
    margin-left: 5px;
    animation: blink 0.7s infinite;
    vertical-align: middle;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}

.subtitle {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.2rem;
    margin-top: 1rem;
    font-weight: 300;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

/* Sidebar Styling */
.css-1d391kg, [data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
}

.sidebar .sidebar-content {
    background: transparent;
}

/* Chat Bubbles */
.user-bubble {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 20px 20px 5px 20px;
    padding: 15px 20px;
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    animation: slideInRight 0.3s ease;
    max-width: 80%;
    margin-left: auto;
}

.ai-bubble {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    border-radius: 20px 20px 20px 5px;
    padding: 15px 20px;
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
    animation: slideInLeft 0.3s ease;
    max-width: 80%;
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

/* Form Styling */
.stTextArea > div > div > textarea {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    color: white;
    padding: 15px;
}

.stTextArea > div > div > textarea::placeholder {
    color: rgba(255, 255, 255, 0.6);
}

/* Select Box */
.stSelectbox > div > div {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    color: white;
}

/* Info/Success Boxes */
.stAlert {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    color: white;
}

/* Audio Player */
audio {
    width: 100%;
    border-radius: 25px;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.3));
}

/* Floating Animation */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.floating {
    animation: float 3s ease-in-out infinite;
}

h1, h2, h3 {
    color: white !important;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(245, 87, 108, 0.6);
}
</style>
""", unsafe_allow_html=True)

# ------------------ ANIMATED TYPING HEADER ------------------
st.markdown("""
<div class="typing-container floating">
    <div class="typing-text">
        Welcome to Harsh's Custom GPT
        <span class="typing-cursor"></span>
    </div>
    <div class="subtitle">✨ Your intelligent AI companion for every conversation 💬</div>
</div>
""", unsafe_allow_html=True)

# ------------------ HISTORY SETUP ------------------
HISTORY_FILE = "chat_history.json"
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

all_history = load_history()
today_str = datetime.now().strftime("%Y-%m-%d")
if "current_date" not in st.session_state:
    st.session_state.current_date = today_str

all_dates = sorted(list(set([today_str] + list(all_history.keys()))), reverse=True)
selected_date = st.sidebar.selectbox("📅 Select Chat Date", all_dates)

if selected_date != st.session_state.current_date:
    st.session_state.current_date = selected_date
    st.session_state.chat_history = all_history.get(selected_date, [])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = all_history.get(selected_date, [])

# ------------------ SIDEBAR SETTINGS ------------------
st.sidebar.header("⚙️ Settings")

personality = st.sidebar.selectbox("🎭 Personality", [
    "🎓 Teacher", "🧠 Coder", "🧙 Philosopher", "😄 Friendly Chat"
])
personality_prompts = {
    "🎓 Teacher": "You are a patient teacher who explains things clearly.",
    "🧠 Coder": "You are a skilled coding assistant who gives precise code and explanations.",
    "🧙 Philosopher": "You are a wise philosopher who answers with depth.",
    "😄 Friendly Chat": "You are a cheerful, friendly companion."
}

language_option = st.sidebar.selectbox("🌐 Preferred Language", [
    "Auto Detect", "English", "Hindi", "Telugu"
])
language_codes = {"English": "en", "Hindi": "hi", "Telugu": "te"}
tts_enabled = st.sidebar.checkbox("🔊 Enable Text-to-Speech", value=False)

# ------------------ FUN FACT + WELCOME ------------------
fun_facts = [
    "🌷 Did you know? Smiling actually boosts your mood!",
    "💫 Fun fact: You're amazing just the way you are!",
    "🧁 Tip: Take a deep breath — everything's going to be okay 💖",
    "🌈 Happiness looks good on you!",
    "🍓 Word of the day: 'Lumos' – Let your light shine!"
]
st.success("✨ Hey there! Ready to have an amazing conversation?")
st.info(random.choice(fun_facts))

# ------------------ USER INPUT FORM ------------------
col1, col2 = st.columns([5, 1])
with col1:
    with st.form(key="chat_form", clear_on_submit=True):
        st.text_area("💬 Type your message here...", height=120, key="user_input", placeholder="Ask me anything...")
        submit_button = st.form_submit_button("💌 Send Message")

# ------------------ GPT CHAT ------------------
if submit_button and st.session_state.user_input.strip():
    user_input = st.session_state.user_input.strip()

    if language_option == "Auto Detect":
        detected_lang = detect(user_input)
    else:
        detected_lang = language_codes[language_option]

    system_prompt = f"{personality_prompts[personality]} Reply in {language_option if language_option != 'Auto Detect' else detected_lang} language."

    messages = [{"role": "system", "content": system_prompt}]
    for i in range(0, len(st.session_state.chat_history), 2):
        messages.append({"role": "user", "content": st.session_state.chat_history[i][1]})
        messages.append({"role": "assistant", "content": st.session_state.chat_history[i+1][1]})
    messages.append({"role": "user", "content": user_input})

    with st.spinner("💭 Thinking..."):
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False,
            )
            response = completion.choices[0].message.content
        except Exception as e:
            response = f"❌ Error: {e}"

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("ai", response))

    all_history[st.session_state.current_date] = st.session_state.chat_history
    save_history(all_history)

# ------------------ DISPLAY CHAT ------------------
st.markdown("---")
st.subheader(f"💬 Conversation - {st.session_state.current_date}")

for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='user-bubble'>👤 <b>You:</b><br>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🤖 <b>HARSHGPT:</b><br>{msg}</div>", unsafe_allow_html=True)

        if tts_enabled:
            try:
                tts = gTTS(text=msg, lang=detected_lang if detected_lang in ["en", "hi", "te"] else "en")
                with io.BytesIO() as audio_buffer:
                    tts.write_to_fp(audio_buffer)
                    audio_bytes = audio_buffer.getvalue()
                    b64 = base64.b64encode(audio_bytes).decode()
                    st.markdown(f"""
                        <audio controls>
                            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                        </audio>
                    """, unsafe_allow_html=True)
            except Exception:
                st.warning("⚠️ Could not generate voice output.")

# ------------------ ACTION BUTTONS ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🧾 Summarize Chat"):
        if st.session_state.chat_history:
            combined = "\n".join([f"{r.upper()}: {m}" for r, m in st.session_state.chat_history])
            messages = [
                {"role": "system", "content": "Summarize the following chat briefly:"},
                {"role": "user", "content": combined}
            ]
            with st.spinner("✨ Creating summary..."):
                try:
                    summary = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=messages,
                        max_tokens=500
                    ).choices[0].message.content
                    st.success("📌 Summary:")
                    st.info(summary)
                except Exception as e:
                    st.error(f"❌ Failed to summarize: {e}")
        else:
            st.warning("No chat to summarize yet 🌷")

with col2:
    export_text = "\n".join([f"{r.upper()}: {m}" for r, m in st.session_state.chat_history])
    st.download_button("📥 Download Chat", export_text, file_name=f"chat_{st.session_state.current_date}.txt")
