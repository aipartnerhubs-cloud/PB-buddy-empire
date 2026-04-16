import streamlit as st
import re
from datetime import datetime

# --- 1. AI बडी की आवाज़ और अलर्ट लॉजिक ---
def ai_badi_speak(message, status="info"):
    script = f"""<script>
        var msg = new SpeechSynthesisUtterance('{message}');
        msg.lang = 'hi-IN';
        msg.rate = 0.9;
        window.speechSynthesis.speak(msg);
    </script>"""
    st.components.v1.html(script, height=0)
    
    if status == "error": st.error(message)
    elif status == "warning": st.warning(message)
    else: st.success(message)

st.set_page_config(page_title="PB Buddy: Smart Coach", layout="centered")

# --- 2. मुख्य डैशबोर्ड ---
st.title("🛡️ BP Buddy: AI Smart Coach")
st.info("प्रशांत भाई, यह सिस्टम एजेंट का हाथ पकड़कर उसे PB Partners पर काम सिखाएगा।")

# --- 3. डेटा ऑडिट सेक्शन (गलती पकड़ना) ---
st.header("🔍 डेटा की जांच करें")
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        v_num = st.text_input("गाड़ी का नंबर (उदा: MH12AB1234)").upper().replace(" ", "")
    with col2:
        expiry = st.date_input("पुरानी पॉलिसी की एक्सपायरी")

    if st.button("✅ डेटा चेक करें"):
        # गाड़ी नंबर का वेरिफिकेशन
        if not re.match("^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$", v_num):
            ai_badi_speak("गाड़ी नंबर का फॉर्मेट गलत है। कृपया इसे MH12AB1234 जैसा लिखें।", "error")
        
        # एक्सपायरी का वेरिफिकेशन
        days_left = (expiry - datetime.now().date()).days
        if days_left < 0:
            ai_badi_speak("यह पॉलिसी एक्सपायर हो चुकी है। एजेंट से कहें कि इंस्पेक्शन (Inspection) के लिए तैयार रहे।", "warning")
        else:
            ai_badi_speak("डेटा सही लग रहा है। अब पी बी पार्टनर्स ऐप पर कोटेशन बनाएं।", "success")

# --- 4. ट्रेनिंग और गाइडिंग (Steps) ---
st.divider()
st.header("🎓 PB Partners ट्रेनिंग गाइड")

with st.expander("Step 1: कोटेशन कैसे बनाएं?"):
    if st.button("सुनें: कोटेशन गाइड"):
        ai_badi_speak("पी बी पार्टनर्स ऐप खोलें, मोटर सेक्शन चुनें और गाड़ी का नंबर डालकर अलग-अलग कंपनियों के रेट चेक करें।")
    st.link_button("PB Partners पोर्टल खोलें 🌐", "https://www.pbpartners.com/")

with st.expander("Step 2: डॉक्युमेंट अपलोड"):
    if st.button("सुनें: फोटो गाइड"):
        ai_badi_speak("आरसी और पुरानी पॉलिसी की फोटो साफ़ होनी चाहिए। ध्यान रहे कि कोई कोना कटा न हो।")

with st.expander("Step 3: पेमेंट और पॉलिसी"):
    if st.button("सुनें: पेमेंट गाइड"):
        ai_badi_speak("पेमेंट होने के बाद 'My Policies' में जाएं और तुरंत पीडीएफ डाउनलोड करके ग्राहक को व्हाट्सएप करें।")

# --- 5. साइडबार ---
st.sidebar.title("🤖 AI Status")
if st.sidebar.button("AI कोच को जगाएं"):
    ai_badi_speak("नमस्ते प्रशांत भाई। मैं तैयार हूँ एजेंट को गाइड करने के लिए।")
