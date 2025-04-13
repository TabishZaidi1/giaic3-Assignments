import streamlit as st

def main():
    st.title("🌱 Growth Mindset Challenge")
    st.write("Believe in your ability to grow and improve!")
    
    # Section 1: Introduction
    st.header("What is a Growth Mindset?")
    st.write(
        "A growth mindset is the belief that your abilities and intelligence "
        "can develop through hard work, perseverance, and learning from mistakes."
    )
    
    # Section 2: Why Adopt a Growth Mindset?
    st.header("Why Adopt a Growth Mindset?")
    reasons = [
        "🌟 Embrace Challenges: See obstacles as learning opportunities.",
        "💡 Learn from Mistakes: Errors help you improve.",
        "🔥 Persist Through Difficulties: Hard work leads to growth.",
        "🎉 Celebrate Effort: Focus on learning, not just results.",
        "🔄 Keep an Open Mind: Stay curious and adapt."
    ]
    for reason in reasons:
        st.write(reason)
    
    # Section 3: Interactive Challenge
    st.header("Your Growth Mindset Challenge")
    challenge = st.selectbox("Pick a challenge to work on today:", [
        "Try something new and reflect on what you learned",
        "Work on a difficult task without giving up",
        "Turn a mistake into a learning opportunity",
        "Help someone else develop a growth mindset"
    ])
    st.write(f"Great choice! Stay committed to '{challenge}' today.")
    
    # Section 4: Reflection
    st.header("Reflect on Your Learning")
    user_input = st.text_area("What is one key lesson you've learned recently?")
    if st.button("Submit Reflection"):
        st.success("Thank you for sharing! Keep growing. 🌱")
    
    # Section 5: Motivational Quote
    st.header("Today's Inspiration")
    st.write("🚀 *" + "Your potential is endless. Keep pushing forward!" + "*")

if __name__ == "__main__":
    main()
