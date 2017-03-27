from matplotlib import pyplot as plt


def plot():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title('norminal gdp')

    plt.ylabel('Billions of $')

    plt.show()




if __name__ == '__main__':

    plot()