import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time
import operator

# file_data = open("2_5391220104455259243", "r")
# file_data = open("2_5391220104455264892", "r")

def fetch_data(file_name):
    data = []
    usage_time_dates = {}
    # usage_
    lastTime = None
    try:
        file_data = open(file_name)
        while True:
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
                # print(time_diff)
                if app in usage_time_dates:
                    usage_time_dates[app] += time_diff
                else:
                    usage_time_dates[app] = time_diff
            lastTime = stemp
            data.append(new_data)
    except Exception as e:
        print("E: " + str(e))

    # usage_time_dates = sorted(usage_time_dates.items(), key=operator.itemgetter(1))
    usage_times = [ts.total_seconds() for ts in usage_time_dates.values()]

    categories = {
        "Social Media": ["telegram-desktop", "Discord"],
        "Work": ["code", "java", "st"]
    }
    category_time_dates = {}
    for k in usage_time_dates.keys():
        isOther = True
        for c in categories.keys():
            if k in categories[c]:
                if c in category_time_dates.keys():
                    category_time_dates[c] += usage_time_dates[k]
                else:
                    category_time_dates[c] = usage_time_dates[k]
                isOther = False
        if isOther:
            if "Other" in category_time_dates.keys():
                category_time_dates["Other"] += usage_time_dates[k]
            else:
                category_time_dates["Other"] = usage_time_dates[k]

    # category_times = [ts.total_seconds() for ts in usage_time_dates.values()]

    return usage_time_dates, usage_times, category_time_dates

def plot_graph(dictionary):
    # specify a date to use for the times
    zero = dt.datetime(2018,1,1)
    times = [zero + t for t in dictionary.values()]
    # convert datetimes to numbers
    zero = md.date2num(zero)
    times = [t-zero for t in md.date2num(times)]

    f = plt.figure()
    ax = f.add_subplot(1,1,1)

    ax.bar(dictionary.keys(), times, bottom=zero)
    ax.yaxis_date()
    ax.yaxis.set_major_formatter(md.DateFormatter("%H:%M"))

    # add 10% margin on top (since ax.margins seems to not work here)
    ylim = ax.get_ylim()
    ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))

while True:
    print("Plot the data you want to see")
    print("apps (--pie) (--yesterday)              Show how long different apps have been opened")
    print("categories (--pie) (--yesterday)       Show how long different categegories have been opened")
    inp = input("")
    if "--yesterday" in inp:
        usage_time_dates, usage_times, category_time_dates = fetch_data("2_5391220104455264892")
    else:
        usage_time_dates, usage_times, category_time_dates = fetch_data("2_5391220104455264892newFake")

    if inp == "apps" or inp == "apps --yesterday":
        plot_graph(usage_time_dates)
    elif inp == "apps --pie" or inp == "apps --pie --yesterday":
        plt.pie(usage_times, labels=usage_time_dates.keys())
    elif inp == "categories" or inp == "categories --yesterday":
        plot_graph(category_time_dates)
    elif inp == "categories --pie" or inp == "categories --pie --yesterday":
        plt.pie([x.total_seconds() for x in category_time_dates.values()], labels=category_time_dates.keys())
    elif inp == "exit":
        exit()
    else:
        print("Unknown command ", inp, ", exiting...")
        exit()

    plt.show()
