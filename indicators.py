import pandas as pd
import numpy as np

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    df['daily_return'] = df['close'].pct_change()
    df['cum_return'] = (1 + df['daily_return']).cumprod() - 1
    df['annual_return'] = df['daily_return'].mean() * 252
    return df

def compute_ma(df: pd.DataFrame, windows=[5,20,60]) -> pd.DataFrame:
    for w in windows:
        df[f'MA{w}'] = df['close'].rolling(w).mean()
    return df

def compute_rsi(df: pd.DataFrame, period=14) -> pd.DataFrame:
    delta = df['close'].diff()
    up, down = delta.clip(lower=0), -delta.clip(upper=0)
    roll_up = up.rolling(period).mean()
    roll_down = down.rolling(period).mean()
    rs = roll_up / roll_down
    df['RSI'] = 100 - 100 / (1 + rs)
    return df

def compute_macd(df: pd.DataFrame, short=12, long=26, signal=9) -> pd.DataFrame:
    df['EMA_short'] = df['close'].ewm(span=short, adjust=False).mean()
    df['EMA_long'] = df['close'].ewm(span=long, adjust=False).mean()
    df['MACD'] = df['EMA_short'] - df['EMA_long']
    df['Signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    return df

def compute_bollinger(df: pd.DataFrame, window=20, num_std=2) -> pd.DataFrame:
    df['MA20'] = df['close'].rolling(window).mean()
    df['STD20'] = df['close'].rolling(window).std()
    df['Upper'] = df['MA20'] + num_std*df['STD20']
    df['Lower'] = df['MA20'] - num_std*df['STD20']
    return df

def simple_ma_strategy(df: pd.DataFrame, short=5, long=20) -> pd.DataFrame:
    df['signal'] = 0
    df['signal'][short:] = np.where(df[f'MA{short}'][short:] > df[f'MA{long}'][short:], 1, 0)
    df['position'] = df['signal'].diff()
    return df
