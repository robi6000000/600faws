import streamlit as st

st.set_page_config(page_title="Test App")

st.title("Streamlit Placeholder App")
st.write("This is a test app to see if Streamlit is running on the cloud.")

# Simple input to test interaction
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Your Streamlit app is running.")

# File uploader to check cloud interaction
uploaded_file = st.file_uploader("Upload a file to test", type=["txt", "png", "jpg"])
if uploaded_file:
    st.write(f"Uploaded file: {uploaded_file.name}")
    if uploaded_file.type.startswith("image/"):
        from PIL import Image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded image", use_container_width=True)

# Optional: display GitHub repo info if you connect a token/env variable
import os
gh_user = os.getenv("GITHUB_USER")
gh_repo = os.getenv("GITHUB_REPO")
if gh_user and gh_repo:
    st.info(f"Connected GitHub account: {gh_user}, Repo: {gh_repo}")
else:
    st.info("No GitHub environment variables set. Only testing Streamlit runtime.")
