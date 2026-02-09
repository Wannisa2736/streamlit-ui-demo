import streamlit as st
import numpy as np

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Voice Analytics",
    layout="wide",
    page_icon="📞"
)

# ------------------ STYLE ------------------
st.markdown("""
<style>
body {
    background-color: #0f1117;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 16px;
}
.feature {
    background-color: #16232e;
    padding: 20px;
    border-radius: 12px;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

# ------------------ COMPONENT ------------------
def card(title, value, icon):
    st.markdown(f"""
    <div class="card">
        <h4>{icon} {title}</h4>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PAGES ------------------
def dashboard_page():
    st.markdown("## 🎯 Voice Analytics Dashboard")
    st.caption("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

    c1, c2, c3, c4 = st.columns(4)
    with c1: card("ไฟล์เสียง", "0", "📂")
    with c2: card("การวิเคราะห์", "0", "📊")
    with c3: card("คะแนนเฉลี่ย", "N/A", "⭐")
    with c4: card("สถานะ", "พร้อมใช้งาน", "✅")

    st.markdown("### 📋 ฟีเจอร์หลัก")

    f1, f2 = st.columns(2)
    with f1:
        st.markdown("""
        <div class="feature">
        <h4>📂 ไฟล์เสียง</h4>
        • อัปโหลดไฟล์ WAV<br>
        • ดูรายการไฟล์<br>
        • เปิดฟังเสียง
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature">
        <h4>🎙️ อัดเสียง</h4>
        • สร้างไฟล์เสียงทดสอบ<br>
        • อัดเสียงจริง<br>
        • บันทึกข้อมูลสนทนา
        </div>
        """, unsafe_allow_html=True)

    f3, f4 = st.columns(2)
    with f3:
        st.markdown("""
        <div class="feature" style="background:#143d2b">
        <h4>📊 วิเคราะห์</h4>
        • วิเคราะห์คุณภาพเสียง<br>
        • ประเมิน Sentiment<br>
        • คำนวณ UX Score
        </div>
        """, unsafe_allow_html=True)

    with f4:
        st.markdown("""
        <div class="feature" style="background:#3a2f12">
        <h4>📄 รายงาน</h4>
        • สรุปผลลัพธ์<br>
        • ส่งออก JSON<br>
        • ดูข้อมูลเชิงลึก
        </div>
        """, unsafe_allow_html=True)

def file_page():
    st.markdown("## 📂 ไฟล์เสียง")
    st.file_uploader("อัปโหลดไฟล์เสียง WAV", type=["wav"])
    st.info("ยังไม่มีไฟล์เสียง")

def record_page():
    st.markdown("## 🎙️ ข้อมูลการสนทนา")

    c1, c2 = st.columns(2)
    with c1:
        st.text_input("ID ผู้ใช้บริการ", "CUST001")
    with c2:
        st.text_input("ID เจ้าหน้าที่", "AGENT001")

    st.text_input("หมายเลขโทรศัพท์", "089-123-4567")

    st.markdown("### ⚙️ ตัวเลือกเสียง")
    st.number_input("ความถี่ตัวอย่าง", value=44100)
    st.radio("จำนวนช่อง", ["Mono (1)", "Stereo (2)"])
    st.slider("ระยะเวลา (วินาที)", 1, 60, 10)

    st.button("🔴 เริ่มอัดเสียง")
    st.button("➕ สร้างไฟล์ทดสอบ")

def analysis_page():
    st.markdown("## 📊 วิเคราะห์ไฟล์เสียง")
    st.info("ยังไม่มีไฟล์สำหรับการวิเคราะห์")

def report_page():
    st.markdown("## 📄 รายงาน")
    st.metric("จำนวนการวิเคราะห์", 7)
    st.metric("คะแนนเฉลี่ย", "8.45 / 10")
    st.metric("ยอดเยี่ยม", "0 / 7")

def sentiment_page():
    st.markdown("## 😊 Sentiment Analysis")
    st.selectbox("เลือกไฟล์เสียง", [])
    st.info("ยังไม่มีข้อมูล Sentiment")

def setting_page():
    st.markdown("## ⚙️ ตั้งค่า")
    st.checkbox("โหมด Dark Mode", value=True)
    st.checkbox("บันทึก Log")

# ------------------ SIDEBAR ------------------
st.sidebar.title("📞 Voice Analytics")
page = st.sidebar.radio(
    "เลือกหน้า:",
    [
        "หน้าหลัก",
        "ไฟล์เสียง",
        "อัดเสียง",
        "วิเคราะห์",
        "รายงาน",
        "Sentiment Analysis",
        "ตั้งค่า"
    ]
)

# ------------------ ROUTER ------------------
if page == "หน้าหลัก":
    dashboard_page()
elif page == "ไฟล์เสียง":
    file_page()
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
