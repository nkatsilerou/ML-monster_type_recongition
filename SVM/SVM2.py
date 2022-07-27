from sklearn.preprocessing import MinMaxScaler
from sklearn import svm
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import csv

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
    Goblin = -1
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

i = 302
header1 = data[0:0]
test = data.iloc[i:]
train = data.iloc[:i]

test = header1.append(test)

Xtest = test.drop("type", axis=1)
ytest = test["type"]
Xtrain = train.drop("type", axis=1)
ytrain = train["type"]



print(Xtest)
print(ytest)
print(Xtrain)
print(ytrain)
print('#########################################################')



scaling = MinMaxScaler(feature_range=(-1,1)).fit(train_svm)
Xtrain = scaling.transform(Xtrain)
Xtest = scaling.transform(Xtest)

svc_lin = svm.SVC(kernel='linear')
svc_lin.fit(Xtrain,ytrain)

svc_gauss = svm.SVC(kernel='rbf')
svc_gauss.fit(Xtrain,ytrain)

lin_pred = svc_lin.predict(Xtest)
gaus_pred = svc_gauss.predict(Xtest)

accuracy_lin = metrics.accuracy_score(ytest, lin_pred)
f1_score_lin = metrics.f1_score(ytest,lin_pred, average='weighted')

accuracy_gaus = metrics.accuracy_score(ytest, gaus_pred)
f1_score_gaus = metrics.f1_score(ytest,gaus_pred, average='weighted')

print('Accuracy linear :', accuracy_lin)
print('f1 linear :', f1_score_lin)
print('Accuracy gauss :', accuracy_gaus)
print('f1 gauss :', f1_score_gaus)



