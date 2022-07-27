# logistic regression for multi-class classification using a one-vs-rest
from sklearn.linear_model import LinearRegression
from sklearn.multiclass import OneVsRestClassifier
import pandas as pd
import csv
# define dataset

def openTrain():
    file = open("train.csv")
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    train_rows = []
    for row in csv_reader:
        train_rows.append(row)
    file.close()
    return train_rows
#k = input("Enter k :")
def convertColorInTrain(rows):
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

    Ghoul = 0
    Goblin = 0.5
    Ghost = 1

    for i in rows:
        if i[6] == 'Ghoul':
            i[6] = Ghoul
        elif i[6] == 'Goblin':
            i[6] = Goblin
        elif i[6] == 'Ghost':
            i[6] = Ghost


rows = openTrain()
convertColorInTrain(rows)
file  = open("newTrain.csv",'w',newline='')
writer = csv.writer(file)
header = ['id','bone length','rotting flesh','hair length','has soul','color','type']
writer.writerow(header)
writer.writerows(rows)
file.close()
data = pd.read_csv('newTrain.csv')
X = data.drop("type",axis=1)
y= data["type"]
# define model
model = LinearRegression()
# define the ovr strategy
ovr = OneVsRestClassifier(model)
# fit model
ovr.fit(X, y)
# make predictions
yhat = ovr.predict(X)
print(yhat)