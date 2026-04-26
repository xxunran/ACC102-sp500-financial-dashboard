# S&P 500 Cross‑Industry Financial Ratio Dashboard

## 1. Problem & User
Individual investors and business students lack a quick, visual tool to compare key financial ratios across multiple companies. This dashboard solves that by providing an interactive interface to explore profitability, solvency, and efficiency trends for 32 representative S&P 500 firms.

## 2. Data
- **Source**: WRDS Compustat (annual fundamentals, 2015–2024)
- **Access date**: 25 April 2026
- **Key fields**: ticker, company name, year, ROE, profit margin, debt ratio, asset turnover, current ratio
- **Sample**: 32 companies covering all 11 GICS sectors (Technology, Financials, Healthcare, Consumer, Energy, Industrials, Materials, Real Estate, Utilities, Communication Services)

## 3. Methods
- **Data acquisition**: Batch SQL queries (10 tickers per batch) from WRDS Compustat.
- **Data cleaning**: Pandas – convert to numeric, drop missing key rows, fill missing equity with assets minus liabilities.
- **Ratio calculation**: ROE, profit margin, debt ratio, asset turnover, current ratio.
- **Dashboard**: Streamlit + Plotly Express for interactive line charts and data tables.

## 4. Key Findings
- **ROE**: Apple (AAPL) and Microsoft (MSFT) consistently show ROE above 30%.
- **Debt ratio**: Financial firms (e.g., JPM) have higher debt (~85%) than tech firms.
- **Profit margin**: Visa (V) exhibits >50% margin due to its asset‑light model.
- **Sector patterns**: Energy companies (XOM, CVX) show more volatile profitability.

## 5. How to run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sp500-financial-dashboard.git
   cd sp500-financial-dashboard
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
4. The browser will open at http://localhost:8501. Use the sidebar to select companies, ratios, and year range.

## 6. Product link / Demo
- **GitHub repository**: https://github.com/xxunran/ACC102-sp500-financial-dashboard
- **Demo video**:

## 7. Limitations & next steps
- **Limitations**: Only 32 companies (sector‑representative but not full S&P 500); annual data only (quarterly would be more timely); no cash flow or valuation ratios.
- **Next steps**: Expand to all 500 constituents; add industry average benchmarks; include free cash flow and P/E ratios; automate monthly data updates.



