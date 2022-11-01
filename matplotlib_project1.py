from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


plt.figure(figsize = (12,8))

ax1 = plt.subplot(1,2,1)

ax1.plot(range(len(months)),visits_per_month,marker = "o")

plt.xlabel("Months",labelpad=10)
plt.ylabel("Visits per Month",labelpad=15)
plt.title("Total page visits over the past year",y=1.025)

ax1.set_xticks(range(len(months)))
ax1.set_xticklabels(months)


ax2 = plt.subplot(1,2,2)

ax2.plot(range(len(months)),key_limes_per_month, color = "yellow")
ax2.plot(range(len(months)),persian_limes_per_month, color = "blue")
ax2.plot(range(len(months)),blood_limes_per_month, color = "red")

ax2.legend(["key_limes","persian_limes","blood_limes"],loc = "upper right")

ax2.set_xticks(range(len(months)))
ax2.set_xticklabels(months)

plt.xlabel("Months",labelpad=10)
plt.ylabel("Number of Lemon Sold",labelpad=15)
plt.title("Numbers of limes of different species sold each month",y=1.025)

plt.subplots_adjust(wspace = 0.35)

plt.savefig("my_plot.png")

plt.show()
