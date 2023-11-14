import matplotlib.pyplot as plt


dataFem = [1072817,1703975,1129540,3786418,307986]
dataMasc = [1100676,1776515,1220468,4096717,293280]
ages = ["0 - 4","5 - 11","12 - 17","18 - 59","60"]

plt.scatter(ages, dataFem, label="Female", marker="x")
plt.scatter(ages, dataMasc, label="Male", marker=".")

xTicks = [0, 500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000]
xLabels = [0, 500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000]

plt.xlabel("Age of Refugees")
plt.ylabel("Number of Refugees")
plt.yticks(xLabels, xTicks)
plt.legend()

plt.savefig("demographics.png", bbox_inches="tight")
