import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import numpy as np
import sys
import pickle



frame=pd.read_csv('tempData.csv')
le=preprocessing.LabelEncoder()
frame=frame.iloc[:,1:9]

model_list=frame.Model.to_numpy()
model_upper=[x.upper() for x in model_list]
le.fit(model_upper)

carModel=le.transform(model_upper)

make=preprocessing.LabelEncoder()

make_list=frame.Make.to_numpy()
make_upper=[x.upper() for x in make_list]
make.fit(make_upper)

carMake=make.transform(make_upper)

state_list=frame.State.to_numpy()
state_upper=[x.upper() for x in state_list]
state=preprocessing.LabelEncoder()

state.fit(state_upper)

carState=state.transform(state_upper)


col_Make=pd.DataFrame(carMake,columns=['Make'])

col_Model=pd.DataFrame(carModel,columns=['Model'])

col_State=pd.DataFrame(carState,columns=['State'])

col_Price=pd.DataFrame(frame.Price.to_numpy(),columns=['Price'])

col_Year=pd.DataFrame(frame.Year.to_numpy(),columns=['Year'])

col_Mileage=pd.DataFrame(frame.Mileage.to_numpy(),columns=['Mileage'])

col_City=pd.DataFrame(frame.City.to_numpy(),columns=['City'])

col_Vin=pd.DataFrame(frame.Vin.to_numpy(),columns=['Vin'])

resultFrame=pd.concat([col_Make,col_Model,col_State,col_Year,col_Mileage,col_Vin,col_City,col_Price],axis=1,sort=False)

from sklearn.ensemble import RandomForestRegressor
#regr = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=10)

#regr.fit(resultFrame.iloc[:,0:5],resultFrame.iloc[:,7])

filename = 'finalized_model.random_forest_model'
regr = pickle.load(open(filename, 'rb'))


price_drop={'ACURA':1500,
 'ALFA':1500,
 'AM':1500,
 'ASTON':2000,
 'AUDI':2500,
 'BENTLEY':2500,
 'BMW':2500,
 'BUICK':2500,
 'CADILLAC':2500,
 'CHEVROLET':2500,
 'CHRYSLER':2500,
 'DODGE':2500,
 'FERRARI':4000,
 'FIAT':3000,
 'FISKER':2500,
 'FORD':2800,
 'FREIGHTLINER':2500,
 'GENESIS':2000,
 'GEO':2000,
 'GMC':2500,
 'HONDA':2000,
 'HUMMER':2500,
 'HYUNDAI':2000,
 'INFINITI':2000,
 'ISUZU':2000,
 'JAGUAR':2000,
 'JEEP':2500,
 'KIA':2400,
 'LAMBORGHINI':3000,
 'LAND':3000,
 'LEXUS':2000,
 'LINCOLN':2500,
 'LOTUS':2300,
 'MASERATI':2700,
 'MAYBACH':2000,
 'MAZDA':2000,
 'MCLAREN':2300,
 'MERCEDES-BENZ':2300,
 'MERCURY':2300,
 'MINI':2500,
 'MITSUBISHI':2500,
 'NISSAN':2500,
 'OLDSMOBILE':2000,
 'PLYMOUTH':2000,
 'PONTIAC':2000,
 'PORSCHE':3000,
 'RAM':2500,
 'ROLLS-ROYCE':3500,
 'SAAB':3400,
 'SATURN':2600,
 'SCION':2300,
 'SMART':2300,
 'SUBARU':2000,
 'SUZUKI':2400,
 'TESLA':2000,
 'TOYOTA':2000,
 'VOLKSWAGEN':2400,
 'VOLVO':2500}

data1=[]

company=np.where(make.classes_==str(sys.argv[1]).upper())
data1.append(company[0][0])

car_m=np.where(le.classes_==str(sys.argv[2]).upper())
data1.append(car_m[0][0])

car_s=np.where(state.classes_==" "+str(sys.argv[3]).upper())
data1.append(car_s[0][0])

data1.append(int(sys.argv[4]))
data1.append(int(sys.argv[5]))
command=[]
command.append(data1)

#print(data1)
data=[[55,452,5,2006,100000]]
pp=regr.predict(command)-price_drop[make.classes_[data1[0]]]
#p.where(make.classes_=="TOYOTA")

print("Predicted Price is: ",str(pp[0]))
