from math import sqrt
from math import pi
from math import exp
import csv
import pandas as pd
def openTest():
    file = open("test.csv")
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)
    file.close()
    return rows

def openTrain():
    file = open("train.csv")
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    train_rows = []
    for row in csv_reader:
        train_rows.append(row)
    file.close()
    return train_rows

def convertColorAndTypeInTrain(train_rows):
    white=0
    black= 0.2
    clear = 0.4
    blue = 0.6
    green = 0.8
    blood = 1

    for i in train_rows:
        if i[5] == "white":
            i[5]=white
        elif i[5] == "black":
            i[5]=black
        elif i[5] == "clear":
            i[5]=clear
        elif i[5] == "blue":
            i[5]=blue
        elif i[5] == "green":
            i[5]=green
        elif i[5] == "blood":
            i[5]=blood

    Ghoul = 0
    Goblin = 2
    Ghost = 1

    for i in train_rows:
        if i[6] == 'Ghoul':
            i[6] = Ghoul
        elif i[6] == 'Goblin':
            i[6] = Goblin
        elif i[6] == 'Ghost':
            i[6] = Ghost




rows = openTrain()
convertColorAndTypeInTrain(rows)
file  = open("newTrain.csv",'w',newline='')
writer = csv.writer(file)
header = ['id','bone length','rotting flesh','hair length','has soul','color','type']
writer.writerow(header)
writer.writerows(rows)
file.close()
file = open("newTrain.csv")
csv_reader = csv.reader(file)
header = next(csv_reader)
dataset = []
for row in csv_reader:
    dataset.append(row)
file.close()
dataset2 = []
for i in range(len(dataset)):
    color =dataset[i].pop(5)
    dataset2.append([dataset[i][0],color])
    dataset[i].pop(0)

for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        dataset[i][j] = float(dataset[i][j])

def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated







def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x - avg) ** 2 for x in numbers]) / float(len(numbers) - 1)
    return sqrt(variance)


def mean(numbers):
    return sum(numbers) / float(len(numbers))


def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries



# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries




def calculate_probability(x, mean, stdev):
    exponent = exp(-((x - mean) ** 2 / (2 * stdev ** 2)))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent


# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, count = class_summaries[i]
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities


summaries  = summarize_by_class(dataset)
probabilities = calculate_class_probabilities(summaries,dataset[0])
print(probabilities)
