import matplotlib.pyplot as plt

# Data values
years = ["2006", "2007", "2008", "2010"]
horsforthValues = [180, 190, 225, 225]
headinglyValues = [100, 92, 79, 83]
hydeValues = [720, 731, 721, 766]

# Plotting
plt.plot(years, horsforthValues, label="Horsforth Ward")
plt.plot(years, headinglyValues, label="Headingley Ward")
plt.plot(years, hydeValues, label="Hyde Park and Woodhouse Ward")

# Plotting settings
plt.title("Child Poverty in Leeds")
plt.ylabel("Number of Children")
plt.xlabel("Year")
plt.legend()

# Saving
plt.savefig("childPoverty.png", bbox_inches="tight", dpi=300)