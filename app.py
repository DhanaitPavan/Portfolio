"""
Pavan Dhanait — Personal Portfolio (Streamlit)
Run locally:   pip install -r requirements.txt && streamlit run app.py
Deploy free:   https://share.streamlit.io (push this folder to GitHub, then deploy)
"""

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Pavan Dhanait | Data Scientist & ML Engineer",
    page_icon="🎥🧑‍🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
EMAIL = "pavandh9766@gmail.com"
PHONE = "+91 84828 87936"
GITHUB = "https://github.com/DhanaitPavan"
LINKEDIN = "https://www.linkedin.com/in/pavan-dhanait?utm_source=share_via&utm_content=profile&utm_medium=member_android"
CERT_URL = "https://www.coursera.org/account/accomplishments/professional-cert/3KCGSW0P3D7D"

ACCENT = "#d97706"      # deeper amber for light backgrounds
ACCENT2 = "#0891b2"     # deeper cyan for light backgrounds
INK = "#0b1220"

# ---------------------------------------------------------------------------
# Styling (Light Theme Adapted)
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;500;600;800&display=swap');

      html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
      .block-container {{ max-width: 1150px; padding-top: 1.5rem; padding-bottom: 4rem; }}

      h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif; letter-spacing: -0.02em; }}

      /* Hero */
      .hero {{
          background:
            radial-gradient(900px 420px at 85% -10%, rgba(251,191,36,0.18), transparent 60%),
            radial-gradient(700px 380px at 5% 110%, rgba(34,211,238,0.12), transparent 60%),
            linear-gradient(135deg, #fffbeb 0%, #ffffff 60%, #fef3c7 100%);
          border: 1px solid rgba(251,191,36,0.3);
          border-radius: 20px;
          padding: 3.2rem 3rem 2.6rem;
          color: #1f2937;
          margin-bottom: 2.2rem;
          box-shadow: 0 4px 20px -4px rgba(0,0,0,0.05);
      }}
      .hero h1 {{
          font-size: 3.2rem; line-height: 1.05; margin: 0.4rem 0 1rem;
          color: #111827;
      }}
      .hero h1 span {{ color: {ACCENT}; }}
      .hero p {{ color: #4b5563; font-size: 1.08rem; max-width: 640px; }}

      .eyebrow {{
          font-size: 0.72rem; font-weight: 700; letter-spacing: 0.22em;
          text-transform: uppercase; color: {ACCENT}; margin-bottom: 0.3rem;
      }}
      .eyebrow-dark {{ color: #b45309; }}
      .muted {{ color: #4b5563; }}

      /* Chips */
      .chip {{
          display: inline-block; border: 1px solid #d1d5db; border-radius: 999px;
          padding: 3px 14px; margin: 3px 5px 3px 0; font-size: 0.8rem;
          background: #ffffff; color: #374151; transition: all .18s ease;
      }}
      .chip:hover {{ border-color: {ACCENT}; background: #fffbeb; transform: translateY(-1px); }}

      /* Stat cards */
      .stat-card {{
          border: 1px solid #e5e7eb; border-radius: 16px; padding: 1.3rem 1.4rem;
          background: linear-gradient(180deg, #ffffff, #fafaf7);
          box-shadow: 0 1px 3px rgba(16,24,40,0.08);
          transition: all .2s ease;
      }}
      .stat-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 28px -12px rgba(180,83,9,0.25); border-color: {ACCENT}; }}
      .stat-num {{
          font-family: 'Space Grotesk', sans-serif; font-size: 2.4rem;
          font-weight: 700; color: {INK}; line-height: 1;
      }}
      .stat-num em {{ color: #b45309; font-style: normal; }}
      .stat-label {{ color: #4b5563; font-size: 0.85rem; margin-top: 0.35rem; }}

      /* Project cards */
      .proj {{
          border: 1px solid #e5e7eb; border-radius: 18px; overflow: hidden;
          background: #ffffff; height: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: all .22s ease;
      }}
      .proj:hover {{ transform: translateY(-5px); box-shadow: 0 18px 40px -18px rgba(16,24,40,0.15); }}
      .proj-band {{
          height: 10px;
          background: linear-gradient(90deg, {ACCENT}, #f59e0b, {ACCENT2});
      }}
      .proj-body {{ padding: 1.5rem 1.7rem 1.7rem; }}
      .proj-body h3 {{ margin: 0 0 0.2rem; font-size: 1.35rem; color: #111827; }}
      .proj-sub {{ color: #b45309; font-weight: 600; margin-bottom: 0.7rem; }}

      /* Timeline */
      .tl-item {{
          border-left: 3px solid {ACCENT}; padding: 0.2rem 0 1.2rem 1.4rem;
          position: relative; margin-left: 0.4rem;
      }}
      .tl-item::before {{
          content: ''; position: absolute; left: -9px; top: 6px;
          width: 13px; height: 13px; border-radius: 50%;
          background: {ACCENT}; border: 3px solid #fffbeb;
      }}
      .tl-date {{ font-size: 0.75rem; font-weight: 700; letter-spacing: 0.12em; color: #b45309; text-transform: uppercase; }}

      /* Contact banner */
      .contact-banner {{
          background:
            radial-gradient(600px 300px at 90% 0%, rgba(8,145,178,0.1), transparent 60%),
            linear-gradient(135deg, #fffbeb, #fef3c7);
          border: 1px solid rgba(251,191,36,0.35);
          color: #1f2937; border-radius: 20px; padding: 2.6rem 2.8rem;
          box-shadow: 0 4px 20px -4px rgba(0,0,0,0.04);
      }}
      .contact-banner h2 {{ color: #111827; margin-top: 0.2rem; }}
      .contact-banner a {{ color: {ACCENT}; }}
      .contact-line {{ font-size: 1.05rem; margin: 0.35rem 0; }}

      a {{ text-decoration: none; }}
      div[data-testid="stLinkButton"] > a {{
          border-radius: 999px !important; font-weight: 600;
          transition: all .18s ease;
      }}
      div[data-testid="stLinkButton"] > a:hover {{ transform: translateY(-2px); }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero">
      <p class="eyebrow">Entry-level Data & AI Professional</p>
      <h1>Turning raw data<br/>into <span>clear decisions.</span></h1>
      <p>I'm <strong style="color:#111827;">Pavan Dhanait</strong> — a Data Scientist,
      Data Analyst, ML Engineer, and aspiring GenAI Engineer building practical
      systems that connect analysis with action.</p>
      <p style="font-size:0.92rem; margin-top:1.4rem;">
        📍 Maharashtra, India &nbsp;·&nbsp; ✅ Open to entry-level opportunities
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

b1, b2, b3, b4 = st.columns([1.2, 1, 1, 2.2])
b1.link_button("📄 Explore my work", "#selected-work", use_container_width=True)
b2.link_button("🐙 GitHub", GITHUB, use_container_width=True)
b3.link_button("💼 LinkedIn", LINKEDIN, use_container_width=True)
b4.link_button(f"✉️ {EMAIL}", f"mailto:{EMAIL}", use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# About + animated stats
# ---------------------------------------------------------------------------
st.markdown('<p class="eyebrow eyebrow-dark">About</p>', unsafe_allow_html=True)
st.header("Curious by nature. Analytical by training.")
st.write(
    "I'm an Information Technology engineering student who enjoys moving from messy "
    "datasets to useful products — asking the right questions, finding patterns, testing "
    "models, and making the result understandable."
)
st.write(
    "My experience spans analytics dashboards, recommendation systems, and multimodal "
    "biometric applications. I'm now looking for a team where I can strengthen my craft "
    "while contributing dependable analysis and thoughtful machine learning work."
)

st.markdown("")
s1, s2, s3 = st.columns(3)
for col, num, suffix, label in [
    (s1, "9.12", "<em>/10</em>", "CGPA — B.E. Information Technology"),
    (s2, "2", "", "Industry internships (Amdox · Sumago)"),
    (s3, "2", "", "Featured builds — CaptClass & Crop Analytics"),
]:
    col.markdown(
        f"""
        <div class="stat-card">
          <div class="stat-num">{num}{suffix}</div>
          <div class="stat-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ---------------------------------------------------------------------------
# Skills — interactive radar + chips
# ---------------------------------------------------------------------------
st.markdown('<p class="eyebrow eyebrow-dark">Core toolkit</p>', unsafe_allow_html=True)
st.header("Skills built for the full data journey.")

radar_col, chips_col = st.columns([1.1, 1.4], gap="large")

with radar_col:
    categories = ["Data & Analysis", "Machine Learning", "Visualization", "Delivery & Tools", "Databases & SQL"]
    values = [5, 4, 4, 4, 4]
    fig = go.Figure(
        go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill="toself",
            fillcolor="rgba(217,119,6,0.12)",
            line=dict(color="#d97706", width=3),
            marker=dict(size=7, color="#b45309"),
            hovertemplate="%{theta}<extra></extra>",
        )
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5], showticklabels=False, gridcolor="#e5e7eb"),
            angularaxis=dict(gridcolor="#e5e7eb", tickfont=dict(size=12, family="Space Grotesk", color="#374151")),
            bgcolor="rgba(0,0,0,0)",
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        margin=dict(l=50, r=50, t=30, b=30),
        height=380,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.caption("Hover the radar — a snapshot of where I spend most of my craft.")

with chips_col:
    skill_groups = {
        "01 · Data & analysis": ["Python", "SQL", "EDA", "Statistics", "Pandas", "NumPy"],
        "02 · Machine learning": ["Scikit-learn", "Feature Engineering", "Model Evaluation", "Recommendation Systems"],
        "03 · Building & delivery": ["Streamlit", "Power BI", "Jupyter", "Git", "GitHub", "Data Visualization"],
    }
    for title, skills in skill_groups.items():
        st.subheader(title)
        st.markdown("".join(f'<span class="chip">{s}</span>' for s in skills), unsafe_allow_html=True)
        st.markdown("")

st.divider()

# ---------------------------------------------------------------------------
# Projects — tabbed deep dive
# ---------------------------------------------------------------------------
st.markdown('<p class="eyebrow eyebrow-dark" id="selected-work">Selected work</p>', unsafe_allow_html=True)
st.header("Built to solve, not just showcase.")

tab1, tab2 = st.tabs(["🧠 CaptClass — AI Attendance", "🌾 Crop Sales Data Analytics"])

with tab1:
    st.markdown(
        """
        <div class="proj"><div class="proj-band"></div><div class="proj-body">
          <h3>CaptClass</h3>
          <p class="proj-sub">AI-powered attendance & student management</p>
          <p class="muted">A Streamlit application combining face recognition and voice
          biometrics to manage student enrollment and attendance logs through relational
          data models and secure authentication.</p>
          <p><span class="chip">Python</span><span class="chip">Streamlit</span>
          <span class="chip">dlib</span><span class="chip">librosa</span>
          <span class="chip">resemblyzer</span></p>
        </div></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**🎭 Face recognition**\n\nEnrollment and identification of students through facial embeddings.")
    c2.markdown("**🎙️ Voice biometrics**\n\nA second biometric factor using audio features for verification.")
    c3.markdown("**🔐 Secure data layer**\n\nRelational data models and secure authentication for attendance logs.")

with tab2:
    st.markdown(
        """
        <div class="proj"><div class="proj-band"></div><div class="proj-body">
          <h3>Crop Sales Data Analytics</h3>
          <p class="proj-sub">From seasonal signals to planning insights</p>
          <p class="muted">An interactive analysis of seasonal trends, pricing patterns,
          and regional performance, designed to clarify demand and revenue signals for
          crop distribution and sales planning.</p>
          <p><span class="chip">Python</span><span class="chip">EDA</span>
          <span class="chip">Streamlit</span><span class="chip">Data Visualization</span></p>
        </div></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📈 Seasonal trends**\n\nRecurring demand patterns surfaced from historical crop sales data.")
    c2.markdown("**💰 Pricing patterns**\n\nHow prices move across seasons and categories, made readable.")
    c3.markdown("**🗺️ Regional performance**\n\nRegion-level comparisons to support distribution and planning decisions.")

st.divider()

# ---------------------------------------------------------------------------
# Experience — interactive timeline + details
# ---------------------------------------------------------------------------
st.markdown('<p class="eyebrow eyebrow-dark">Experience</p>', unsafe_allow_html=True)
st.header("Learning by building in real teams.")

tl_col, chart_col = st.columns([1.3, 1], gap="large")

with tl_col:
    st.markdown(
        """
        <div class="tl-item">
          <p class="tl-date">Feb — May 2026</p>
          <h3 style="margin:0.15rem 0;">Data Science Intern</h3>
          <p style="color:#b45309; font-weight:600; margin:0;">Amdox Solutions · Bengaluru, India</p>
          <p class="muted">Worked on crop sales analytics, applying data preprocessing,
          exploratory analysis, feature engineering, and recommendation algorithms to
          deliver personalized crop suggestions.</p>
          <p><span class="chip">Python</span><span class="chip">Scikit-learn</span><span class="chip">Recommendations</span></p>
        </div>
        <div class="tl-item">
          <p class="tl-date">Dec 2024 — Feb 2025</p>
          <h3 style="margin:0.15rem 0;">Python AI / ML Intern</h3>
          <p style="color:#b45309; font-weight:600; margin:0;">Sumago Infotech Pvt. Ltd. · Nashik, India</p>
          <p class="muted">Developed and optimized machine learning models, cleaned and
          visualized datasets, and contributed across training, evaluation, and
          application deployment workflows.</p>
          <p><span class="chip">Machine Learning</span><span class="chip">Pandas</span><span class="chip">Model Pipelines</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with chart_col:
    fig2 = go.Figure(
        go.Scatter(
            x=["Dec 2024", "Feb 2025", "Feb 2026", "May 2026"],
            y=[1, 1.35, 2, 2.35],
            mode="lines+markers+text",
            text=["Sumago<br>AI/ML Intern", "", "Amdox<br>Data Science Intern", ""],
            textposition="top center",
            line=dict(color="#d97706", width=4, shape="spline", smoothing=1.2),
            marker=dict(size=13, color="#ffffff", line=dict(color="#d97706", width=3)),
            hovertemplate="%{x}<extra></extra>",
        )
    )
    fig2.update_layout(
        title=dict(text="My journey so far", font=dict(family="Space Grotesk", size=18, color="#111827")),
        showlegend=False,
        xaxis=dict(showgrid=False, tickfont=dict(size=11, color="#4b5563")),
        yaxis=dict(visible=False, range=[0.6, 2.9]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
        height=340,
    )
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
    st.caption("Two internships, one direction: deeper into applied data science.")

st.divider()

# ---------------------------------------------------------------------------
# Education & credentials
# ---------------------------------------------------------------------------
e1, e2 = st.columns(2, gap="large")
with e1:
    st.markdown('<p class="eyebrow eyebrow-dark">Education</p>', unsafe_allow_html=True)
    st.subheader("🎓 B.E. Information Technology")
    st.write("Pravara Rural Engineering College, Loni")
    st.caption("Savitribai Phule Pune University · 2022—2026")
    st.progress(0.912, text="**CGPA 9.12 / 10**")

with e2:
    st.markdown('<p class="eyebrow eyebrow-dark">Credentials & recognition</p>', unsafe_allow_html=True)
    st.markdown(f"📖 [**Microsoft AI & ML Engineering**]({CERT_URL}) — Professional Certificate · June 2025")
    st.markdown("📖 **Database Management System** — NPTEL Certificate · September 2024")
    st.markdown("🏆 **Star Intern & academic top scorer** — Recognized at Sumago Infotech; scored 9.36 SGPA in second-year IT.")

st.divider()

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="contact-banner">
      <p class="eyebrow">Available for entry-level opportunities</p>
      <h2>Have a data problem worth solving? Let's talk.</h2>
      <p class="contact-line">📞 {PHONE} &nbsp;·&nbsp; ✉️ <a href="mailto:{EMAIL}"><u>{EMAIL}</u></a></p>
      <p class="contact-line">🐙 <a href="{GITHUB}"><u>GitHub</u></a> &nbsp;·&nbsp;
         💼 <a href="{LINKEDIN}"><u>LinkedIn</u></a></p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
cb1, cb2, cb3 = st.columns([1, 1, 2])
cb1.link_button("✉️ Email me", f"mailto:{EMAIL}", use_container_width=True)
cb2.link_button("🐙 View GitHub", GITHUB, use_container_width=True)
cb3.link_button("💼 Connect on LinkedIn", LINKEDIN, use_container_width=True)

st.caption("© 2026 Pavan Dhanait · Data Science · Analytics · Machine Learning · GenAI")
