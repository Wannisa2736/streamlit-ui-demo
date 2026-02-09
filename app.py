import streamlit as st
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Voice Analytics",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
body { background-color:#1f232a; }
.card {
    background:#2a2f36;
    padding:24px;
    border-radius:16px;
    margin-bottom:20px;
}
.footer {
    text-align:center;
    color:#888;
    font-size:12px;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 📞 Voice Analytics")

page = st.sidebar.radio(
    "เลือกหน้า:",
    [
        "หน้าหลัก",
        "ไฟล์เสียง",
        "อัดเสียง",
        "วิเคราะห์ไฟล์เสียง",
        "รายงาน",
        "Sentiment Analysis",
        "ตั้งค่า"
    ]
)

# ---------------- DASHBOARD ----------------
def dashboard_page():
    st.markdown("## 🏠 หน้าหลัก")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📁 ไฟล์เสียง", "7")
    c2.metric("📊 วิเคราะห์แล้ว", "7")
    c3.metric("⭐ คะแนนเฉลี่ย", "8.45/10")
    c4.metric("✅ สถานะ", "ดี (Good)")

# ---------------- FILE ----------------
def file_page():
    st.markdown("## 🎧 ไฟล์เสียง")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.info("หน้าอัปโหลดไฟล์เสียง (Prototype)")
    st.file_uploader("อัปโหลดไฟล์เสียง", type=["wav", "mp3"])
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RECORD (รูปที่เพิ่งส่ง) ----------------
def record_page():
    st.markdown("## 🎙️ ข้อมูลการสนทนา")

    # ข้อมูลผู้ใช้
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.text_input("ID ผู้ใช้บริการ", "CUST001")
    col2.text_input("ID เจ้าหน้าที่", "AGENT001")
    st.text_input("หมายเลขโทรศัพท์", "089-123-4567")
    st.markdown("</div>", unsafe_allow_html=True)

    # ตัวเลือกเสียง
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### ⚙️ ตัวเลือก")
    st.text_input("ความถี่ตัวอย่าง", "44100")

    channel = st.radio(
        "จำนวนช่อง",
        ["Mono (1)", "Stereo (2)"],
        index=0
    )

    duration = st.slider("ระยะเวลา (วินาที)", 1, 60, 10)
    st.markdown("</div>", unsafe_allow_html=True)

    # อัดเสียง
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎤 อัดเสียงจริง")

    colb1, colb2, colb3 = st.columns(3)
    colb1.button("🔴 เริ่มอัดเสียง")
    colb2.button("✏️ แก้ไข")
    colb3.button("➕ สร้างไฟล์ทดสอบ")

    st.caption("หมายเหตุ: เป็น UX Prototype ยังไม่อัดเสียงจริง")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ANALYSIS ----------------
def analysis_page():
    st.markdown("## 📊 วิเคราะห์ไฟล์เสียง")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.button("📂 วิเคราะห์ทั้งหมด")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.warning(
        'ยังไม่มีไฟล์เสียง กรุณาไปที่ "ไฟล์เสียง" เพื่อสร้างหรือโหลดไฟล์'
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- REPORT ----------------
def report_page():
    st.markdown("## 📈 รายงาน")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("📁 จำนวนการวิเคราะห์", "7")
    c2.metric("⭐ คะแนนเฉลี่ย", "8.45/10")
    c3.metric("✅ ยอดเยี่ยม", "0/7")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    data = {
        "ไฟล์": [f"test_20260205_15012{i}.wav" for i in range(8,15)],
        "UX Score": [8.45]*7,
        "ระดับ": ["ดี (Good)"]*7,
        "เวลา": ["2026-02-05 15:01:29"]*7
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SENTIMENT ----------------
def sentiment_page():
    st.markdown("## 😊 Sentiment Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        fig, ax = plt.subplots()
        ax.pie(
            [100, 0],
            labels=["บวก", "ลบ"],
            colors=["#19c37d", "#f4c430"],
            wedgeprops={"width":0.35},
            startangle=90
        )
        ax.text(0, 0, "100%", ha="center", va="center", fontsize=20)
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        fig2, ax2 = plt.subplots()
        ax2.bar(["บวก"], [7])
        ax2.set_ylim(0, 8)
        st.pyplot(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.progress(1.0, "😊 ความพึงพอใจ 100%")
    st.progress(0.0, "😐 ความไม่พึงพอใจ 0%")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SETTING ----------------
def setting_page():
    st.markdown("## ⚙️ ตั้งค่า")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.selectbox("ภาษา", ["ภาษาไทย", "English"])
    st.selectbox("ธีม", ["Dark Mode", "Light Mode"])
    st.checkbox("เปิดแจ้งเตือน", True)
    st.button("บันทึก")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ROUTER ----------------
if page == "หน้าหลัก":
    dashboard_page()
elif page == "ไฟล์เสียง":
    file_page()
elif page == "อัดเสียง":
    record_page()
elif page == "วิเคราะห์ไฟล์เสียง":
    analysis_page()
elif page == "รายงาน":
    report_page()
elif page == "Sentiment Analysis":
    sentiment_page()
elif page == "ตั้งค่า":
    setting_page()

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>Voice Analytics Dashboard | Call Center UX Analyzer</div>",
    unsafe_allow_html=True
)
