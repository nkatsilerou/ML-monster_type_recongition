import pandas as pd
import csv




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
x = data.drop("type",axis=1)
y= data["type"]
print(data)


from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras import losses
model = Sequential()
#model.add(Dense(100, input_dim=6, activation="softmax"))
model.add(Dense(100, activation="sigmoid"))
model.add(Dense(2, activation="softmax"))

#sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error', optimizer='SGD', metrics=["accuracy"])

#model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x,y, epochs=150, batch_size=10)
_, accuracy = model.evaluate(x, y)
print("Model accuracy: %.2f"% (accuracy*100))
predictions = model.predict(x)
print([round(x[0]) for x in predictions])
#print([round(z)])