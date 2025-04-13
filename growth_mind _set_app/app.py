import streamlit as st
import random
from datetime import date

# Sample challenges and quotes
challenges = [
    "Try something new today that scares you a little.",
    "Spend 15 minutes learning a new skill online.",
    "Reflect on a mistake you made recently and write down what you learned.",
    "Ask someone for feedback today and really listen to it.",
    "Do something today that you’re not good at—yet!",
]

quotes = [
    "“It’s not that I’m so smart, it’s just that I stay with problems longer.” – Albert Einstein",
    "“Mistakes are proof that you are trying.” – Jennifer Lim",
    "“Challenges are what make life interesting.” – Joshua J. Marine",
    "“I can’t do it… yet.” – Carol Dweck",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
]

# App title and intro
st.title("🌱 Growth Mindset Challenge")
st.subheader("Fuel your mind with daily challenges and inspiration.")

# Daily challenge
today = date.today()
random.seed(today.toordinal())  # Ensures the same challenge per day
daily_challenge = random.choice(challenges)
quote_of_the_day = random.choice(quotes)

st.markdown("### 🔥 Today's Challenge")
st.info(daily_challenge)

st.markdown("### 💬 Quote of the Day")
st.success(quote_of_the_day)

# User interaction
completed = st.checkbox("✅ I completed today's challenge!")

if completed:
    st.balloons()
    st.success("Awesome! You're building that growth mindset muscle. 💪")

# Optional journaling
st.markdown("### ✍️ Reflect on Your Progress")
reflection = st.text_area("What did you learn or experience today?", height=150)

if st.button("Save Reflection"):
    with open("reflections.txt", "a") as f:
        f.write(f"{today} - {reflection}\n")
    st.success("Reflection saved!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Embrace the power of *yet*!")

