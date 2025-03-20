import streamlit as st
import os

# Get dynamic port for deployment
PORT = int(os.getenv("PORT", 8501))

# Set page configuration
st.set_page_config(page_title="AI Multi-Tool Suite", layout="wide")

# Sidebar Navigation
st.sidebar.image("https://i.imgur.com/3yFQlLk.png", use_column_width=True)  # Placeholder logo
st.sidebar.success("🎯 **Select a tool from the sidebar to get started!**")

# --- Main Title & Subtitle ---
st.title("🌟 AI Multi-Tool Suite")
st.markdown(
    "<h4 style='color:#4CAF50;'>Your AI-powered assistant for enhanced productivity 🚀</h4>",
    unsafe_allow_html=True,
)
st.write("Welcome to the AI-powered multipage application. Select a tool from the sidebar to begin.")

st.markdown("---")

# --- AI Tools Section ---
st.markdown("## 🌟 Available AI Tools")
st.write("Explore the powerful AI-driven applications available in this suite:")

# Define AI tools in a list for easy iteration
ai_tools = [
    ("💼 **Smart ATS (Resume Analyzer)**", [
        "📌 **Optimize your resume** for ATS.",
        "🔍 **Match your resume** with a Job Description to see keyword relevance.",
        "📊 **Get a match score & missing keyword analysis.**",
    ]),
    ("📄 **Invoice Extractor (AI Document Scanner)**", [
        "📜 **Extract key details** from invoice images.",
        "🔍 **AI-powered scanning** for faster processing.",
        "📂 **Supports JPG, PNG, PDF formats.**",
    ]),
    ("🎥 **YouTube Transcriber (AI Video Summarizer)**", [
        "🎙️ **Extract & summarize transcripts** from YouTube videos.",
        "📑 **Get detailed bullet-point summaries.**",
        "🚀 **Perfect for students, researchers, and professionals.**",
    ]),
    ("✂️ **Background Remover**", [
        "🖼️ **Remove image backgrounds instantly.**",
        "🎨 **Keep only the subject with high accuracy.**",
        "🌐 **Supports PNG, JPG, and more formats.**",
    ]),
    ("🍏 **Calorie Calculator (AI Image-Based)**", [
        "🍔 **Upload a food image and calculate its calories.**",
        "🧠 **AI-powered recognition for food items.**",
        "📈 **Get an accurate calorie count.**",
    ]),
    ("📚 **Chat with PDF (Multiple Files Support)**", [
        "🗂️ **Upload and analyze multiple PDFs at once.**",
        "💬 **Ask questions based on PDF content.**",
        "🧠 **Advanced AI provides relevant answers.**",
    ]),
    ("📊 **Data Explorer**", [
        "📈 **Upload datasets & visualize trends effortlessly.**",
        "🔍 **Generate AI-powered insights.**",
        "📊 **Supports CSV, Excel, and other formats.**",
    ]),
    ("🖼️ **Image Classifier**", [
        "🏷️ **Upload images & classify objects with AI.**",
        "🔍 **Recognizes multiple categories using deep learning.**",
        "🚀 **Get instant classification results.**",
    ]),
    ("😊 **Sentiment Analyzer**", [
        "💬 **Analyze text sentiment (positive, neutral, negative).**",
        "📊 **AI-powered insights for feedback & social media.**",
        "🚀 **Instant sentiment results with detailed breakdowns.**",
    ]),
]

# Loop through AI tools to display dynamically
for tool, details in ai_tools:
    st.markdown(f"### {tool}")
    for detail in details:
        st.markdown(f"- {detail}")
    st.markdown("---")

# --- How to Use Section ---
st.markdown("## 📌 How to Use This AI Suite")
st.markdown(
    """
    1. **Select a tool from the sidebar** 📌.  
    2. **Follow the on-screen instructions** for each AI tool.  
    3. **Upload necessary files** (PDFs, Images, etc.).  
    4. **Let AI process your input & generate insights** 🚀.  
    5. **Download or use the AI-generated results**.  
    """
)

st.markdown("---")

# --- Contact Section ---
st.markdown("### 📞 Need Help?")
st.markdown(
    """
    💬 **If you have any questions or need support, feel free to reach out:**  
    - 📧 **Email:** [vaishnavikalambate241@gmail.com](mailto:vaishnavikalambate241@gmail.com)  
    - 🛠️ **Check the FAQ section in the sidebar**  
    """
)

# Closing Remark
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #FF5733;'>Empowering You with AI 🚀</h4>", unsafe_allow_html=True)

# Auto-run the Streamlit app
if __name__ == "__main__":
    os.system(f"streamlit run AI_Multi-Tool_Suite.py --server.port {PORT} --server.address 0.0.0.0")
