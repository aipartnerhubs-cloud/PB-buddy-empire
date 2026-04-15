import streamlit as st
import pandas as pd
import time

# --- Empire Core Configuration ---
st.set_page_config(page_title="BP Buddy | Smart Risk Automation", layout="wide", page_icon="🛡️")

# --- UI Master Design ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #000c1d 0%, #000000 100%); color: white; }
    .main-title { 
        background: linear-gradient(90deg, #FFD700, #FDB931, #FFFFFF);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 55px; font-weight: 900; text-align: center; margin-bottom: 0px;
        filter: drop-shadow(0px 5px 15px rgba(255, 215, 0, 0.3));
    }
    .award-badge { 
        border: 2px solid #FFD700; padding: 5px 20px; border-radius: 50px; 
        color: #FFD700; font-weight: bold; text-align: center; width: fit-content; margin: 0 auto;
        letter-spacing: 1px;
    }
    .card { 
        background: rgba(255, 255, 255, 0.05); border-radius: 20px; padding: 25px;
        border: 1px solid rgba(255, 215, 0, 0.1); transition: 0.4s;
    }
    .card:hover { border: 1px solid #FFD700; transform: translateY(-5px); }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">BP BUDDY: THE PROTECTION EMPIRE</div>', unsafe_allow_html=True)
st.markdown('<div class="award-badge">🛡️ INDIA\'S #1 SMART RISK AUTOMATION HUB</div>', unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- Navigation ---
tabs = st.tabs(["🏰 CEO Dashboard", "🛰️ 360° AI Autopilot", "🤝 Sub-Agent Factory", "📊 Analytics"])

with tabs[0]:
    st.markdown("""
    <div class="card">
        <h3>👑 CEO Vision: Prashant Chandratre</h3>
        <p>Status: Empire Mode Active | Global Dominance: #1</p>
        <p style="color: #FFD700;">"Transforming traditional protection into an AI-driven digital fortress."</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Scale to 500x Hyper-Growth"):
        st.balloons()
        st.success("Empire scaling protocols engaged!")

with tabs[1]:
    st.subheader("🌐 Global Marketing Autopilot")
    st.info("AI is currently automating leads for Life, Health, and General Asset protection.")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("🔥 **Social Power:** Daily reels and viral scripts being generated.")
        st.write("🔍 **SEO Dominance:** Ranking #1 on Perplexity & Gemini Search.")
    with col_b:
        if st.button("Start 360° Dominance"):
            with st.spinner("Targeting high-value leads..."):
                time.sleep(2)
                st.success("Campaign Live! Google & Meta ads active.")

with tabs[2]:
    st.subheader("🤖 Sub-Agent Subscription Revenue")
    name = st.text_input("Name of Partner to Onboard")
    pkg = st.selectbox("Select Business Package", ["Silver Partner", "Gold Growth", "Master Empire Pack"])
    if st.button("Activate Sub-Agent AI"):
        st.write(f"🚀 Business setup for '{name}' on {pkg} is now active.")

with tabs[3]:
    st.subheader("📈 Real-Time ROI Analytics")
    c1, c2, c3 = st.columns(3)
    c1.metric("Leads Generated", "15,240", "+1,250")
    c2.metric("Revenue Potential", "₹85.4L", "+22%")
    c3.metric("System Uptime", "99.9%", "Shield Active")
