import math
import csv
import random

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



def convertColorInTest(rows):
    white=0
    black= 0.2
    clear = 0.4
    blue = 0.6
    green = 0.8
    blood = 1

    for i in rows:
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
    Goblin = 0.5
    Ghost = 1

    for i in train_rows:
        if i[6] == 'Ghoul':
            i[6] = Ghoul
        elif i[6] == 'Goblin':
            i[6] = Goblin
        elif i[6] == 'Ghost':
            i[6] = Ghost


#calculate the euclidean distance
def euclidean_distance(row1,row2):
    distance=0.0
    for i in range(1, 6):
        distance += ((float(row1[i])) - float((row2[i]))) ** 2.0
    #print(distance)
    return math.sqrt(distance)


def calculateAccuracy(TP,TN,P,N):
    ACC = (TP+TN)/(P+N)
    return ACC

def calculateF1score(TP,FP,FN):
    Precision = TP/(TP+FP)
    Recall = (TP/(TP+FN))
    F1 = 2*((Precision*Recall)/(Precision+Recall))
    return F1



#locate the most similar neighbors
def get_neighbors(train,test_row,number_of_neighbors):
    distances = list()
    for train_row in train:
        dist=euclidean_distance(test_row,train_row)
        distances.append((train_row,dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors=list()
    for i in range(number_of_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


#prediction with neighbors
def predict_class(train,test_row,number_of_neighbors):
    neighbors = get_neighbors(train,test_row,number_of_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction




#KNN algorithm
def k_nearest_neighbors(train,test,number_of_neighbors):
    predictions=list()
    for row in test:
        output = predict_class(train,row,number_of_neighbors)
        predictions.append((row[0],output))
    return(predictions)

def convertToString(predictions):
    newlist = []
    for i in predictions:
        predictions2 = list(i)
        newlist.append(predictions2)
    for i in newlist:
        if i[1] == 0:
            i[1] = 'Ghoul'
        elif i[1] == 0.5:
            i[1] = 'Goblin'
        elif i[1] == 1:
            i[1] = 'Ghost'
    return newlist

def write_csv_with_results(filename,predictions):
    f=open(filename,'w', newline='')
    writer= csv.writer(f)
    header = ['id','type']
    writer.writerow(header)
    writer.writerows(predictions)
    f.close()


def RunKnnForK1():
    k=1
    rows = openTest()
    train_rows = openTrain()
    convertColorInTest(rows)
    convertColorAndTypeInTrain(train_rows)
    predictions = k_nearest_neighbors(train_rows,rows,int(k))
    predictions = convertToString(predictions)
    filename = 'predictions1.csv'
    print("k = ",k)
    for i in predictions:
        print(i)
    write_csv_with_results(filename,predictions)

def RunKnnForK3():
    k=3
    rows = openTest()
    train_rows = openTrain()
    convertColorInTest(rows)
    convertColorAndTypeInTrain(train_rows)
    predictions = k_nearest_neighbors(train_rows,rows,int(k))
    predictions = convertToString(predictions)
    filename = 'predictions3.csv'
    print("k = ",k)
    for i in predictions:
        print(i)
    write_csv_with_results(filename,predictions)

def RunKnnForK5():
    k=5
    rows = openTest()
    train_rows = openTrain()
    convertColorInTest(rows)
    convertColorAndTypeInTrain(train_rows)
    predictions = k_nearest_neighbors(train_rows,rows,int(k))
    predictions = convertToString(predictions)
    filename = 'predictions5.csv'
    print("k = ",k)
    for i in predictions:
        print(i)
    write_csv_with_results(filename,predictions)

def RunKnnForK7():
    k=7
    rows = openTest()
    train_rows = openTrain()
    convertColorInTest(rows)
    convertColorAndTypeInTrain(train_rows)
    predictions = k_nearest_neighbors(train_rows,rows,int(k))
    predictions = convertToString(predictions)
    filename = 'predictions7.csv'
    print("k = ",k)
    for i in predictions:
        print(i)
    write_csv_with_results(filename,predictions)

def RunKnnForK10():
    k=10
    rows = openTest()
    train_rows = openTrain()
    convertColorInTest(rows)
    convertColorAndTypeInTrain(train_rows)
    predictions = k_nearest_neighbors(train_rows,rows,int(k))
    predictions = convertToString(predictions)
    filename = 'predictions10.csv'
    print("k = ",k)
    for i in predictions:
        print(i)
    write_csv_with_results(filename,predictions)

RunKnnForK1()
RunKnnForK3()
RunKnnForK5()
RunKnnForK7()
RunKnnForK10()