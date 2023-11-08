import csv


def readCsv(fileName, delimiter=","):
    data = []
    with open(fileName, mode='r') as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        for row in rows:
            data.append(dict(row))

    return data


def writeCsv(data, fileName, delimiter=","):
    fieldnames = data[0].keys()
    with open(fileName, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        for datum in data:
            writer.writerow(datum)
