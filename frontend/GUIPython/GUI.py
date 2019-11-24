import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time
import operator

file_data = open("2_5391220104455259243", "r")
data = []
usage_times = {}
lastTime = None
try:
    while (True):
        new_data = file_data.readline()
        if new_data == "":
            break
        stemp = int(new_data.split()[0])
        app = new_data.split()[1]
        if lastTime is not None:
            t0 = dt.datetime.fromtimestamp(round(lastTime / 1))  # 1000
            t1 = dt.datetime.fromtimestamp(round(stemp / 1))  # 1000
            # current_time_utc = dt.datetime.utcnow()

            time_diff = (t1 - t0)
            print(time_diff)
            if app in usage_times:
                usage_times[app] += time_diff
            else:
                usage_times[app] = time_diff
        lastTime = stemp
        data.append(new_data)
except Exception as e:
    print("E: " + str(e))

# for d in data:
#     print(d)

# plt.plot(usage_times.keys(), usage_times.values())
# plt.plot(usage_times.keys(), [dt.datetime.fromtimestamp(ts) for ts in usage_times.values()])

sorted_x = sorted(usage_times.items(), key=operator.itemgetter(1))

# specify a date to use for the times
zero = dt.datetime(2018,1,1)
time = [zero + t for t in usage_times.values()]
# convert datetimes to numbers
zero = md.date2num(zero)
time = [t-zero for t in md.date2num(time)]

f = plt.figure()
ax = f.add_subplot(1,1,1)

ax.bar(usage_times.keys(), time, bottom=zero)
ax.yaxis_date()
ax.yaxis.set_major_formatter(md.DateFormatter("%H:%M"))

# add 10% margin on top (since ax.margins seems to not work here)
ylim = ax.get_ylim()
ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))


plt.show()

# n=20
# duration=1000
# now=time.mktime(time.localtime())
# timestamps=np.linspace(now,now+duration,n)
# dates=[dt.datetime.fromtimestamp(ts) for ts in timestamps]
# values=np.sin((timestamps-now)/duration*2*np.pi)
# plt.subplots_adjust(bottom=0.2)
# plt.xticks( rotation=25 )
# ax=plt.gca()
# xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
# ax.xaxis.set_major_formatter(xfmt)
# plt.plot(dates,values)
# plt.show()

