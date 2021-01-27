import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data["Date"])
data.sort_values("Date", inplace=True)
# When the data's order is incorrect.
# Store the data as a pandas type by `pd.to_datetime()`
# Sort date by the method sort_values()
# inplace=True : Modified and replaced the original object
# 直接修改原始物件，不建立新物件
# inplace=False: Modified and Created as the new object.
# 修改資料，創建並返回新的對象承載其修改結果

price_date =data['Date']
price_close = data['Close']
# price_open = data['Open']

plt.plot_date(price_date, price_close, linestyle="solid")
# plt.plot_date(price_date, price_open, linestyle="solid")
plt.gcf().autofmt_xdate()


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
