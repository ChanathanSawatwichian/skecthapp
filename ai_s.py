import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("✏️ เปลี่ยนภาพเป็นลายเส้นด้วย AI")
st.write("อัปโหลดภาพ แล้วดูเวทมนตร์การแปลงเป็นภาพสเก็ตช์!")

uploaded_file = st.file_uploader("📸 เลือกภาพ", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    # แปลงภาพเป็น grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # กลับสีภาพ
    inv_gray = 220 - gray

    # เบลอเพื่อให้ขอบนุ่มขึ้น
    blur = cv2.GaussianBlur(inv_gray, (21, 21), sigmaX=0, sigmaY=0)

    # Invert อีกครั้งแล้ว blend เพื่อให้เหมือนลายเส้น
    sketch = cv2.divide(gray, 255 - blur, scale=256.0)

    # แสดงภาพก่อน–หลัง
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="ภาพต้นฉบับ", use_container_width=True)
    with col2:
        st.image(sketch, caption="ภาพลายเส้น", use_container_width=True)

    st.success("✅ เสร็จแล้ว! กดค้างที่ภาพเพื่อลงเครื่องได้เลย")

bg1="""
<style>
.stApp {
    background-color: #2e8b57;
    color: #ffffff;
}
</style>
"""

st.html(bg1)
