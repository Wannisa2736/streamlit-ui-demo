import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Voice Analytics",
    page_icon="📞",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
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

# ---------------- COMMON STYLE ----------------
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

# ---------------- PAGES ----------------
def dashboard_page():
    st.markdown("## 🎯 Voice Analytics Dashboard")
    st.caption("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

    col1, col2, col3, col4 = st.columns(4)
    with col1: card("ไฟล์เสียง", "0", "📂")
    with col2: card("การวิเคราะห์", "0", "📊")
    with col3: card("คะแนนเฉลี่ย", "N/A", "⭐")
    with col4: card("สถานะ", "พร้อมใช้งาน", "✅")

    st.markdown("### 📋 ฟีเจอร์หลัก")
    c1, c2 = st.columns(2)

    with c1:
        st.success("📂 ไฟล์เสียง\n- อัปโหลด WAV\n- ดูรายการไฟล์\n- เปิดไฟล์เสียง")

    with c2:
        st.info("🎤 อัดเสียง\n- อัดเสียง WAV\n- อัดเสียงสด\n- บันทึกข้อมูลสนทนา")

    c3, c4 = st.columns(2)
    with c3:
        st.warning("📊 วิเคราะห์\n- วิเคราะห์คุณภาพเสียง\n- ประเมิน Sentiment\n- คำนวณ UX Score")

    with c4:
        st.error("📑 รายงาน\n- สรุปผล\n- ส่งออก JSON\n- ข้อมูลเชิงลึก")

def upload_page():
    st.markdown("## 📂 ไฟล์เสียง")
    st.file_uploader("อัปโหลดไฟล์เสียง (WAV)", type=["wav"])
    st.info("ยังไม่มีไฟล์เสียง")

def record_page():
    st.markdown("## 🎤 อัดเสียง")
    st.text_input("ID ผู้ใช้บริการ")
    st.text_input("ID เจ้าหน้าที่")
    st.text_input("หมายเลขโทรศัพท์")
    st.slider("ระยะเวลา (วินาที)", 1, 60, 10)
    st.button("🔴 เริ่มอัดเสียง")

def analysis_page():
    st.markdown("## 📊 วิเคราะห์ไฟล์เสียง")
    st.info("ยังไม่มีข้อมูลให้วิเคราะห์")

def report_page():
    st.markdown("## 📑 รายงาน")
    st.warning("ยังไม่มีรายงาน")

def sentiment_page():
    st.markdown("## 😊 Sentiment Analysis")

    # mock data
    labels = ["Positive", "Neutral", "Negative"]
    values = [60, 25, 15]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("เปอร์เซ็นต์")
    ax.set_title("ผลการวิเคราะห์ Sentiment")

    st.pyplot(fig)

def setting_page():
    st.markdown("## ⚙️ ตั้งค่า")
    st.checkbox("โหมดมืด")
    st.button("บันทึกการตั้งค่า")

# ---------------- ROUTER ----------------
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
