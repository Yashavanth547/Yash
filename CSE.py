import streamlit as st
import time

# 🎉 Title
st.title("📡 Student Scanner System")

# Upload scanner result (simulated as text input)
scanned_text = st.text_input("Scan QR/Barcode here:")

if scanned_text:
    # Animation Effect
    message = f"🎓 Welcome CSE Student {scanned_text}! 🚀"
    wishes = [
        "💻 Code Hard, Dream Big!",
        "✨ Welcome to the World of CSE!",
        "📚 Learn, Build, Achieve!",
        "🚀 Your Future in Tech Starts Here!"
    ]

    # Typing Animation
    placeholder = st.empty()
    for i in range(len(message)+1):
        placeholder.markdown(f"### {message[:i]}")
        time.sleep(0.1)

    # Show wishes one by one
    for wish in wishes:
        st.success(wish)
        time.sleep(1)
      
