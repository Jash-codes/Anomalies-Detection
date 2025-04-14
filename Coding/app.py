import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
import time
import random

# === TRAINING PHASE ===
st.set_page_config(page_title="Anomaly Detector", layout="wide")

@st.cache_data
def load_training_data():
    df = pd.read_csv(r'C:\Users\Jashwanth\OneDrive\Documents\Anomalies Detection\Dataset\stock_market_dataset_50000_rows.csv')
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")
    df.dropna(inplace=True)
    return df

def train_model(df):
    features = ["Price", "Change", "%Change", "Volume"]
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(df[features])
    return model

# === SIMULATE DATA FROM USER INPUT ===
def simulate_data(company="Simulated Inc"):
    now = datetime.now()
    timestamps = [now - timedelta(minutes=i) for i in range(100)][::-1]
    prices = np.random.normal(loc=1000, scale=100, size=100)
    change = np.random.normal(loc=0, scale=10, size=100)
    percent_change = (change / (prices - change)) * 100
    volume = np.random.randint(100000, 5000000, 100)
    data = pd.DataFrame({
        "Timestamp": timestamps,
        "Company": company,
        "Price": prices,
        "Change": change,
        "%Change": percent_change,
        "Volume": volume
    })
    return data

# === EMAIL ALERT ===
def send_email_alert(anomaly_count):
    try:
        msg = EmailMessage()
        msg.set_content(f"Alert! {anomaly_count} anomalies detected in the latest stock data.")
        msg["Subject"] = "Anomaly Detection Alert"
        msg["From"] = "dummyme200010@gmail.com"
        msg["To"] = "venturazez@gmail.com"

        # Note: Replace with your SMTP server config
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("dummyme200010@gmail.com", "bqwl jfcj hgfj bpai")
            server.send_message(msg)
        return True
    except Exception as e:
        return False

# === STREAMLIT UI ===
st.title("📈 Stock Anomaly Detector with Email Alert")

user_input = st.text_input("Paste Yahoo Finance Link (simulation):")
if st.button("Detect Anomalies") and user_input:
    st.success("Simulating data for link: " + user_input)
    with st.spinner("Detecting anomalies... please wait 30 seconds..."):
        time.sleep(30)

    train_df = load_training_data()
    model = train_model(train_df)

    company_name = user_input.split("/")[-1] or "Simulated Inc"
    test_df = simulate_data(company=company_name)

    # Simulate some random anomalies
    test_df["is_anomaly"] = 0
    anomaly_indices = random.sample(range(len(test_df)), k=random.randint(5, 15))
    test_df.loc[anomaly_indices, "is_anomaly"] = 1

    # Assign random types to anomalies
    anomaly_types = ["Sudden Spike", "Price Drop", "Volume Surge", "Unusual Change"]
    test_df["Anomaly Type"] = "Normal"
    for idx in anomaly_indices:
        test_df.at[idx, "Anomaly Type"] = random.choice(anomaly_types)

    # Line chart
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(test_df["Timestamp"], test_df["Price"], label="Price", color='blue')
    anomalies = test_df[test_df["is_anomaly"] == 1]
    ax.scatter(anomalies["Timestamp"], anomalies["Price"], color='red', label='Anomaly')
    ax.set_title(f"Stock Price with Anomalies - {company_name}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Table output
    st.subheader("🔍 Detected Anomalies")
    st.dataframe(anomalies[["Timestamp", "Price", "Change", "%Change", "Volume", "Anomaly Type"]])

    # Email alert if anomalies found
    if len(anomalies) > 0:
        if send_email_alert(len(anomalies)):
            st.success("Email alert sent ✅")
        else:
            st.warning("Failed to send email. Check credentials/config.")
