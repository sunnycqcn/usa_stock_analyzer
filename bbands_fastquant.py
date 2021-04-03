
from fastquant import backtest, get_stock_data
df = get_stock_data("AAAA", "2018-01-01", "2021-04-01")

res,plot = backtest('bbands', df, init_cash=2000, period=20, devfactor=2.0, return_plot=True)
#plot.savefig('AAAA_bbands.png')
