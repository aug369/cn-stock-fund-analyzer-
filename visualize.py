import plotly.graph_objects as go

def visualize_candlestick(df, title='K线图'):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])
    fig.update_layout(title=title, xaxis_rangeslider_visible=False)
    return fig

def visualize_returns(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['cum_return'], mode='lines', name='累计收益率'))
    fig.update_layout(title='累计收益率')
    return fig

def visualize_ma(df, ma_columns=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['close'], mode='lines', name='收盘价'))
    if ma_columns is None:
        ma_columns = [col for col in df.columns if col.startswith('MA')]
    for col in ma_columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
    fig.update_layout(title='均线图')
    return fig

def visualize_rsi(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI'))
    fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="超买", annotation_position="top right")
    fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="超卖", annotation_position="bottom right")
    fig.update_layout(title='RSI 指标')
    return fig

def visualize_macd(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='MACD'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Signal'], mode='lines', name='Signal'))
    fig.update_layout(title='MACD 指标')
    return fig

def visualize_bollinger(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['close'], mode='lines', name='收盘价'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Upper'], mode='lines', name='上轨', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=df.index, y=df['Lower'], mode='lines', name='下轨', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], mode='lines', name='中轨(MA20)', line=dict(color='orange')))
    fig.update_layout(title='布林带 (Bollinger Bands)')
    return fig
