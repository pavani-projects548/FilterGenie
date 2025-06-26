import os
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(layout="wide")
st.title("🛠️ Smart Log Filtering Assistant")

# Load data
@st.cache_data
def load_logs():
    return pd.read_csv("sample_logs.csv")

@st.cache_data
def load_query_history():
    return pd.read_csv("query_history.csv") if os.path.exists("query_history.csv") else pd.DataFrame(columns=["level"])

# Load logs and query history
logs = load_logs()
query_history = load_query_history()

# Train ML model to suggest filter
le = LabelEncoder()
query_history["level_encoded"] = le.fit_transform(query_history["level"])
x = query_history.index.values.reshape(-1, 1)
y = query_history["level_encoded"]
model = RandomForestClassifier()
model.fit(x, y)
pred = model.predict([[len(query_history)]])
suggested_level = le.inverse_transform(pred)[0]

# Show ML suggestion
st.sidebar.markdown("📎 **ML-Suggested Filter**")
st.sidebar.write(f"Try filtering by: `:green[{suggested_level}]`")

# Manual Filter UI
st.sidebar.header("🔍 Manual Filters")
log_level = st.sidebar.multiselect("Select Severity Level", options=logs["level"].unique(), default=logs["level"].unique())
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime(logs["timestamp"]).min())
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime(logs["timestamp"]).max())

# Apply filters
filtered_logs = logs[
    (logs["level"].isin(log_level)) &
    (pd.to_datetime(logs["timestamp"]) >= pd.to_datetime(start_date)) &
    (pd.to_datetime(logs["timestamp"]) <= pd.to_datetime(end_date))
]

# Save to query history
# Save the current query to history
query_history = pd.read_csv("query_history.csv") if os.path.exists("query_history.csv") else pd.DataFrame(columns=["level"])
query_history = query_history._append({"level": ', '.join(log_level)}, ignore_index=True)
query_history.to_csv("query_history.csv", index=False)


# Display results
st.subheader("🔎 Filtered Log Results")
st.dataframe(filtered_logs)

# Chart 1: Bar Chart
st.subheader("📊 Log Count by Severity")
st.bar_chart(filtered_logs["level"].value_counts())

# Chart 2: Line Chart
st.subheader("📈 Logs Over Time")
logs_over_time = filtered_logs.groupby(pd.to_datetime(filtered_logs["timestamp"]).dt.date).size()
st.line_chart(logs_over_time)

# Sidebar: Show Query History (Last 5)
if os.path.exists("query_history.csv"):
    st.sidebar.markdown("🧠 **Past Queries**")
    history = pd.read_csv("query_history.csv")
    st.sidebar.table(history.tail(5))

# Export CSV
st.download_button("📁 Download as CSV", filtered_logs.to_csv(index=False), file_name="filtered_logs.csv", mime="text/csv")
st.subheader("🛰️ Real-Time Log Stream (Simulated)")

# Load simulated stream logs
if os.path.exists("stream_logs.csv"):
    stream_data = pd.read_csv("stream_logs.csv")

    # Show only the latest 5 entries (simulate streaming)
    latest_logs = stream_data.tail(5)

    st.dataframe(latest_logs)

    # Optional manual refresh button
    if st.button("🔄 Refresh Logs"):
        st.experimental_rerun()
else:
    st.warning("stream_logs.csv not found. Please add it to your project folder.")
