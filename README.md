# cn-stock-fund-analyzer-
Interactive stock and fund analysis platform for Chinese markets, built with Python, AkShare, and Streamlit. Supports data fetching, cleaning, technical indicators (MA, RSI, MACD, Bollinger Bands), simple strategy simulation, interactive Plotly charts, and Excel/CSV report export.

---

# 国内股票/基金分析平台（AkShare版）

一站式国内股票和基金分析平台：实现从数据抓取、清洗、指标计算、策略模拟到可视化展示和报告导出的一体化流程，帮助用户快速分析国内金融资产表现。

---

## 项目简介

本项目基于 Python、AkShare、Pandas、Plotly 和 Streamlit 构建，旨在为国内股票和基金投资者或量化爱好者提供一个简洁易用的数据分析平台。  
平台能够自动获取国内股票和开放式基金的日线数据，处理缺失值与异常数据，计算多种常用技术指标，并根据简单策略生成交易信号。同时提供交互式可视化图表和 Excel 报告导出功能，使数据分析过程直观且易于理解。

核心功能包括：  
- 自动抓取 A 股股票和基金的历史数据  
- 数据清洗与异常值处理  
- 日收益率、累计收益率、年化收益率计算  
- 常用技术指标计算：MA（移动平均线）、RSI（相对强弱指数）、MACD、布林带  
- 简单策略模拟：例如 MA 金叉/死叉买入卖出信号  
- 可视化图表：K 线图、累计收益率折线图  
- Excel 报告导出功能，支持后续数据分析或共享

---

## 功能特点

### 1. 数据抓取
- 使用 AkShare 免费接口获取国内股票和基金日线数据  
- 股票代码示例：`600519`（贵州茅台）、`000001`（平安银行）  
- 基金代码示例：`161039`（富国天惠成长混合）  
- 无需 Token，网络环境通畅即可获取数据  

### 2. 数据清洗
- 自动填充缺失值，保证计算指标时数据连续  
- 异常值处理：对开盘价、收盘价、最高价、最低价去极值  

### 3. 指标计算
- 日收益率、累计收益率、年化收益率  
- 移动平均线（MA）：短期、中期、长期均线  
- 相对强弱指数（RSI）：判断超买超卖状态  
- MACD：趋势和背离判断  
- 布林带（Bollinger Bands）：波动区间分析  

### 4. 策略模拟
- 基于 MA 的简单交易策略：短期均线上穿长期均线买入，反之卖出  
- 可扩展加入 RSI、MACD 等策略组合  

### 5. 可视化
- 交互式 K 线图（可缩放、悬浮提示）  
- 累计收益率折线图，可与多个资产对比  
- 数据表展示最近若干条数据，方便快速查看  

### 6. 报告导出
- 支持导出 Excel 报告，包含原始数据、计算指标、策略信号  
- 可直接用于后续分析或分享

---

## 安装依赖

```bash
git clone https://github.com/aug369/cn-stock-fund-analyzer-.git
cd cn-stock-fund-analyzer-
pip install -r requirements.txt
