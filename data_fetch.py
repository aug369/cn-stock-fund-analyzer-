# data_fetch.py
import akshare as ak
import pandas as pd
import numpy as np


def fetch_stock_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    获取 A 股日线数据，symbol 格式示例：600519 / 000001
    """
    # 自动判断交易所并拼接前缀
    if symbol.startswith('6'):
        full_symbol = 'sh' + symbol
    else:
        full_symbol = 'sz' + symbol

    # 获取数据
    df = ak.stock_zh_a_daily(symbol=full_symbol, start_date=start_date, end_date=end_date)

    # 检查列名
    expected_cols = ['date', 'open', 'high', 'low', 'close', 'volume']
    if not all(col in df.columns for col in expected_cols):
        raise ValueError(f"接口返回列名不符合预期: {df.columns}")

    # 只保留必要列并重命名
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
    df.rename(columns={'date': 'trade_date'}, inplace=True)

    # 日期处理
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df.sort_values('trade_date', inplace=True)
    df.set_index('trade_date', inplace=True)

    # 缺失值填充
    df = df.fillna(method='ffill').fillna(method='bfill')

    # 异常值处理（去极值）
    for col in ['open', 'high', 'low', 'close']:
        df[col] = df[col].clip(lower=df[col].quantile(0.01), upper=df[col].quantile(0.99))

    return df


def fetch_fund_data(fund_code: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    获取基金日净值，fund_code 示例：161039
    """
    df = ak.fund_open_fund_daily_em(fund=fund_code)

    # 新版列名
    if '净值日期' not in df.columns or '单位净值' not in df.columns:
        raise ValueError(f"基金接口返回列名不符合预期: {df.columns}")

    df = df[['净值日期', '单位净值']]
    df.rename(columns={'净值日期': 'trade_date', '单位净值': 'close'}, inplace=True)

    # 日期处理 & 筛选
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df = df[(df['trade_date'] >= pd.to_datetime(start_date)) & (df['trade_date'] <= pd.to_datetime(end_date))]
    df.sort_values('trade_date', inplace=True)
    df.set_index('trade_date', inplace=True)

    # 补齐其他列用于可视化
    df['open'] = df['close']
    df['high'] = df['close']
    df['low'] = df['close']
    df['volume'] = np.nan

    return df
