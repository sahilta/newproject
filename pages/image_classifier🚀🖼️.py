import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

# ✅ Move set_page_config to the first line!
st.set_page_config(page_title="Image Classifier", page_icon="📷", layout="centered")

# Load the MobileNetV2 model
@st.cache_resource
def load_model():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

model = load_model()

# Function to preprocess the image
def preprocess_image(image):
    if image.mode == 'RGBA':  # Convert RGBA to RGB
        image = image.convert('RGB')
    image = image.resize((224, 224))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to get prediction
def predict(image):
    processed_image = preprocess_image(image)
    preds = model.predict(processed_image)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]
    return decoded_preds

# Streamlit UI
st.title("🖼️ Image Classifier App")
st.markdown("**Upload an image and let the AI classify it using MobileNetV2!**")

# Information Section
st.subheader("📌 How It Works")
st.write("1. Upload an image")
st.write("2. Wait for classification")
st.write("3. View predictions with confidence scores")


# File uploader
uploaded_file = st.file_uploader("📂 Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_container_width=True)
    st.write("🔍 Classifying...")
    
    with st.spinner("🤖 AI is thinking..."):
        time.sleep(2)  # Simulate processing time
        predictions = predict(image)
    
    st.success("✅ Classification Complete!")
    
    # Display Predictions in a styled format
    st.subheader("📌 Top Predictions:")
    for pred in predictions:
        st.markdown(f"- **{pred[1]}**: {pred[2]*100:.2f}% confidence")
    
    # Additional feature: Confidence bar visualization
    st.subheader("📊 Confidence Levels")
    for pred in predictions:
        st.progress(float(pred[2]))
