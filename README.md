# 📈 Anomaly Detection in Stock Market Data (Streamlit Dashboard)

This project is a smart, interactive **Anomaly Detection Dashboard** that simulates stock behavior and highlights suspicious trends using **Machine Learning** (Isolation Forest). Built with **Streamlit**, this dashboard accepts Yahoo Finance URLs and sends real-time **email alerts** when anomalies are found.

---

## 🔧 Features

✅ Paste a Yahoo Finance URL to simulate monitoring  
✅ 30-second fake detection loader (for realism 😉)  
✅ Random anomaly simulation using Isolation Forest  
✅ Line chart with anomaly markers (📉 sudden drop, 📈 spike, etc.)  
✅ Anomaly summary table with type of anomaly  
✅ 📧 Email alert sent if anomalies are detected

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/anomaly-detection-dashboard.git
cd anomaly-detection-dashboard
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```
Or individually:
```bash
pip install streamlit pandas numpy matplotlib scikit-learn
```

### 3. Prepare the Dataset
Place the dataset `stock_market_dataset_50000_rows.csv` in the root directory. You can use the one provided or your own stock data.

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📧 Email Alerts Setup

This project supports Gmail-based email alerts using **App Passwords**.

1. Enable [2-Step Verification](https://myaccount.google.com/security)
2. Visit [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a 16-character app password
4. Replace placeholders in `app.py`:
```python
msg["From"] = "dummy.sender@gmail.com"
msg["To"] = "receiver@gmail.com"
server.login("dummy.sender@gmail.com", "your_app_password")
```

✅ Do **NOT** use your real Gmail password! Always use the App Password.

---

## 📸 Sample Dashboard Output
- Paste Yahoo link
- Wait 30 seconds
- View chart with red markers
- Read table of anomalies
- Receive email alert (if enabled)

---

## 📂 Project Structure
```
📁 anomaly-detection-dashboard
├── app.py                       # Streamlit dashboard
├── stock_market_dataset.csv    # Training data for Isolation Forest
├── README.md                   # You are here 👋
└── .streamlit/secrets.toml     # (Optional) for email credentials
```

---

## 🤝 Credits
Developed by [Your Name] as part of a machine learning project to detect anomalies in financial data using ML and simulation techniques.

---

## 📜 License
MIT License - Feel free to use and modify.

