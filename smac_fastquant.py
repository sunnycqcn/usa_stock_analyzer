
from fastquant import backtest, get_stock_data
df = get_stock_data("AAAA", "2018-03-01", "2021-04-01")
############smac######################
res,plot = backtest('smac', df, init_cash=2000, sell_prop=1, buy_prop=1,  fast_period=10, slow_period=30, return_plot=True)
#plot.savefig('AAAA_smac.png')
