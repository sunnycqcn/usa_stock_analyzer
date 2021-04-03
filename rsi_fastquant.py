
from fastquant import backtest, get_stock_data
df = get_stock_data("AAAA", "2018-01-01", "2021-04-01")
############smac######################
############RSI######################
res,plot = backtest('rsi', df, init_cash=2000, rsi_period=14, rsi_upper=70, rsi_lower=30, return_plot=True)
#plot.savefig('AAAA_rsi.png')
