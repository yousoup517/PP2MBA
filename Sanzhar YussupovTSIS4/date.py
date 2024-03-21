#ex1
import datetime
current_date = datetime.datetime.now()
minus5days = current_date - datetime.timedelta(5)
print(minus5days)
#ex2
today = datetime.datetime.now()
yesterday = today- datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print("Yesterday was ", yesterday)
print("Today is ", today)
print("Tomorrow will be ", tomorrow)
#ex3
now = datetime.datetime.now().replace(microsecond=0)
print(now)
#ex4
date1 = datetime(2023, 5, 15, 12, 30, 0)  
date2 = datetime(2023, 5, 10, 8, 45, 0)   
minus = date1 - date2
diff = minus.total_seconds()
print(diff)
