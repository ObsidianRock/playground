from matplotlib import pyplot as plt
from collections import Counter

def plot():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title('norminal gdp')

    plt.ylabel('Billions of $')

    plt.show()

def bar():

    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
    plt.show()


def hist():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()],  histogram.values(), 8)
    plt.axis([-5, 105, 0, 5])

    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()


if __name__ == '__main__':

    hist()