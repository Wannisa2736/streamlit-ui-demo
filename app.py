import streamlit as st
import pandas as pd

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="Voice Analytics Dashboard",
    layout="wide"
)

# ===============================
# CSS (Dark UI)
# ===============================
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #111827;
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1f2933;
}
section[data-testid="stSidebar"] h2 {
    color: white;
}
section[data-testid="stSidebar"] button {
    width: 100%;
    background: none;
    color: #cbd5f5;
    border-radius: 8px;
    margin-bottom: 6px;
}
section[data-testid="stSidebar"] button:hover {
    background-color: #374151;
}

/* Card */
.card {
    background: #2a3038;
    border-radius: 14px;
    padding: 24px;
    box-shadow: 0 0 0 1px #374151;
}

/* Metric */
.metric-box {
    background: #2a3038;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #374151;
}
.metric-title {
    font-size: 14px;
    color: #9ca3af;
}
.metric-value {
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Session state
# ===============================
if "page" not in st.session_state:
    st.session_state.page = "หน้าหลัก"

# ===============================
# Sidebar (เรียงตามที่กำหนด)
# ===============================
with st.sidebar:
    st.markdown("## 📞 Voice Analytics")

    if st.button("🏠 หน้าหลัก"):
        st.session_state.page = "หน้าหลัก"
    if st.button("📁 ไฟล์เสียง"):
        st.session_state.page = "ไฟล์เสียง"
    if st.button("🎙️ อัดเสียง"):
        st.session_state.page = "อัดเสียง"
    if st.button("📊 วิเคราะห์"):
        st.session_state.page = "วิเคราะห์"
    if st.button("📑 รายงาน"):
        st.session_state.page = "รายงาน"
    if st.button("😊 Sentiment Analysis"):
        st.session_state.page = "Sentiment Analysis"
    if st.button("⚙️ ตั้งค่า"):
        st.session_state.page = "ตั้งค่า"

# ===============================
# Helper
# ===============================
def metric(title, value):
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def card(title, items):
    li = "".join([f"<li>{i}</li>" for i in items])
    st.markdown(f"""
    <div class="card">
        <b>{title}</b>
        <ul>{li}</ul>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# Pages
# ===============================

# 1. หน้าหลัก
if st.session_state.page == "หน้าหลัก":
    st.markdown("## 🎯 Voice Analytics Dashboard")
    st.caption("Call Center UX Analyzer")

    c1, c2, c3, c4 = st.columns(4)
    with c1: metric("ไฟล์เสียง", "9")
    with c2: metric("อัดเสียง", "3")
    with c3: metric("คะแนนเฉลี่ย", "8.45")
    with c4: metric("สถานะระบบ", "พร้อมใช้งาน")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        card("ไฟล์เสียง", ["อัปโหลด", "เปิดไฟล์"])
    with col2:
        card("อัดเสียง", ["บันทึกการสนทนา", "ตั้งค่าการอัด"])
    with col3:
        card("วิเคราะห์", ["UX Score", "Sentiment"])
    with col4:
        card("รายงาน", ["สรุปผล", "ดูย้อนหลัง"])

# 2. ไฟล์เสียง
elif st.session_state.page == "ไฟล์เสียง":
    st.markdown("## 📁 ไฟล์เสียง")
    uploaded = st.file_uploader("อัปโหลดไฟล์เสียง (.wav)", type=["wav"])
    if uploaded:
        st.success("อัปโหลดไฟล์เรียบร้อย")
        st.audio(uploaded)

# 3. อัดเสียง (เหมือนภาพ)
elif st.session_state.page == "อัดเสียง":
    st.markdown("## 🎙️ ข้อมูลการสนทนา")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("ID ผู้ใช้บริการ", value="CUST001")
    with col2:
        st.text_input("ID เจ้าหน้าที่", value="AGENT001")

    st.text_input("หมายเลขโทรศัพท์", value="089-123-4567")

    st.markdown("### ⚙️ ตัวเลือกการอัดเสียง")
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.text_input("ความถี่ตัวอย่าง (Hz)", value="44100")

        st.radio(
            "จำนวนช่อง",
            ["Mono (1)", "Stereo (2)"],
            index=0,
            horizontal=True
        )

        st.slider(
            "ระยะเวลา (วินาที)",
            min_value=1,
            max_value=60,
            value=10
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🎧 อัดเสียงจริง")
    b1, b2, b3 = st.columns(3)
    with b1:
        st.button("🔴 เริ่มอัดเสียง", use_container_width=True)
    with b2:
        st.button("✏️ แก้ไขข้อมูล", use_container_width=True)
    with b3:
        st.button("➕ สร้างไฟล์ทดสอบ", use_container_width=True)

# 4. วิเคราะห์
elif st.session_state.page == "วิเคราะห์":
    st.markdown("## 📊 วิเคราะห์เสียง")
    st.progress(0.7)
    st.caption("กำลังวิเคราะห์คุณภาพเสียงและบทสนทนา...")

# 5. รายงาน
elif st.session_state.page == "รายงาน":
    st.markdown("## 📑 รายงานผล")

    c1, c2, c3 = st.columns(3)
    with c1: metric("จำนวนไฟล์", "7")
    with c2: metric("คะแนนเฉลี่ย", "8.45 / 10")
    with c3: metric("คุณภาพ", "Good")

    df = pd.DataFrame({
        "ไฟล์": [f"call_00{i}.wav" for i in range(1, 8)],
        "UX Score": [8.45]*7,
        "ผลลัพธ์": ["Good"]*7
    })
    st.dataframe(df, use_container_width=True)

# 6. Sentiment Analysis
elif st.session_state.page == "Sentiment Analysis":
    st.markdown("## 😊 Sentiment Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card" style="text-align:center">
            <h3>🙂 Positive</h3>
            <h1 style="color:#22c55e;">100%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.bar_chart({"Positive": [6], "Negative": [0]})

# 7. ตั้งค่า (เหมือนภาพ)
elif st.session_state.page == "ตั้งค่า":
    st.markdown("## ⚙️ ตั้งค่า")

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.selectbox("ภาษา", ["ภาษาไทย", "English"])
        st.selectbox("ธีม", ["Dark Mode", "Light Mode"])

        st.checkbox("เปิดใช้งานการแจ้งเตือน", value=True)
        st.checkbox("บันทึกประวัติการใช้งาน", value=False)

        c1, c2 = st.columns(2)
        with c1:
            st.button("💾 บันทึก")
        with c2:
            st.button("ยกเลิก")

        st.markdown("</div>", unsafe_allow_html=True)
