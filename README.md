FilterGenie: Smart Log Filtering Assistant

**FilterGenie** is a Streamlit-powered smart assistant designed to simplify the process of log filtering and visualization. Built for the Splunk Build-a-Thon 2025, this tool empowers users to analyze log files with the help of ML-driven filter suggestions, real-time simulated log streaming, and data visualization features.

---

# Features

* **ML-Based Filter Suggestions**: Predicts likely severity levels (INFO, ERROR, etc.) based on query history using a Random Forest classifier.
* **Manual Filtering**: Allows users to filter logs by severity levels and view only what matters.
* **Visual Analytics**: Dynamic bar chart (by severity) and line chart (logs over time).
* **Query History Tracking**: Automatically logs past filters for future model training.
* **CSV Export**: Save filtered logs for further reporting or audit.
* **Simulated Real-Time Logs**: App supports live log stream simulation.

---

 How to Run

 1. Clone the Repository


git clone https://github.com/pavani-projects548/FilterGenie.git
cd FilterGenie


 2. Install Requirements

pip install -r requirements.txt


3. Run the App


streamlit run log_dashboard.py


4. Simulate Log Streaming (Optional)

You can simulate real-time logs by appending new lines to `sample_logs.csv` while the app is running.

---

 Files in Repo

| File                | Description                                             |
| ------------------- | ------------------------------------------------------- |
| `log_dashboard.py`  | Main Streamlit app code                                 |
| `sample_logs.csv`   | Sample log data input                                   |
| `query_history.csv` | Auto-generated ML training data for severity suggestion |
| `requirements.txt`  | Python dependencies                                     |



 Project Zip

A zipped version of this project is available separately for submission.



 📌 Future Improvements

* Integration with live log APIs or Splunk Cloud
* Advanced filtering: regex, full-text search
* Role-based access and user session management
* NLP-based filter queries



👩‍💻 Developed By

**Pavani** for the Splunk Build-a-Thon 2025

GitHub: [pavani-projects548](https://github.com/pavani-projects548)

---

License

This project is shared under the MIT License. See `LICENSE` file for details.
