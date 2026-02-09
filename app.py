import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Voice Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0f1115, #151a21);
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #1c2028;
}

.card {
    background: #232833;
    border-radius: 16px;
    padding: 20px;
    height: 120px;
}

.feature {
    border-radius: 16px;
    padding: 20px;
    height: 170px;
}

.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 13px;
    color: white;
    opacity: 0.7;
    padding: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🎧 Voice Analytics")

    page = st.radio(
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

# ---------------- PAGES ----------------
def dashboard():
    st.markdown("## 🎯 Voice Analytics Dashboard")
    st.markdown("ระบบวิเคราะห์คุณภาพการบริการ Call Center")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown('<div class="card">📁 ไฟล์เสียง<h2>0</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">📊 การวิเคราะห์<h2>0</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card">⭐ คะแนนเฉลี่ย<h2>N/A</h2></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="card">✅ สถานะ<h2>พร้อมใช้งาน</h2></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📋 ฟีเจอร์หลัก")

    f1, f2 = st.columns(2)
    f3, f4 = st.columns(2)

    with f1:
        st.markdown('<div class="feature" style="background:#18384a">📂 <b>ไฟล์เสียง</b><br><br>• อัปโหลด WAV<br>• ดูไฟล์ทั้งหมด</div>', unsafe_allow_html=True)
    with f2:
        st.markdown('<div class="feature" style="background:#1e3a2f">🎙️ <b>อัดเสียง</b><br><br>• อัดเสียงจริง<br>• บันทึกบทสนทนา</div>', unsafe_allow_html=True)
    with f3:
        st.markdown('<div class="feature" style="background:#1f4d2f">📈 <b>วิเคราะห์</b><br><br>• วิเคราะห์เสียง<br>• Sentiment</div>', unsafe_allow_html=True)
    with f4:
        st.markdown('<div class="feature" style="background:#4a3b14">📄 <b>รายงาน</b><br><br>• สรุปผล<br>• Export JSON</div>', unsafe_allow_html=True)


def file_page():
    st.markdown("## 📁 ไฟล์เสียง")
    st.info("หน้านี้เป็น UX Prototype สำหรับจัดการไฟล์เสียง")
    st.file_uploader("อัปโหลดไฟล์เสียง (WAV)", type=["wav"])
    st.table({"ชื่อไฟล์": ["call_001.wav", "call_002.wav"], "สถานะ": ["พร้อม", "วิเคราะห์แล้ว"]})


def record_page():
    st.markdown("## 🎙️ อัดเสียง")
    st.warning("โหมด Prototype (ยังไม่เชื่อม PyAudio)")
    st.button("เริ่มอัดเสียง")
    st.button("หยุดอัดเสียง")


def analysis_page():
    st.markdown("## 📊 วิเคราะห์เสียง")
    st.selectbox("เลือกไฟล์", ["call_001.wav", "call_002.wav"])
    st.button("เริ่มวิเคราะห์")
    st.success("ผลลัพธ์จะถูกแสดงตรงนี้ (Mock)")


def report_page():
    st.markdown("## 📄 รายงาน")
    st.metric("คะแนนเฉลี่ย", "8.45 / 10")
    st.download_button("Export JSON", data="{}", file_name="report.json")


def sentiment_page():
    st.markdown("## 😊 Sentiment Analysis")
    st.progress(70)
    st.write("Positive: 70% | Neutral: 20% | Negative: 10%")


def setting_page():
    st.markdown("## ⚙️ ตั้งค่า")
    st.checkbox("โหมด Dark")
    st.checkbox("เปิด Log ระบบ")


# ---------------- ROUTER ----------------
if page == "หน้าหลัก":
    dashboard()
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

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
🖥️ Voice Analytics Dashboard | Call Center UX Analyzer
</div>
""", unsafe_allow_html=True)
