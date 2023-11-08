from matplotlib import pyplot as plt


def plotFrequencyHistogram(datetimes, title, xLabel, yLabel, start=None, end=None, logScale=False, step=60):
    stepCount = int((max(datetimes) - min(datetimes)).total_seconds() / step)

    plt.figure(figsize=(12, 6))
    plt.hist(datetimes, bins=stepCount, edgecolor='black', alpha=0.7)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)

    if logScale:
        plt.yscale('log')

    if start or end:
        start = start or min(datetimes)
        end = end or max(datetimes)
        plt.xlim(start, end)

    plt.grid(True)
    plt.tight_layout()
    plt.show()
