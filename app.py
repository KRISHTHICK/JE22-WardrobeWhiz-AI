# app.py
import streamlit as st
from PIL import Image
import os
from wardrobe_utils import categorize_clothing, combine_outfits
from agent_planner import ask_agent
from rag_helper import load_pdf_and_ask

st.set_page_config(page_title="WardrobeWhiz AI", layout="wide")
st.title("🧺 WardrobeWhiz AI - Smart Closet & Outfit Planner")

uploaded_imgs = st.file_uploader("📸 Upload Your Clothes (JPG/PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_imgs:
    st.subheader("🧾 Clothing Items Detected")
    for img_file in uploaded_imgs:
        img = Image.open(img_file)
        st.image(img, caption=img_file.name, width=150)
        category, color, season = categorize_clothing(img)
        st.markdown(f"**Type**: {category}, **Color**: {color}, **Season**: {season}")

    st.subheader("👕 Outfit Combiner")
    if st.button("Suggest Outfit Combination"):
        outfits = combine_outfits(uploaded_imgs)
        for i, combo in enumerate(outfits, 1):
            st.markdown(f"{i}. {combo}")

st.divider()
st.subheader("🧠 Ask the AI Fashion Agent")
q = st.text_input("E.g., What should I wear for a rainy evening dinner?")
if q:
    st.markdown(ask_agent(q))

st.divider()
st.subheader("📄 Upload Fashion Guides (PDF) for RAG")
pdf_docs = st.file_uploader("Upload Style PDFs", type=["pdf"], accept_multiple_files=True)
pdf_q = st.text_input("Ask about uploaded style documents")
if pdf_docs and pdf_q:
    rag_answer = load_pdf_and_ask(pdf_docs, pdf_q)
    st.markdown(rag_answer)
