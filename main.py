import streamlit as st
from data_fetch import fetch_stock_data, fetch_fund_data
from indicators import compute_returns, compute_ma, compute_rsi, compute_macd, compute_bollinger, simple_ma_strategy
from visualize import visualize_candlestick, visualize_returns, visualize_ma, visualize_rsi, visualize_macd, visualize_bollinger
from io import BytesIO

st.set_page_config(page_title="国内股票/基金分析平台", layout="wide")
st.title("国内股票/基金分析平台（AkShare版）")

# ---- 用户输入 ----
asset_type = st.radio("资产类型", ["股票", "基金"])
symbol = st.text_input("输入代码 (股票示例: 600519, 基金示例: 161039)", value="600519")
start_date = st.date_input("开始日期")
end_date = st.date_input("结束日期")

# ---- 获取数据 ----
if st.button("获取数据"):
    try:
        # 数据抓取
        if asset_type == "股票":
            df = fetch_stock_data(symbol, start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d"))
        else:
            df = fetch_fund_data(symbol, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

        # 技术指标计算
        df = compute_returns(df)
        df = compute_ma(df)
        df = compute_rsi(df)
        df = compute_macd(df)
        df = compute_bollinger(df)
        df = simple_ma_strategy(df)

        # 可视化
        st.subheader("K线图")
        st.plotly_chart(visualize_candlestick(df))

        st.subheader("累计收益率")
        st.plotly_chart(visualize_returns(df))

        st.subheader("均线图 (MA)")
        st.plotly_chart(visualize_ma(df))

        st.subheader("RSI 指标")
        st.plotly_chart(visualize_rsi(df))

        st.subheader("MACD 指标")
        st.plotly_chart(visualize_macd(df))

        st.subheader("布林带 (Bollinger Bands)")
        st.plotly_chart(visualize_bollinger(df))

        st.subheader("数据表（最近20条）")
        st.dataframe(df.tail(20))

        # 导出 Excel
        output = BytesIO()
        df.to_excel(output, index=True, engine='openpyxl')
        output.seek(0)

        st.download_button(
            label="导出 Excel 分析报告",
            data=output,
            file_name=f"{symbol}_analysis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"获取数据或计算指标出错: {e}")
