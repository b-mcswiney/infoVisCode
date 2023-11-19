import csv
import matplotlib.pyplot as plt

# dataList = []

# with open("/home/nano/Year3/infoVisCode/cwk1/new_population.csv", "r") as data_file:
#     reader = csv.reader(data_file)

#     for row in reader:
#         dataList.append([int(row[5]), row[1], row[3]])

# dataList.sort(reverse=True)

# count = 0

# while count < 20:
#     print(dataList[count])
#     count += 1

# data.sort(reverse=True)

data = {'Syrian Arab Rep. ': 6702910, 
        'Afghanistan ': 2594827, 
        'South Sudan ': 2188785, 
        'Myanmar ': 1103245,
        'Dem. Rep. of the Congo ': 840392,
        'Somalia ': 812356,
        'Sudan ': 787823,
        'Central African Rep. ':  642161,
        'Eritrea ': 524738,
        'Burundi ': 372951,
        'Nigeria ': 352960,
        'Iraq ': 333200,
        'Viet Nam ': 316728,
        'Rwanda ': 245781,
        'Colombia ': 189866,
        'Unknown  ': 184067,
        'China ': 175361,
        'Venezuela (Bolivarian Republic of) ': 171112,
        'Mali ': 164588,
        'Ethiopia ': 151426}

names = list(data.keys())
values = list(data.values())

xTicks = [0 ,1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]
xLabels = [0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]

plt.barh(names, values)


plt.title("Top 10 refugee populations in 2020 by country of origin")
plt.xlabel("Population of Refugees")
plt.ylabel("Country of origin")
plt.xticks(xLabels, xTicks)

plt.savefig("population.png", bbox_inches="tight")
