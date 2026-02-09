import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Voice Analytics Dashboard",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "หน้าหลัก"

# -----------------------------
# SIDEBAR STYLE (RED THEME + ACTIVE)
# -----------------------------
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #fff5f5;
}

div.stButton > button {
    width: 100%;
    border-radius: 8px;
    background-color: #ffffff;
    color: #333;
    border: 1px solid #e5e5e5;
    margin-bottom: 6px;
    font-size: 15px;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background-color: #fee2e2;
    color: #b91c1c;
}

div.stButton > button.active {
    background-color: #dc2626 !important;
    color: white !important;
    font-weight: 600;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 📞 Voice Analytics")
    st.markdown("เลือกหน้า:")

    menu = [
        "หน้าหลัก",
        "ไฟล์เสียง",
        "อัดเสียง",
        "วิเคราะห์",
        "รายงาน",
        "Sentiment Analysis",
        "ตั้งค่า"
    ]

    for m in menu:
        clicked = st.button(m, use_container_width=True, key=m)

        if clicked:
            st.session_state.page = m

        is_active = st.session_state.page == m

        st.markdown(f"""
        <script>
        const buttons = window.parent.document.querySelectorAll('button');
        buttons.forEach(btn => {{
            if (btn.innerText === "{m}") {{
                btn.classList.remove("active");
                {"btn.classList.add('active');" if is_active else ""}
            }}
        }});
        </script>
        """, unsafe_allow_html=True)

# -----------------------------
# PAGE: หน้าหลัก
# -----------------------------
if st.session_state.page == "หน้าหลัก":
    st.title("🎯 Voice Analytics Dashboard")
    st.caption("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📁 ไฟล์เสียง", "0")
    c2.metric("📊 การวิเคราะห์", "0")
    c3.metric("⭐ คะแนนเฉลี่ย", "N/A")
    c4.success("พร้อมใช้งาน")

    st.divider()

    col1, col2 = st.columns(2)
    col1.info("📁 **ไฟล์เสียง**\n\n- อัปโหลดไฟล์ WAV\n- ดูรายการไฟล์\n- เปิดฟังเสียง")
    col2.warning("🎤 **อัดเสียง**\n\n- อัดเสียงทดลอง\n- ตั้งค่า sample rate\n- บันทึกไฟล์")

    col3, col4 = st.columns(2)
    col3.success("📊 **วิเคราะห์**\n\n- วิเคราะห์คุณภาพเสียง\n- ประเมิน Sentiment\n- คำนวณ UX Score")
    col4.error("📑 **รายงาน**\n\n- สรุปผล\n- Export JSON\n- ดูย้อนหลัง")

# -----------------------------
# PAGE: ไฟล์เสียง
# -----------------------------
elif st.session_state.page == "ไฟล์เสียง":
    st.title("📂 จัดการไฟล์เสียง")

    uploaded = st.file_uploader(
        "อัปโหลดไฟล์เสียง (WAV, MP3, M4A)",
        type=["wav", "mp3", "m4a"]
    )

    if uploaded:
        st.success(f"อัปโหลดไฟล์ {uploaded.name} สำเร็จ")

    st.subheader("📄 รายการไฟล์เสียง")
    st.info("ยังไม่มีไฟล์เสียง กรุณาอัปโหลดหรือสร้างไฟล์")

# -----------------------------
# PAGE: อัดเสียง
# -----------------------------
elif st.session_state.page == "อัดเสียง":
    st.title("🎙️ ข้อมูลการสนทนา")

    col1, col2 = st.columns(2)
    cust_id = col1.text_input("ID ผู้ใช้บริการ", "CUST001")
    agent_id = col2.text_input("ID เจ้าหน้าที่", "AGENT001")

    phone = st.text_input("หมายเลขโทรศัพท์", "089-123-4567")

    st.divider()

    st.subheader("⚙️ ตัวเลือกการอัดเสียง")
    sample_rate = st.number_input("ความถี่ตัวอย่าง", value=44100)
    channel = st.radio("จำนวนช่อง", ["Mono (1)", "Stereo (2)"])
    duration = st.slider("ระยะเวลา (วินาที)", 1, 60, 10)

    st.divider()
    if st.button("🔴 เริ่มอัดเสียง"):
        st.info("โหมด Demo: ยังไม่ได้เชื่อม PyAudio")

# -----------------------------
# PAGE: วิเคราะห์
# -----------------------------
elif st.session_state.page == "วิเคราะห์":
    st.title("📈 วิเคราะห์ไฟล์เสียง")

    if st.button("📂 วิเคราะห์ทั้งหมด"):
        st.success("วิเคราะห์เสร็จสิ้น (Mock Data)")

    st.info("ยังไม่มีไฟล์เสียง กรุณาอัปโหลดไฟล์ที่หน้า **ไฟล์เสียง**")

# -----------------------------
# PAGE: รายงาน
# -----------------------------
elif st.session_state.page == "รายงาน":
    st.title("📑 รายงาน")

    c1, c2, c3 = st.columns(3)
    c1.metric("จำนวนการวิเคราะห์", "7")
    c2.metric("คะแนนเฉลี่ย", "8.45 / 10")
    c3.metric("ยอดเยี่ยม", "0 / 7")

    st.divider()

    data = {
        "ไฟล์": [f"test_{i}.wav" for i in range(1, 8)],
        "UX Score": [8.45]*7,
        "ระดับ": ["ดี (Good)"]*7,
        "เวลา": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]*7
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

# -----------------------------
# PAGE: Sentiment Analysis
# -----------------------------
elif st.session_state.page == "Sentiment Analysis":
    st.title("😊😐😠 กราฟความเห็นบวก/ลบ")

    col1, col2 = st.columns(2)
    col1.metric("บวก", "100%")
    col2.metric("ลบ", "0%")

    st.progress(1.0)
    st.caption("ความพึงพอใจ: 100%")

# -----------------------------
# PAGE: ตั้งค่า
# -----------------------------
elif st.session_state.page == "ตั้งค่า":
    st.title("⚙️ ตั้งค่า")

    lang = st.selectbox("ภาษา", ["ภาษาไทย", "English"])
    theme = st.selectbox("ธีม", ["Dark Mode", "Light Mode"])

    notify = st.checkbox("เปิดใช้งานการแจ้งเตือน", value=True)
    log = st.checkbox("บันทึกประวัติการใช้งาน")

    col1, col2 = st.columns(2)
    col1.button("💾 บันทึก")
    col2.button("❌ ยกเลิก")
