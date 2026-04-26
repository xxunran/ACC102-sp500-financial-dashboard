import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="S&P 500 Financial Analysis Tools", layout="wide")
st.title("📊 Analysis of Financial Ratios of Cross-Industry S&P 500 Companies")
st.markdown("**32 representative companies | 2015-2024** | Quickly compare the profitability, debt-paying ability and operational efficiency")

@st.cache_data
def load_data():
    df = pd.read_csv('sp500_32companies_ratios.csv')
    df['year'] = df['year'].astype(int)
    return df

df = load_data()

st.sidebar.header("⚙️ Filter Settings")
companies = sorted(df['ticker'].unique())
selected_tickers = st.sidebar.multiselect(
    "Select companies (multiple choices are allowed, and it is recommended to choose no more than 5)",
    options=companies,
    default=[companies[0]] if companies else []
)
if len(selected_tickers) > 5:
    st.sidebar.warning("More than 5 options have been selected. Only the top 5 options are displayed.")
    selected_tickers = selected_tickers[:5]

metrics = {
    "ROE": "roe",
    "Profit Margin": "profit_margin",
    "Debt Ratio": "debt_ratio",
    "Asset Turnover": "asset_turnover",
    "Current Ratio": "current_ratio"
}
selected_metrics = st.sidebar.multiselect(
    "Select financial indicators",
    options=list(metrics.keys()),
    default=["ROE", "Debt Ratio"]
)

years = sorted(df['year'].unique())
year_range = st.sidebar.slider(
    "Year range",
    min_value=min(years), max_value=max(years),
    value=(min(years), max(years)), step=1
)

filtered = df[df['ticker'].isin(selected_tickers)]
filtered = filtered[(filtered['year'] >= year_range[0]) & (filtered['year'] <= year_range[1])]

if filtered.empty:
    st.warning("No data available. Please adjust your selection.")
else:
    for metric_display in selected_metrics:
        metric_col = metrics[metric_display]
        plot_df = filtered[['ticker', 'year', metric_col]].dropna()
        if plot_df.empty:
            st.info(f"Indicator {metric_display} has no valid data")
            continue
        fig = px.line(plot_df, x='year', y=metric_col, color='ticker',
                      title=f"{metric_display} Trend Comparison",
                      labels={metric_col: metric_display, 'year': 'year', 'ticker': 'company'},
                      markers=True)
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"💡 {metric_display} The higher the better (the debt-to-asset ratio should be considered in conjunction with the industry) ")

    with st.expander("📋 View the detailed data table"):
        st.dataframe(filtered)

st.markdown("---")
st.caption("Data sources: WRDS Compustat (2015-2024) ")
