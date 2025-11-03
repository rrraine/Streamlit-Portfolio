import streamlit as st
import random
import os
import yagmail 
import time
from datetime import date
from streamlit_drawable_canvas import st_canvas


# PAGE CONFIG 
st.set_page_config(
    page_title="Lorraine's Portfolio",
    page_icon="🐾",
    layout="wide"
)

#  HEADER 
st.title("🌸 Lorraine Quezada")
st.subheader("3rd Year Computer Science Student")
st.write("Welcome to my digital space! I’m a passionate learner exploring the world of technology, creativity, and cats. 🐾")

#  NAVIGATION TABS 
tabs = st.tabs(["🏠 Home", "🧍 About Me", "💼 Portfolio", "📊 Extras", "📫 Contact"])


with tabs[0]:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/lorraine_photo.png", caption="That's me!", use_container_width=True)

    with col2:
        st.markdown("""
        ### Hello there! 👋  
        I'm **Lorraine**, but you can call me *Raine, Lori, or Riri*.  
        I'm currently a 3rd year **Computer Science student at Cebu Institute of Technology**.

        I love combining logic and creativity through programming, storytelling, and design.  
        When I’m not coding, you’ll probably find me reading and taking care of my dogs.
        """)

        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Years in Tech", 3)

        with col2:
            st.metric("Projects Created", 5)

        with col3:
            st.metric("Programming Languages Learned", 4)

with tabs[1]:
    st.header("🧠 My Story")

    st.write("""
    I started my journey in computer science out of curiosity — how can computers turn ideas into reality?
    Over time, that curiosity turned into passion. I learned how to code, design user interfaces, and build projects
    that combine both logic and art.
    """)

    st.markdown("### 🌼 Education")
    st.write("- Bachelor of Science in Computer Science — Cebu Institute of Technology (2023–Present)")
    st.write("- Graduated with high honors in Senior High School")

    st.markdown("### ✨ Hobbies & Interests")
    st.write("🐱 Taking care of my 2 dogs (3 but the eldest, Lucky, passed away) ")
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


with tabs[2]:
    st.header("My Portfolio")

    # Tabs for different projects
    project_tabs = st.tabs([
        "🎮 Kainderya",
        "👮🏼 Inmate Escape",
        "🏫 CampusHive",
        "📄 My Work Portfolio"
    ])

  
    with project_tabs[0]:
        st.subheader("🎮 Kainderya — A Multiplayer Cooking Game")
        st.image("images/kainderya.jpg", caption="Kainderya Preview", use_container_width=True)
        st.write("""
         **Kainderya** is a cooperative multiplayer cooking game set in a lively Filipino eatery.  
        Players work together to cook, serve, and clean up orders under time pressure — promoting teamwork and quick thinking.  
        Inspired by everyday karinderya life, it brings local culture into a fun, chaotic kitchen challenge.
        """)

    with project_tabs[1]:
        st.subheader("Inmate Escape — Endless Runner Game")
        st.image("images/inmateescape.jpg", caption="Inmate Escape Preview", use_container_width=True)
        st.write("""
        **Inmate Escape** is an endless runner game where players take on the role of an escaped inmate fleeing from the police.  
        The speed increases as the game progresses, challenging players to dodge obstacles and survive as long as possible.  
        The game combines adrenaline-pumping action with smooth, fast-paced gameplay inspired by *Subway Surfers*.
        """)

    with project_tabs[2]:
        st.subheader("🏫 CampusHive — University Connection App")
        st.image("images/campushive.png", caption="CampusHive Interface", use_container_width=True)
        st.write("""
        **CampusHive** is an all-in-one mobile platform that connects students and universities across Cebu.  
        Users can explore schools, view programs, and join campus discussions.  
        Developed with **Java (Android)** and **MySQL**, it enhances student engagement through digital community building.
        """)


   

    with project_tabs[3]:
        st.subheader("📄 My Work Portfolio as a Virtual Assistant")

        with open("files/Lorraine_Quezada_Portfolio.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label="💾 Download Full PDF",
            data=PDFbyte,
            file_name="Lorraine_Quezada_Portfolio.pdf",
            mime="application/pdf"
        )


    # # collapsible preview but so lag due to pdf size
    #     with st.expander("👀 Preview My Portfolio (click to open)"):
    #         import base64
    #         base64_pdf = base64.b64encode(PDFbyte).decode("utf-8")
    #         pdf_display = f"""
    #         <iframe
    #             src="data:application/pdf;base64,{base64_pdf}"
    #             width="100%"
    #             height="600px"
    #             type="application/pdf"
    #             style="border: none;"
    #         ></iframe>
    #         """
    #         st.markdown(pdf_display, unsafe_allow_html=True)


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


# extras
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

    st.markdown("### 🐱 Cat/Dog Happiness Level")
    happiness = st.slider("How happy are your cats/dogs today?", 0, 10, 8)
    st.progress(happiness / 10)
    if happiness >= 8:
        st.success("Your cats/dogs are purring/wagging with joy! 🐾")
    else:
        st.warning("Give them some extra cuddles today 🧡")

      
    with st.container():
        st.header("🧠 Memory Match Mini Game")
        st.write("Double click the cards to flip.")

        # Initialize session state
        if "cards" not in st.session_state:
            emojis = ["🐱", "🐶", "🐰", "🐹", "🐸", "🐼"]
            st.session_state.cards = random.sample(emojis * 2, len(emojis) * 2)
            st.session_state.flipped = []
            st.session_state.matched = []
            st.session_state.attempts = 0
            st.session_state.start_time = time.time()

        # Grid display (3x4)
        cols = st.columns(4)
        for i, emoji in enumerate(st.session_state.cards):
            with cols[i % 4]:
                if i in st.session_state.flipped or i in st.session_state.matched:
                    st.button(emoji, key=f"card_{i}", disabled=True)
                else:
                    if st.button("❓", key=f"card_{i}"):
                        st.session_state.flipped.append(i)

        # Check match logic
        if len(st.session_state.flipped) == 2:
            a, b = st.session_state.flipped
            st.session_state.attempts += 1
            if st.session_state.cards[a] == st.session_state.cards[b]:
                st.session_state.matched.extend([a, b])
                st.toast("✨ Match found!", icon="🎉")
            else:
                st.toast("❌ Not a match, try again!", icon="😅")
            time.sleep(0.7)
            st.session_state.flipped = []

      
        # Win condition
        if len(st.session_state.matched) == len(st.session_state.cards):
            st.balloons()
            elapsed = round(time.time() - st.session_state.start_time, 1)
            st.success(f"🏁 You matched all pairs in {st.session_state.attempts} attempts and {elapsed} seconds!")

        # Display stats
        st.markdown("---")
        cols = st.columns([1, 1, 1, 1])  # Adjust width ratio if needed
        cols[0].metric("Attempts", st.session_state.attempts)
        cols[1].metric("Matches Found", len(st.session_state.matched) // 2)
        if cols[2].button("🔄 Restart Game"):
            emojis = ["🐱", "🐶", "🐰", "🐹", "🐸", "🐼"]
            st.session_state.cards = random.sample(emojis * 2, len(emojis) * 2)
            st.session_state.flipped = []
            st.session_state.matched = []
            st.session_state.attempts = 0
            st.session_state.start_time = time.time()

#contact me
with tabs[4]:
    st.header("📫 Contact Me")

    st.write("You can reach out through my social links below or send me a quick message! 💬")

    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email:** lorraineequezada@gmail.com")
        st.write("💼 **LinkedIn:** [linkedin.com/in/lorrainequezada](https://www.linkedin.com/in/lorraine-quezada-377459329/)")
        st.write("🐙 **GitHub:** [github.com/rrraine](https://github.com/rrraine)")

    with col2:
 
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            sender_email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and sender_email and message:
                    try:
                   
                        yag = yagmail.SMTP("lorraineequezada@gmail.com", "sazh cokd qxlf rtbr")

                     
                        subject = f"📬 New message from {name}"

                    
                        body = f"""
                        <h3>New message received from your Streamlit Portfolio 💌</h3>
                        <p><b>From:</b> {name} &lt;{sender_email}&gt;</p>
                        <p><b>Message:</b></p>
                        <blockquote style="border-left: 3px solid #ddd; padding-left: 10px;">
                        {message.replace('\n', '<br>')}
                        </blockquote>
                        <hr>
                        <p style="font-size: 12px; color: #888;">This message was sent via your Streamlit contact form.</p>
                        """

                        # Send the email
                        yag.send(
                            to="lorraineequezada@gmail.com",
                            subject=subject,
                            contents=body
                        )

                        st.success("Thank you! Your message has been sent successfully 💌")

                    except Exception as e:
                        st.error(f"❌ Oops! Something went wrong: {e}")
                else:
                    st.warning("Please fill out all fields before sending.")
 

