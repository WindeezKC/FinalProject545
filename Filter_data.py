import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator


csv_file_path = "BTC-USD.csv"
#csv_file_path = "C:\\Users\\kella\\Desktop\\545\\Final Project\\BTC-USD.csv"
data = pd.read_csv(csv_file_path)
selected_data = data[['Date', 'Open', 'Close']]

Filterd_csv= "BTC_filtered.csv"
#Filterd_csv = "C:\\Users\\kella\\Desktop\\545\\Final Project\\BTC_filtered.csv"

selected_data.to_csv(Filterd_csv, index=False)
print(f"New CSV file with Date, Open, and Close prices has been created at {Filterd_csv}")

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
start_date = data['Date'].iloc[0]
end_date = data['Date'].iloc[-1]
#print the start and end date of BTC file

print(f"Start date: {start_date.strftime('%Y-%m-%d')}")
print(f"End date: {end_date.strftime('%Y-%m-%d')}")


data = pd.read_csv(Filterd_csv)
data ['Buy Open Sell Close - Profit'] = data['Close'] - data['Open'].round(2)
total_OPEN_CLOSE_profit = data['Buy Open Sell Close - Profit'].sum().round(2)

print(f"Buying at Open and selling at close profit {total_OPEN_CLOSE_profit}")




#save profit each day to file

Open_close_profit = "Open_close_profit.csv"
#Open_close_profit ="C:\\Users\\kella\\Desktop\\545\\Final Project\\Open_close_profit.csv"
data.to_csv(Open_close_profit, columns=['Date', 'Buy Open Sell Close - Profit'], index=False,float_format='%.2f')
#Buy Close sell Open
data ['Buy Close Sell Open - Profit'] = data['Open'] - data['Close'].round(2)
total_CLOSE_OPEN_profit = data['Buy Close Sell Open - Profit'].sum().round(2)
#save that to new CSV like we did with open,close

Close_open_profit = "Close_open_profit.csv"
#Close_open_profit ="C:\\Users\\kella\\Desktop\\545\\Final Project\\Close_open_profit.csv"
data.to_csv(Close_open_profit, columns=['Date', 'Buy Close Sell Open - Profit'], index=False,float_format='%.2f')
print(f"Buying at Close and selling at open profit {total_CLOSE_OPEN_profit}")
data['Date'] = pd.to_datetime(data['Date'])

#Graph the profit
data['Graph - Buy Open Sell Close'] = data['Buy Open Sell Close - Profit'].cumsum()


data['Graph - Buy Close Sell Open'] = data['Buy Close Sell Open - Profit'].cumsum()
#data_thinned = data.iloc[::365]
#split it by year
#show profit every 365 days to get a better looking graph
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Graph - Buy Open Sell Close'], label='Daily Profit', color='blue')
plt.plot(data['Date'], data['Graph - Buy Close Sell Open'], label='Daily Profit', color='red')





#Plot BTC graph

plt.title('Buying Open (Blue) vs Buying Close (Red) for Bitcoin')
plt.xlabel('Date')
plt.ylabel('Profit in USD')
plt.legend()
ax = plt.gca()

plt.xticks(rotation=45)
plt.tight_layout()



#Litecoin filtereing and to be graphed
ltc_csv = "LTC-USD.csv"
data = pd.read_csv(ltc_csv)
selected_data = data[['Date', 'Open', 'Close']]
ltc_filtered= "filtered-ltc.csv"
selected_data.to_csv(ltc_filtered, index=False)
print(f"LTC CSV file with Date, Open, and Close prices has been created at {ltc_filtered}")

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
start_date = data['Date'].iloc[0]
end_date = data['Date'].iloc[-1]
print(f"LTC Start date: {start_date.strftime('%Y-%m-%d')}")
print(f"LTC End date: {end_date.strftime('%Y-%m-%d')}")
data = pd.read_csv(ltc_filtered)
data ['Buy Open Sell Close - Profit'] = data['Close'] - data['Open'].round(2)
total_OPEN_CLOSE_profit = data['Buy Open Sell Close - Profit'].sum().round(2)
print(f"LTC: Buying at Open and selling at close profit {total_OPEN_CLOSE_profit}")
Open_close_profit_LTC = "Open_close_profit_LTC.csv"
#Open_close_profit ="C:\\Users\\kella\\Desktop\\545\\Final Project\\Open_close_profit.csv"
data.to_csv(Open_close_profit_LTC, columns=['Date', 'Buy Open Sell Close - Profit'], index=False,float_format='%.2f')
#Buy Close sell Open
data ['Buy Close Sell Open - Profit'] = data['Open'] - data['Close'].round(2)
total_CLOSE_OPEN_profit = data['Buy Close Sell Open - Profit'].sum().round(2)
#save that to new CSV like we did with open,close
Close_open_profit_LTC = "Close_open_profit_LTC.csv"
#Close_open_profit ="C:\\Users\\kella\\Desktop\\545\\Final Project\\Close_open_profit.csv"
data.to_csv(Close_open_profit_LTC, columns=['Date', 'Buy Close Sell Open - Profit'], index=False,float_format='%.2f')
print(f"Buying at Close and selling at open profit {total_CLOSE_OPEN_profit}")
data['Date'] = pd.to_datetime(data['Date'])
#Graph the profit
data['Graph - Buy Open Sell Close'] = data['Buy Open Sell Close - Profit'].cumsum()
data['Graph - Buy Close Sell Open'] = data['Buy Close Sell Open - Profit'].cumsum()
#data_thinned = data.iloc[::365]
#split it by year
#show profit every 365 days to get a better looking graph
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Graph - Buy Open Sell Close'], label='Daily Profit', color='green')
plt.plot(data['Date'], data['Graph - Buy Close Sell Open'], label='Daily Profit', color='orange')
plt.title('Buying Open LTC (Green) vs Buying Close (Orange) for Bitcoin')
plt.xlabel('Date')
plt.ylabel('Profit in USD')
plt.legend()
ax = plt.gca()

plt.xticks(rotation=45)
plt.tight_layout()





ETH_csv = "ETH-USD.csv"
data = pd.read_csv(ETH_csv)
selected_data = data[['Date', 'Open', 'Close']]
eth_filtered = "filtered-eth.csv"
selected_data.to_csv(eth_filtered,index=False)
print(f"ETH CSV File with Date, Open, Close prices has been created at {eth_filtered}")

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
start_date = data['Date'].iloc[0]
end_date = data['Date'].iloc[-1]
print(f"ETH Start date: {start_date.strftime('%Y-%m-%d')}")
print(f"ETH End date: {end_date.strftime('%Y-%m-%d')}")

data = pd.read_csv(eth_filtered)
data['Buy Open Sell Close - Profit'] = data['Close'] - data['Open'].round(2)
total_OPEN_CLOSE_profit = data['Buy Open Sell Close - Profit'].sum().round(2)


print(f"ETH: Buying at open adn Selling at close profit :{total_CLOSE_OPEN_profit}")
Open_close_profit_ETH = "Open_close_profit_ETH.csv"
#Open_close_profit ="C:\\Users\\kella\\Desktop\\545\\Final Project\\Open_close_profit.csv"
data.to_csv(Open_close_profit_ETH, columns=['Date', 'Buy Open Sell Close - Profit'], index=False,float_format='%.2f')
#Buy Close sell Open
data ['Buy Close Sell Open - Profit'] = data['Open'] - data['Close'].round(2)
total_CLOSE_OPEN_profit = data['Buy Close Sell Open - Profit'].sum().round(2)


close_open_profit_eth = "close_open_profit_eth.csv"
data.to_csv(close_open_profit_eth, columns=['Date', 'Buy Close Sell Open - Profit'], index=False,float_format='%.2f')


print(f"Buying at Close and selling at open profit {total_CLOSE_OPEN_profit}")

data['Date'] = pd.to_datetime(data['Date'])
data['Graph - Buy Open Sell Close'] = data['Buy Open Sell Close - Profit'].cumsum()
data['Graph - Buy Close Sell Open'] = data['Buy Close Sell Open - Profit'].cumsum()


plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Graph - Buy Open Sell Close'], label='Daily Profit', color='purple')
plt.plot(data['Date'], data['Graph - Buy Close Sell Open'], label='Daily Profit', color='cyan')
plt.title('Buying Open ETH (Purple) vs Buying Close (Cyan) for Bitcoin')
plt.xlabel('Date')
plt.ylabel('Profit in USD')
plt.legend()
ax = plt.gca()

plt.xticks(rotation=45)
plt.tight_layout()



#Graph the data
'''
plt.title('Buying Open (Blue) vs Buying Close (Red) for Bitcoin')
plt.xlabel('Date')
plt.ylabel('Profit in USD')
plt.legend()
ax = plt.gca()

plt.xticks(rotation=45)
plt.tight_layout()
'''
plt.show()




