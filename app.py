import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Voice Analytics",
    page_icon="📞",
    layout="wide"
)

# ---------- SIDEBAR ----------
st.sidebar.markdown("## 📞 Voice Analytics")
page = st.sidebar.radio(
    "เลือกหน้า:",
    [
        "หน้าหลัก",
        "ไฟล์เสียง",
        "อัดเสียง",
        "วิเคราะห์",
        "รายงาน",
        "Sentiment Analysis",
        "ตั้งค่า",
    ]
)

# ---------- COMPONENT ----------
def card(title, value, icon=""):
    st.markdown(
        f"""
        <div style="background:#2b2f36;padding:20px;border-radius:12px">
            <h4>{icon} {title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- PAGES ----------
def dashboard_page():
    st.markdown("## 🎯 Voice Analytics Dashboard")
    st.caption("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

    c1, c2, c3, c4 = st.columns(4)
    with c1: card("ไฟล์เสียง", "0", "📂")
    with c2: card("การวิเคราะห์", "0", "📊")
    with c3: card("คะแนนเฉลี่ย", "N/A", "⭐")
    with c4: card("สถานะ", "พร้อมใช้งาน", "✅")

def upload_page():
    st.markdown("## 📂 ไฟล์เสียง")
    st.file_uploader("อัปโหลดไฟล์เสียง (WAV)", type=["wav"])

def record_page():
    st.markdown("## 🎤 อัดเสียง")
    st.text_input("ID ผู้ใช้บริการ")
    st.text_input("ID เจ้าหน้าที่")
    st.text_input("หมายเลขโทรศัพท์")
    st.slider("ระยะเวลา (วินาที)", 1, 60, 10)
    st.button("🔴 เริ่มอัดเสียง")

def analysis_page():
    st.markdown("## 📊 วิเคราะห์ไฟล์เสียง")
    st.info("ยังไม่มีข้อมูล")

def report_page():
    st.markdown("## 📑 รายงาน")
    st.warning("ยังไม่มีรายงาน")

def sentiment_page():
    st.markdown("## 😊 Sentiment Analysis")

    data = {
        "Positive": 60,
        "Neutral": 25,
        "Negative": 15
    }

    st.bar_chart(data)

def setting_page():
    st.markdown("## ⚙️ ตั้งค่า")
    st.checkbox("โหมดมืด")
    st.button("บันทึกการตั้งค่า")

# ---------- ROUTER ----------
if page == "หน้าหลัก":
    dashboard_page()
elif page == "ไฟล์เสียง":
    upload_page()
elif page == "อัดเสียง":
    record_page()
elif page == "วิเคราะห์":
    analysis_page()
elif page == "รายงาน":
    report_page()
elif page == "Sentiment Analysis":
    sentiment_page()
elif page == "ตั้งค่า":
    setting_page()

st.markdown("---")
st.caption("Voice Analytics Dashboard | Call Center UX Analyzer")
