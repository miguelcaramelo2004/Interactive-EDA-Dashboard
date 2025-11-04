import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df_customer = pd.read_csv(
    '/Users/miguelcaramelo/Desktop/Data_Science/1_semestre/Data_Mining/Interactive-EDA-Dashboard/DM_AIAI_CustomerDB (1).csv',
    sep=','
)
df_customer.columns = df_customer.columns.str.strip()

st.set_page_config(page_title="Interactive EDA - Customer Attributes", layout="wide")
st.title("Interactive Customer EDA Dashboard")
st.markdown("Explore customer attributes interactively.")
st.markdown("---")
st.markdown("**Use sidebar filters to analyze specific customer groups.**")

# Sidebar filters
st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df_customer["Gender"].dropna().unique(),
    default=df_customer["Gender"].dropna().unique()
)

education = st.sidebar.multiselect(
    "Select Education Level:",
    options=df_customer["Education"].dropna().unique(),
    default=df_customer["Education"].dropna().unique()
)

marital = st.sidebar.multiselect(
    "Select Marital Status:",
    options=df_customer["Marital Status"].dropna().unique(),
    default=df_customer["Marital Status"].dropna().unique()
)

loyalty = st.sidebar.multiselect(
    "Select Loyalty Status:",
    options=df_customer["LoyaltyStatus"].dropna().unique(),
    default=df_customer["LoyaltyStatus"].dropna().unique()
)

enrollment = st.sidebar.multiselect(
    "Select Enrollment Type:",
    options=df_customer["EnrollmentType"].dropna().unique(),
    default=df_customer["EnrollmentType"].dropna().unique()
)

province_or_state = st.sidebar.multiselect(
    "Select Province or State:",
    options=df_customer["Province or State"].dropna().unique(),
    default=df_customer["Province or State"].dropna().unique()
)

# Apply filters
df_filtered = df_customer[
    (df_customer["Gender"].isin(gender)) &
    (df_customer["Education"].isin(education)) &
    (df_customer["Marital Status"].isin(marital)) & 
    (df_customer["LoyaltyStatus"].isin(loyalty)) & 
    (df_customer["EnrollmentType"].isin(enrollment)) &
    (df_customer["Province or State"].isin(province_or_state))
]

# Income distribution
st.subheader("Income Distribution by Education Level")
fig_income = px.box(
    df_filtered,
    x="Education",
    y="Income",
    color="Education",
    title="Income Distribution by Education Level"
)
st.plotly_chart(fig_income, use_container_width=True)

# CLV by Marital Status
st.subheader("Customer Lifetime Value by Marital Status")
fig_clv = px.box(
    df_filtered,
    x="Marital Status",
    y="Customer Lifetime Value",
    color="Marital Status",
    title="Customer Lifetime Value by Marital Status"
)
st.plotly_chart(fig_clv, use_container_width=True)

# CLV by Loyalty Status
st.subheader("Customer Lifetime Value by Loyalty Status")
fig_clv_ls = px.box(
    df_filtered,
    x="LoyaltyStatus",
    y="Customer Lifetime Value",
    color="LoyaltyStatus",
    title="Customer Lifetime Value by Loyalty Status"
)
st.plotly_chart(fig_clv_ls, use_container_width=True)

# Income vs CLV
st.subheader("Income vs. Lifetime Value")
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

st.subheader("Customers by Province/State")
province_counts = df_filtered["Province or State"].value_counts().reset_index()
province_counts.columns = ["Province or State", "Count"]

fig_province = px.bar(
    province_counts,
    x="Province or State",
    y="Count",
    color="Province or State",
    title="Number of Customers per Province/State"
)
st.plotly_chart(fig_province, use_container_width=True)


# Descriptive stats
st.subheader("Descriptive Statistics")
st.dataframe(df_filtered.describe(include='all').T)



