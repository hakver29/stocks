from datetime import datetime

from dashboard.models import Trade, Depth
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np


def get_trade_data(request, ticker_id):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date is None:
            start_date = '2022-01-01'
        if end_date is None:
            end_date = '2022-01-10'

        trades = Trade.objects.filter(data_id=ticker_id).filter(trade_timestamp__range=[start_date, end_date]).order_by('-trade_timestamp')
    else:
        trades = Trade.objects.filter(data_id=ticker_id).order_by('-trade_timestamp')

    return trades

def get_daily_depths_data(request, ticker_id):
    if request.method == 'GET':
        daily_date = request.GET.get('daily_date')
        intraday = request.GET.get('intraday')

        if daily_date is None:
            daily_date = datetime.today().strftime('%Y-%m-%d')

        if(intraday == 'on'):
            daily_depths = Depth.objects.filter(data_id=ticker_id).filter(tick_timestamp__date=daily_date).order_by('-tick_timestamp')
        else:
            daily_depths = Depth.objects.filter(data_id=ticker_id).filter(tick_timestamp__gte=daily_date).order_by(
                '-tick_timestamp')

        return daily_depths

def get_daily_trades_data(request, ticker_id):
    if request.method == 'GET':
        daily_date = request.GET.get('daily_date')
        intraday = request.GET.get('intraday')

        if daily_date is None:
            daily_date = datetime.today().strftime('%Y-%m-%d')

        if(intraday == 'on'):
            daily_trades = Trade.objects.filter(data_id=ticker_id).filter(trade_timestamp__date=daily_date).order_by('-trade_timestamp')
        else:
            daily_trades = Trade.objects.filter(data_id=ticker_id).filter(trade_timestamp__gte=daily_date).order_by(
                '-trade_timestamp')
        return daily_trades

def get_graphs(stock_data, trades_list):
    graphs = []
    if(len(trades_list) > 0):
        df = pd.DataFrame(trades_list)
        graphs.append(
            go.Bar(x=df['price'], y=df['volume'], name='Bar y3')
        )
        layout = {
            'title': 'Distribution plot for ' + str(stock_data.ticker),
            'xaxis_title': 'Price',
            'yaxis_title': 'Volume',
            'height': 600,
            'width': 1200,
        }
        plot_div = plot({'data': graphs, 'layout': layout},
                        output_type='div')


def get_distribution_plot(stock_data, trades_list):
    if (len(trades_list) > 0):
        df = pd.DataFrame(trades_list)

        graphs = []
        graphs.append(
            go.Bar(x=df['price'], y=df['volume'], name='Distribution plot')
        )
        layout = {
            'title': 'Distribution plot for ' + str(stock_data.ticker),
            'xaxis_title': 'Price',
            'yaxis_title': 'Volume',
            'height': 600,
            'width': 1200,
        }
        distribution_plot = plot({'data': graphs, 'layout': layout},
                        output_type='div')
        return distribution_plot

def get_daily_volume_plot(stock_data, daily_depth_list, daily_trades_list):
    if len(daily_depth_list) > 0:
        df_depths = pd.DataFrame(daily_depth_list)
        df_trades = pd.DataFrame(daily_trades_list)

        graphs = []

        ask_volume = df_depths['ask_volume1'] + df_depths['ask_volume2'] + df_depths['ask_volume3'] + df_depths['ask_volume4'] + df_depths['ask_volume5']
        bid_volume = df_depths['bid_volume1'] + df_depths['bid_volume2'] + df_depths['bid_volume3'] + df_depths[
            'bid_volume4'] + df_depths['bid_volume5']

        graphs.append(
            go.Line(x=df_trades['trade_timestamp'], y=df_trades['price'], name='Price')
        )
        graphs.append(
            go.Line(x=df_depths['tick_timestamp'], y=ask_volume-bid_volume, name='Buy - Sell volume', yaxis='y2')
        )

        layout = {
            'title': 'Order book plot for ' + str(stock_data.ticker),
            'height': 600,
            'width': 1200,
            'xaxis': {'title': 'Time', 'rangebreaks': [dict(bounds=["sat", "mon"]), dict(bounds=[16.5, 8.75], pattern="hour")]},
            'yaxis': {'title': 'Price'},
            'yaxis2': {
                'title': 'Net Volume',
                'titlefont': {'color': 'rgb(148, 103, 189)'},
                'tickfont': {'color': 'rgb(148, 103, 189)'},
                'overlaying': 'y',
                'side': 'right'
            }
        }
        daily_plot = plot({'data': graphs, 'layout': layout},
                          output_type='div')

        return daily_plot

def get_daily_orders_plot(stock_data, daily_depth_list, daily_trades_list):
    if len(daily_depth_list) > 0:
        df_depths = pd.DataFrame(daily_depth_list)
        df_trades = pd.DataFrame(daily_trades_list)

        graphs = []

        ask_orders = df_depths['ask_orders1'] + df_depths['ask_orders2'] + df_depths['ask_orders3'] + df_depths['ask_orders4'] + df_depths['ask_orders5']
        bid_orders = df_depths['bid_orders1'] + df_depths['bid_orders2'] + df_depths['bid_orders3'] + df_depths[
            'bid_orders4'] + df_depths['bid_orders5']
        graphs.append(
            go.Line(x=df_trades['trade_timestamp'], y=df_trades['price'], name='Price')
        )
        graphs.append(
            go.Line(x=df_depths['tick_timestamp'], y=bid_orders - ask_orders, name='Buy - Sell Orders', yaxis='y2')
        )
        layout = {
            'title': 'Net book plot for ' + str(stock_data.ticker),
            'height': 600,
            'width': 1200,
            'xaxis': {'title': 'Time', 'rangebreaks': [dict(bounds=["sat", "mon"]), dict(bounds=[16.5, 8.75], pattern="hour")]},
            'yaxis': {'title': 'Price'},
            'yaxis2': {
                'title': '#Orders',
                'titlefont': {'color': 'rgb(148, 103, 189)'},
                'tickfont': {'color': 'rgb(148, 103, 189)'},
                'overlaying': 'y',
                'side': 'right'
            },
        }
        daily_plot = plot({'data': graphs, 'layout': layout},
                          output_type='div')

        return daily_plot

def get_daily_price_plot(stock_data, daily_depth_list, daily_trade_list):
    if len(daily_trade_list) > 0:
        df_trade = pd.DataFrame(daily_trade_list)
        df_depth = pd.DataFrame(daily_depth_list)

        df_trade['clock'] = df_trade['trade_timestamp'].dt.strftime("%Y:%m:%d-%H:%M:%S")

        graphs = []

        graphs.append(
            go.Line(x=df_trade['trade_timestamp'], y=df_trade['price'], customdata=df_trade['volume'], hovertemplate='(price:%{y},volume:%{customdata})', name='Price')
        )
        graphs.append(
            go.Line(x=df_depth['tick_timestamp'], y=df_depth['ask1'], name='Ask')
        )
        graphs.append(
            go.Line(x=df_depth['tick_timestamp'], y=df_depth['bid1'],name='Bid')
        )
        graphs.append(
            go.Bar(x=df_trade['volume'], y=df_trade['price'], customdata=df_trade['clock'], hovertemplate='(volume:%{x}, price:%{y})<br>time: (%{customdata})', opacity=0.5, name='Distribution plot', xaxis='x2', orientation='h')
        )

        layout = {
            'title': 'Daily price plot for ' + str(stock_data.ticker),
            'yaxis': {'title': 'Price'},
            'xaxis': {'title': 'Time', 'rangebreaks': [dict(bounds=["sat", "mon"]), dict(bounds=[16.5, 8.75], pattern="hour")]},
            'xaxis2': {
                'title': 'Volume',
                'titlefont': {'color': 'rgb(148, 103, 189)'},
                'tickfont': {'color': 'rgb(148, 103, 189)'},
                'overlaying': 'x',
                'side': 'top'
            },
            'height': 800,
            'width': 1000,
        }

        daily_plot = plot({'data': graphs, 'layout': layout},
                          output_type='div')

        return daily_plot

def get_daily_spread_plot(stock_data, daily_depth_list, daily_trade_list):
    if len(daily_trade_list) > 0:
        df_trade = pd.DataFrame(daily_trade_list)
        df_depth = pd.DataFrame(daily_depth_list)

        graphs = []

        graphs.append(
            go.Line(x=df_trade['trade_timestamp'], y=df_trade['price'], name='Price')
        )
        graphs.append(
            go.Line(x=df_depth['tick_timestamp'], y=df_depth['ask1'] - df_depth['bid1'], name='Spread', yaxis='y2')
        )

        layout = {
            'title': 'Daily spread plot for ' + str(stock_data.ticker),
            'yaxis': {'title': 'Price'},
            'xaxis': {'title': 'Time', 'rangebreaks': [dict(bounds=["sat", "mon"]), dict(bounds=[16.5, 8.75], pattern="hour")]},
            'yaxis2': {
                'title': 'Spread (Ask - Bid)',
                'titlefont': {'color': 'rgb(148, 103, 189)'},
                'tickfont': {'color': 'rgb(148, 103, 189)'},
                'overlaying': 'y',
                'side': 'right'
            },
            'height': 800,
            'width': 1000,
        }

        daily_plot = plot({'data': graphs, 'layout': layout},
                          output_type='div')

        return daily_plot

def smoothTriangle(data, degree):
    triangle=np.concatenate((np.arange(degree + 1), np.arange(degree)[::-1])) # up then down
    smoothed=[]

    for i in range(degree, len(data) - degree * 2):
        point=data[i:i + len(triangle)] * triangle
        smoothed.append(np.sum(point)/np.sum(triangle))
    # Handle boundaries
    smoothed=[smoothed[0]]*int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed
