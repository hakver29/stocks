from django.shortcuts import render

from .helpers import get_trade_data, get_daily_trades_data, get_daily_depths_data, get_distribution_plot, \
    get_daily_volume_plot, get_daily_price_plot, get_daily_orders_plot, get_daily_spread_plot
from .models import Stock
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go


# Create your views here.
def index(request):
    stocks = Stock.objects.all().order_by('id')
    context = {
        'stocks': stocks
    }
    return render(request, 'index.html', context)


def stock(request, ticker_id, **kwargs):
    stock_data = Stock.objects.all().filter(ticker_id=ticker_id).first()
    trades = get_trade_data(request, ticker_id)
    daily_depths = get_daily_depths_data(request, ticker_id)
    daily_trades = get_daily_trades_data(request, ticker_id)
    trades_list = [
        {
            'price': trade.price,
            'volume': trade.volume,
            'trade_timestamp': trade.trade_timestamp
        } for trade in trades
    ]
    daily_trades_list = [
        {
            'price': trade.price,
            'volume': trade.volume,
            'trade_timestamp': trade.trade_timestamp
        } for trade in daily_trades
    ]
    daily_depth_list = [
        {
            'ask1': depth.ask1,
            'bid1': depth.bid1,
            'ask_volume1': depth.ask_volume1,
            'ask_volume2': depth.ask_volume2,
            'ask_volume3': depth.ask_volume3,
            'ask_volume4': depth.ask_volume4,
            'ask_volume5': depth.ask_volume5,
            'bid_volume1': depth.bid_volume1,
            'bid_volume2': depth.bid_volume2,
            'bid_volume3': depth.bid_volume3,
            'bid_volume4': depth.bid_volume4,
            'bid_volume5': depth.bid_volume5,

            'ask_orders1': depth.ask_orders1,
            'ask_orders2': depth.ask_orders2,
            'ask_orders3': depth.ask_orders3,
            'ask_orders4': depth.ask_orders4,
            'ask_orders5': depth.ask_orders5,
            'bid_orders1': depth.bid_orders1,
            'bid_orders2': depth.bid_orders2,
            'bid_orders3': depth.bid_orders3,
            'bid_orders4': depth.bid_orders4,
            'bid_orders5': depth.bid_orders5,


            'tick_timestamp': depth.tick_timestamp
        } for depth in daily_depths
    ]

    distribution_plot = get_distribution_plot(stock_data, trades_list)
    daily_volume_plot = get_daily_volume_plot(stock_data, daily_depth_list, daily_trades_list)
    daily_orders_plot = get_daily_orders_plot(stock_data, daily_depth_list, daily_trades_list)
    daily_price_plot = get_daily_price_plot(stock_data, daily_depth_list, daily_trades_list)
    daily_spread_plot = get_daily_spread_plot(stock_data, daily_depth_list, daily_trades_list)

    context = {
        'distribution_plot': distribution_plot,
        'daily_volume_plot': daily_volume_plot,
        'daily_orders_plot': daily_orders_plot,
        'daily_price_plot': daily_price_plot,
        'daily_spread_plot': daily_spread_plot,
        'stock': stock_data,
        'trades': trades,
        'daily_trades': daily_trades
    }
    return render(request, 'stock.html', context)
