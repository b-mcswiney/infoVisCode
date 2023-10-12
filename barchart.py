import matplotlib.pyplot as plt

# Names of data
years = ["2010", "2011"]
values = [[15.1, 25.2], [28.3, 30.0]]

x = [1.2, 2.4]
y = [0.8, 2.0]
notchCoords = [1.0, 2.2]

plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.bar(x, values[1], label="% women", width=0.4)
plt.bar(y, values[0], label="% male", width=0.4)

plt.ylabel("Percentage")
plt.xlabel("Year")
plt.xticks(notchCoords, years)
plt.ylim(0, 40)
plt.legend()

plt.subplot(132)
plt.scatter(x, values[1], label="% women")
plt.scatter(y, values[0], label="% men")
plt.xticks(notchCoords, years)
plt.ylabel("Percentage")
plt.xlabel("Year")
plt.ylim(0, 40)
plt.legend()

plt.savefig("barchart.png", bbox_inches="tight", dpi=300)
