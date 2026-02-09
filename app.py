import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Voice Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ GLOBAL STYLE ------------------
st.markdown("""
<style>
/* background */
.stApp {
    background: linear-gradient(180deg, #0f1115, #151a21);
    color: white;
}

/* sidebar */
section[data-testid="stSidebar"] {
    background-color: #1c2028;
}

/* sidebar title */
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* card */
.card {
    background: #232833;
    border-radius: 16px;
    padding: 20px;
    height: 120px;
}

/* feature card */
.feature {
    border-radius: 16px;
    padding: 20px;
    height: 170px;
}

/* footer */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 13px;
    color: white;
    opacity: 0.7;
    padding: 8px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("## 🎧 Voice Analytics")
    menu = st.radio(
        "เลือกหน้า:",
        ["หน้าหลัก", "ไฟล์เสียง", "อัดเสียง", "วิเคราะห์", "รายงาน", "Sentiment Analysis", "ตั้งค่า"]
    )

# ------------------ MAIN CONTENT ------------------
st.markdown("## 🎯 Voice Analytics Dashboard")
st.markdown("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

# ------------------ TOP CARDS ------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
        📁 ไฟล์เสียง<br>
        <h2>0</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        📊 การวิเคราะห์<br>
        <h2>0</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        ⭐ คะแนนเฉลี่ย<br>
        <h2>N/A</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
        ✅ สถานะ<br>
        <h2>พร้อมใช้งาน</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ------------------ FEATURE SECTION ------------------
st.markdown("### 📋 ฟีเจอร์หลัก")

f1, f2 = st.columns(2)
f3, f4 = st.columns(2)

with f1:
    st.markdown("""
    <div class="feature" style="background:#18384a">
        📂 <b>ไฟล์เสียง</b><br><br>
        • อัปโหลดไฟล์ WAV<br>
        • ดูรายการไฟล์ทั้งหมด<br>
        • เปิดไฟล์เสียง
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature" style="background:#1e3a2f">
        🎙️ <b>อัดเสียง</b><br><br>
        • สร้างไฟล์ทดสอบ<br>
        • อัดเสียงจริง<br>
        • บันทึกบทสนทนา
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature" style="background:#1f4d2f">
        📈 <b>วิเคราะห์</b><br><br>
        • วิเคราะห์คุณภาพเสียง<br>
        • ประเมิน Sentiment<br>
        • คำนวณ UX Score
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class="feature" style="background:#4a3b14">
        📄 <b>รายงาน</b><br><br>
        • สรุปผลการวิเคราะห์<br>
        • ส่งออก JSON<br>
        • ดูข้อมูลเชิงลึก
    </div>
    """, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
🖥️ Voice Analytics Dashboard | Call Center UX Analyzer
</div>
""", unsafe_allow_html=True)
