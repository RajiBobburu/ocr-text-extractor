import streamlit as st
import numpy as np
from PIL import Image
import json

from utils.ocr_engine import load_reader
from utils.processor import extract_text, draw_boxes

st.set_page_config(
    page_title="OCR Text Extractor",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 OCR Text Extractor")
st.caption("Extract text from images using EasyOCR")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox("Language", ["en", "hi", "fr", "de", "es"])
    use_gpu = st.checkbox("Use GPU", value=False)
    min_conf = st.slider("Min Confidence (%)", 0, 100, 30)

# Upload
uploaded = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, use_container_width=True)

    img_array = np.array(image)

    with st.spinner("Processing OCR..."):
        reader = load_reader(language, use_gpu)
        results = reader.readtext(img_array)

        full_text, filtered, stats = extract_text(results, min_conf)
        boxed_image = draw_boxes(image.copy(), results, min_conf)

    if filtered:
        # Tabs
        tab1, tab2 = st.tabs(["📄 Text", "📦 Visualization"])

        with tab1:
            st.subheader("📄 Extracted Text")
            st.text_area("", full_text, height=250)

            st.code(full_text)

            st.write(f"Words: {stats['words']}")
            st.write(f"Characters: {stats['chars']}")
            st.write(f"Avg Confidence: {stats['avg_conf']}%")

            # Download TXT
            st.download_button(
                "⬇ Download Text",
                data=full_text,
                file_name="ocr_output.txt"
            )

            # Download JSON
            json_data = [
                {"text": text, "confidence": round(conf * 100, 2)}
                for _, text, conf in filtered
            ]

            st.download_button(
                "⬇ Download JSON",
                data=json.dumps(json_data, indent=2),
                file_name="ocr_output.json"
            )

            st.subheader("🔍 Detected Segments")
            for i, (bbox, text, conf) in enumerate(filtered):
                st.write(f"{i+1}. {text} ({round(conf*100,1)}%)")

        with tab2:
            st.subheader("📦 Detected Text Regions")
            st.image(boxed_image, use_container_width=True)

    else:
        st.warning("No text detected. Try lowering confidence.")