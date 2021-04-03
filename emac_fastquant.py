
from fastquant import backtest, get_stock_data
df = get_stock_data("AAAA", "2018-01-01", "2021-04-01")
res,plot = backtest('emac', df, init_cash=2000, fast_period=10, slow_period=30, return_plot=True)
#plot.savefig('AAAA_emac.png')
