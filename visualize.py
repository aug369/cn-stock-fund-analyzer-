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
