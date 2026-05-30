import streamlit as st
from datetime import datetime
import json

from components.sidebar import sidebar
from utils.gemini_helper import ask_gemini
from utils.memory import load_chat, save_chat
from utils.file_handler import read_file
from utils.speech import text_to_audio

st.set_page_config(

    page_title="AI Assistant",

    page_icon="🤖"

)

model,temp,mode,clear = sidebar()

if "messages" not in st.session_state:

    st.session_state.messages = load_chat()

if clear:

    st.session_state.messages = []

uploaded = st.file_uploader(

    "Upload PDF / TXT",

    [

        "pdf",

        "txt"

    ]
)

context = ""

if uploaded:

    context = read_file(
        uploaded
    )

for msg in st.session_state.messages:

    with st.chat_message(

        msg["role"]

    ):

        st.markdown(
            msg["content"]
        )

        if "time" in msg:

            st.caption(
                msg["time"]
            )

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    current_time = datetime.now().strftime("%H:%M")

    st.session_state.messages.append(

        {

            "role":"user",

            "content":prompt,

            "time":current_time

        }

    )

    history = ""

    for m in st.session_state.messages:

        history += f"{m['role']} : {m['content']}\n"

    final_prompt = f"""

Mode: {mode}

Context:

{context[:5000]}

Conversation:

{history}

User:

{prompt}

"""

    with st.spinner(

        "Thinking..."

    ):

        reply = ask_gemini(

            model,

            final_prompt

        )

    st.session_state.messages.append(

        {

            "role":"assistant",

            "content":reply,

            "time":datetime.now().strftime("%H:%M")

        }

    )

    save_chat(
        st.session_state.messages
    )

    with st.chat_message(

        "assistant"

    ):

        st.markdown(
            reply
        )

    audio = text_to_audio(
        reply
    )

    st.audio(
        audio
    )

chat_data = json.dumps(

    st.session_state.messages,

    indent=4

)

st.sidebar.download_button(

    "Download Chat",

    chat_data,

    file_name="chat_history.json"

)