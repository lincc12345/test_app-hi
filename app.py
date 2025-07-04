import streamlit as st
st.title("helllo how are you")
import streamlit as st

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
    import streamlit as st

import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

import streamlit as st

st.badge("NO")
st.badge("NO", icon=":material/check:", color="red")

st.markdown(
    ":violet-badge[:material/star: NO] :orange-badge[⚠️ NOO] :gray-badge[NO]"
)