import streamlit as st
from data_fetch import fetch_stock_data, fetch_fund_data
from indicators import compute_returns, compute_ma, compute_rsi, compute_macd, compute_bollinger, simple_ma_strategy
from visualize import visualize_candlestick, visualize_returns

st.title("国内股票/基金分析平台（AkShare版）")

asset_type = st.radio("资产类型", ["股票", "基金"])
symbol = st.text_input("输入代码 (股票示例: 600519, 基金示例: 161039)", value="600519")
start_date = st.date_input("开始日期")
end_date = st.date_input("结束日期")

if st.button("获取数据"):
    if asset_type == "股票":
        # 股票直接输入纯数字即可，内部会自动加 sh/sz
        df = fetch_stock_data(symbol, start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d"))
    else:
        df = fetch_fund_data(symbol, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

    df = compute_returns(df)
    df = compute_ma(df)
    df = compute_rsi(df)
    df = compute_macd(df)
    df = compute_bollinger(df)
    df = simple_ma_strategy(df)

    st.subheader("K线图")
    st.plotly_chart(visualize_candlestick(df))

    st.subheader("累计收益率")
    st.plotly_chart(visualize_returns(df))

    st.subheader("数据表")
    st.dataframe(df.tail(20))

    st.download_button(
        label="导出Excel",
        data=df.to_excel(index=True, engine='openpyxl'),
        file_name=f"{symbol}_analysis.xlsx")
