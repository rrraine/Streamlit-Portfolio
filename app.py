import streamlit as st
import random
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Lorraine's Portfolio",
    page_icon="🐾",
    layout="wide"
)

# --- HEADER ---
st.title("🌸 Lorraine Quezada")
st.subheader("2nd Year Computer Science Student | Cat Lover | Developer of Kainderya 🐱🍽️")
st.write("Welcome to my digital space! I’m a passionate learner exploring the world of technology, creativity, and cats. 🐾")

# --- NAVIGATION TABS ---
tabs = st.tabs(["🏠 Home", "🧍 About Me", "💼 Portfolio", "📊 Extras", "📫 Contact"])

# =====================================================
# 🏠 HOME TAB
# =====================================================
with tabs[0]:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://i.imgur.com/qO0JhA7.png", caption="That's me!", use_container_width=True)

    with col2:
        st.markdown("""
        ### Hello there! 👋  
        I'm **Lorraine**, but you can call me *Raine, Lori, or Riri*.  
        I'm currently a 2nd-year **Computer Science student at Cebu Institute of Technology**.

        I love combining logic and creativity through programming, storytelling, and design.  
        When I’m not coding, you’ll probably find me reading, working on Paws and Pages 🐾📖, or cuddling cats.
        """)

        st.markdown("---")
        st.metric("Years in Tech", 2)
        st.metric("Projects Created", 5)
        st.metric("Programming Languages Learned", 4)

# =====================================================
# 🧍 ABOUT ME TAB
# =====================================================
with tabs[1]:
    st.header("🧠 My Story")

    st.write("""
    I started my journey in computer science out of curiosity — how can computers turn ideas into reality?
    Over time, that curiosity turned into passion. I learned how to code, design user interfaces, and build projects
    that combine both logic and art.
    """)

    st.markdown("### 🌼 Education")
    st.write("- Bachelor of Science in Computer Science — Cebu Institute of Technology (2023–Present)")
    st.write("- Graduated with honors in Senior High School")

    st.markdown("### ✨ Hobbies & Interests")
    st.write("🐱 Taking care of cats")
    st.write("📚 Reading books and manga")
    st.write("💻 Building interactive apps and games")
    st.write("🎮 Playing strategy and rhythm games")

    with st.expander("🌸 Fun Facts About Me"):
        st.write("- I once coded a cat café game for a class project.")
        st.write("- I love naming my variables after cats.")
        st.write("- My dream is to build a real-life Paws and Pages café someday.")

    st.markdown("### 🌈 Life Progress")
    progress = st.slider("How close do you think I am to my goals?", 0, 100, 70)
    st.progress(progress / 100)

# =====================================================
# 💼 PORTFOLIO TAB
# =====================================================
with tabs[2]:
    st.header("💼 My Portfolio")

    project_tabs = st.tabs(["🎮 Kainderya", "🏫 CampusHive", "🐾 Paws and Pages"])

    with project_tabs[0]:
        st.subheader("🎮 Kainderya — A Multiplayer Cooking Game")
        st.image("https://i.imgur.com/1GsfD8I.png", caption="Kainderya Preview", use_container_width=True)
        st.write("""
        A multiplayer cooking game inspired by Filipino eateries (karinderya, tapsilogan, etc.).
        Players must cook and serve orders together, wash plates, and manage time — all in chaos and fun!
        """)

    with project_tabs[1]:
        st.subheader("🏫 CampusHive — University Connection App")
        st.image("https://i.imgur.com/6c8GJ4V.png", caption="CampusHive Interface", use_container_width=True)
        st.write("""
        CampusHive connects students and schools in Cebu. It helps users discover programs, view university details,
        and engage in campus discussions. Built with Java and MySQL.
        """)

    with project_tabs[2]:
        st.subheader("🐾 Paws and Pages — Bookstore & Cat Café Concept")
        st.image("https://i.imgur.com/k6KMUxe.png", caption="Paws and Pages Mockup", use_container_width=True)
        st.write("""
        A hybrid business concept that merges a cozy bookstore, cat café, and study hub for animal lovers.
        Includes fostering, adoptions, and quiet workspaces.
        """)

    st.markdown("---")
    st.header("💡 Skills Overview")

    col1, col2, col3 = st.columns(3)
    col1.progress(0.9)
    col1.write("Python 🐍")

    col2.progress(0.85)
    col2.write("Java ☕")

    col3.progress(0.8)
    col3.write("C++ 💻")

    col1.progress(0.75)
    col1.write("MySQL 🗃️")

    col2.progress(0.7)
    col2.write("HTML/CSS 🌐")

    col3.progress(0.65)
    col3.write("JavaFX 🎨")

# =====================================================
# 📊 EXTRAS TAB
# =====================================================
with tabs[3]:
    st.header("📊 Extras & Fun Features")

    st.subheader("🧩 Quote of the Day")
    quotes = [
        "“Code is like humor. When you have to explain it, it’s bad.” – Cory House",
        "“First, solve the problem. Then, write the code.” – John Johnson",
        "“Talk is cheap. Show me the code.” – Linus Torvalds",
        "“The only way to learn a new programming language is by writing programs in it.” – Dennis Ritchie"
    ]
    st.info(random.choice(quotes))

    st.markdown("### 🐱 Cat Happiness Level")
    happiness = st.slider("How happy are your cats today?", 0, 10, 8)
    st.progress(happiness / 10)
    if happiness >= 8:
        st.success("Your cats are purring with joy! 🐾")
    else:
        st.warning("Give them some extra cuddles today 🧡")

# =====================================================
# 📫 CONTACT TAB
# =====================================================
with tabs[4]:
    st.header("📫 Contact Me")

    st.write("You can reach out through my social links below or send me a quick message! 💬")

    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email:** yourname@email.com")
        st.write("💼 **LinkedIn:** [linkedin.com/in/lorrainequezada](https://linkedin.com)")
        st.write("🐙 **GitHub:** [github.com/lorraineq](https://github.com)")

    with col2:
        with st.form("contact_form"):
            name = st.text_input("Name")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success(f"Thank you, {name}! Your message has been sent. 💌")

    st.markdown("---")
    st.caption("© 2025 Lorraine Quezada | Made with 💖 and Streamlit")

