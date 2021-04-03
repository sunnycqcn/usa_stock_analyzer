# Import pandas
import pandas as pd
#import time
#from datetime import datetime
#START_DATE = datetime(2018, 1, 1)   # Change here if you want to get old/new data.
#END_DATE = datetime.now()
# Import yfinance
import yfinance as yf
##STAR=2020-01-01
##END=2021-04-01
# Import data from yahoo finance
data = yf.download(tickers='AAAA', start="2019-01-01", end="2021-04-03")
# Drop the NaN values
data = data.dropna()
data.head()
######################
# Import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fast')
# Plot the closing price
plot = data.Close.plot(figsize=(10,5))
plt.grid()
plt.show()
plt.savefig('AAAA_macd.png')
###############################3
# Import talib
import talib
# Calculate parabolic sar
data['SAR'] = talib.SAR(data.High, data.Low, acceleration=0.02, maximum=0.2)
##############################
# Plot Parabolic SAR with close price
plot = data[['Close', 'SAR']][:500].plot(figsize=(10,5))
plt.grid()
plt.show()
plt.savefig('AAAA_SAR.png')
##########################################
# Calculate Tenkan-sen
high_9 = data.High.rolling(9).max()
low_9 = data.Low.rolling(9).min()
data['tenkan_sen_line'] = (high_9 + low_9) /2
# Calculate Kijun-sen
high_26 = data.High.rolling(26).max()
low_26 = data.Low.rolling(26).min()
data['kijun_sen_line'] = (high_26 + low_26) / 2
# Calculate Senkou Span A
data['senkou_spna_A'] = ((data.tenkan_sen_line + data.kijun_sen_line) / 2).shift(26)
# Calculate Senkou Span B
high_52 = data.High.rolling(52).max()
low_52 = data.High.rolling(52).min()
data['senkou_spna_B'] = ((high_52 + low_52) / 2).shift(26)
# Calculate Chikou Span B
data['chikou_span'] = data.Close.shift(-26)
# Plot closing price and parabolic SAR
komu_cloud = data[['Close','SAR']][:500].plot(figsize=(12, 7))
# Plot Komu cloud
komu_cloud.fill_between(data.index[:500], data.senkou_spna_A[:500], data.senkou_spna_B[:500],
 where=data.senkou_spna_A[:500] >= data.senkou_spna_B[:500], color='lightgreen')
komu_cloud.fill_between(data.index[:500], data.senkou_spna_A[:500], data.senkou_spna_B[:500],
 where=data.senkou_spna_A[:500] < data.senkou_spna_B[:500], color='lightcoral')
plt.grid()
plt.legend()
plt.savefig('AAAA_Komu.png')
##################buy singal##############3
data['signal'] = 0
data.loc[(data.Close > data.senkou_spna_A) & (data.Close > data.senkou_spna_B) & (data.Close > data.SAR), 'signal'] = 1

##################sell singal##############
data.loc[(data.Close < data.senkou_spna_A) & (data.Close < data.senkou_spna_B) & (data.Close < data.SAR), 'signal'] = -1
data['signal'].value_counts()
data.head()
data.to_csv(r'AAAA.csv')
############return test
# Calculate daily returns
daily_returns = data.Close.pct_change()
# Calculate strategy returns
strategy_returns = daily_returns *data['signal'].shift(1)
# Calculate cumulative returns
(strategy_returns+1).cumprod().plot(figsize=(10,5))
# Plot the strategy returns
plt.xlabel('Date')
plt.ylabel('Strategy Returns (%)')
plt.grid()
plt.savefig('AAAA_return.png')

