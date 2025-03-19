import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import altair as alt

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    sentiment = "Positive" if scores['compound'] > 0 else "Negative" if scores['compound'] < 0 else "Neutral"
    return sentiment, scores

def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    sentiment = "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"
    return sentiment, blob.sentiment.polarity

def plot_sentiment(scores):
    labels = ['Positive', 'Neutral', 'Negative']
    values = [scores['pos'], scores['neu'], scores['neg']]
    
    fig, ax = plt.subplots()
    sns.barplot(x=labels, y=values, palette=["green", "gray", "red"], ax=ax)
    ax.set_title("Sentiment Distribution")
    ax.set_ylabel("Score")
    st.pyplot(fig)

def save_analysis_to_csv(text, vader_sentiment, vader_scores, blob_sentiment, blob_polarity):
    data = {
        "Text": [text],
        "VADER Sentiment": [vader_sentiment],
        "VADER Compound": [vader_scores['compound']],
        "TextBlob Sentiment": [blob_sentiment],
        "TextBlob Polarity": [blob_polarity]
    }
    df = pd.DataFrame(data)
    df.to_csv("sentiment_analysis.csv", index=False)
    return df

def show_sentiment_trend(text_list):
    data = []
    for text in text_list:
        sentiment, scores = analyze_sentiment_vader(text)
        data.append({"Text": text, "Compound Score": scores['compound']})
    df = pd.DataFrame(data)
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X("Text:N", title="Text Samples"),
        y=alt.Y("Compound Score:Q", title="Sentiment Score"),
        tooltip=["Text", "Compound Score"]
    ).properties(title="Sentiment Trend Over Multiple Texts")
    st.altair_chart(chart, use_container_width=True)

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis Tool", layout="wide")
st.title("📊 Sentiment Analysis Tool")
st.write("Analyze the sentiment of a given text using VADER and TextBlob with interactive visualizations and data export.")

# User Input
text_list = st.text_area("Enter multiple texts (one per line) for trend analysis:").split("\n")

if st.button("Analyze"):
    if text_list and any(text.strip() for text in text_list):
        st.subheader("📈 Sentiment Trend Analysis")
        show_sentiment_trend(text_list)
        
        for text in text_list:
            vader_sentiment, vader_scores = analyze_sentiment_vader(text)
            blob_sentiment, blob_polarity = analyze_sentiment_textblob(text)
            
            st.subheader(f"🔍 Sentiment Analysis for: {text[:50]}...")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**VADER Sentiment:** {vader_sentiment}")
                st.json(vader_scores)
                plot_sentiment(vader_scores)
            with col2:
                st.write(f"**TextBlob Sentiment:** {blob_sentiment}")
                st.write(f"**Polarity Score:** {blob_polarity:.2f}")
            
            # Save and Download Feature
            df = save_analysis_to_csv(text, vader_sentiment, vader_scores, blob_sentiment, blob_polarity)
            st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name=f"sentiment_analysis_{text_list.index(text)}.csv", mime="text/csv", key=f"download_{text_list.index(text)}")
    else:
        st.warning("Please enter some text to analyze.")
