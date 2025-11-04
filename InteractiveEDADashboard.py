# # Importing Libraries

# In[2]:


# Remember: library imports are ALWAYS at the top of the script, no exceptions!



import streamlit as st
import pandas as pd
import plotly.express as px


#Loading the data

df_customer = pd.read_csv('/Users/miguelcaramelo/Desktop/Data_Science/1_semestre/Data_Mining/Interactive-EDA-Dashboard/DM_AIAI_CustomerDB (1).csv', sep = ',')





st.set_page_config(page_title="Interactive EDA - Customer Attributes", layout="wide")
st.title("👥 Interactive Customer EDA Dashboard")
st.markdown("Explore customer demographics, education, income, and loyalty behavior interactively.")

# -------------------------------
# 2️⃣ Sidebar filters
# -------------------------------
st.sidebar.header("🔍 Filters")

gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].dropna().unique(),
    default=df["Gender"].dropna().unique()
)

education = st.sidebar.multiselect(
    "Select Education Level:",
    options=df["Education"].dropna().unique(),
    default=df["Education"].dropna().unique()
)

marital = st.sidebar.multiselect(
    "Select Marital Status:",
    options=df["Marital Status"].dropna().unique(),
    default=df["Marital Status"].dropna().unique()
)

# Apply filters
df_filtered = df[
    (df["Gender"].isin(gender)) &
    (df["Education"].isin(education)) &
    (df["Marital Status"].isin(marital))
]

# -------------------------------
# 3️⃣ Main charts
# -------------------------------

# A. Income distribution
st.subheader("💰 Income Distribution by Education Level")
fig_income = px.box(
    df_filtered,
    x="Education",
    y="Income",
    color="Education",
    title="Income Distribution by Education Level"
)
st.plotly_chart(fig_income, use_container_width=True)

# B. Customer Lifetime Value by Marital Status
st.subheader("💎 Customer Lifetime Value by Marital Status")
fig_clv = px.box(
    df_filtered,
    x="Marital Status",
    y="Customer Lifetime Value",
    color="Marital Status",
    title="Customer Lifetime Value by Marital Status"
)
st.plotly_chart(fig_clv, use_container_width=True)

# C. Average income by gender
st.subheader("👫 Average Income by Gender")
avg_income = df_filtered.groupby("Gender")["Income"].mean().reset_index()
fig_gender_income = px.bar(
    avg_income,
    x="Gender", y="Income",
    color="Gender",
    title="Average Income per Gender"
)
st.plotly_chart(fig_gender_income, use_container_width=True)

# D. Education vs. CLV
st.subheader("📈 Education Level vs. Lifetime Value")
fig_edu_clv = px.scatter(
    df_filtered.dropna(subset=["Income", "Customer Lifetime Value"]),
    x="Income",
    y="Customer Lifetime Value",
    color="Education",
    size="Income",
    hover_data=["Marital Status", "Gender"],
    title="Income vs. Customer Lifetime Value by Education"
)
st.plotly_chart(fig_edu_clv, use_container_width=True)

# -------------------------------
# 4️⃣ Summary statistics
# -------------------------------
st.subheader("📊 Summary Statistics")
st.dataframe(df_filtered[["Latitude", "Longitude", "Income", "Customer Lifetime Value"]].describe().T)

st.markdown("---")
st.markdown("**Developed for exploratory analysis of customer attributes.** Use sidebar filters to focus on specific groups.")


