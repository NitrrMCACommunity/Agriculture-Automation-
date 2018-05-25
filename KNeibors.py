
# Module import statements:


import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd


# Import Dataset:


path ='Dataset\datasets.csv'
data=pd.read_csv(path)
data.replace('?',-99999,inplace=True)
data.columns=['CropType','cropDays','soilMoisture','temp','humidity','y']
print(data.head())


# Model Training and Testing part:


x=np.array(data.drop(['y'],1))
y=np.array(data['y'])
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
cls=neighbors.KNeighborsClassifier()
cls.fit(x_train,y_train)
accuracy=cls.score(x_test,y_test)
print(accuracy)


# Prediction for Ground Nuts (2):


example_pre=np.array([2,32,700,32,32])
example_pre=example_pre.reshape([1,-1])
prediction =cls.predict(example_pre)
if(prediction==1):
    print("Irrigation is required")
else:
    print("Irrigation is not required")

