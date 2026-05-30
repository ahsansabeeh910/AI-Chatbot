import streamlit as st

def sidebar():

    st.sidebar.title("Settings")

    model = st.sidebar.selectbox(

        "Model",

        [

            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash"

        ]
    )

    temperature = st.sidebar.slider(

        "Temperature",

        0.0,

        1.0,

        0.7

    )

    mode = st.sidebar.selectbox(

        "Assistant Mode",

        [

            "Normal",

            "Coding",

            "Study",

            "Career"

        ]
    )

    clear = st.sidebar.button(
        "Clear Chat"
    )

    return model,temperature,mode,clear