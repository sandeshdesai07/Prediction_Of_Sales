#importing label encoder
from sklearn.preprocessing import LabelEncoder
#dropping the columns which is not necessary for model
X = raw_train.drop(['Order Date', 'order_month_year', 'Ship Date', 'ship_month_year', 'Sales'], axis=1)
for column in X.columns:
  if X[column].dtype == 'object':
    label = LabelEncoder()
    X[column] = label.fit_transform(X[column])
y = raw_train.Sales

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
#creating empty dictionary for the Root Mean Square Error and R2
models_results_rmse = {}
models_results_R2 = {}

def evaluate(y_t, y_p, title):
  table = PrettyTable()
  table.field_names = ['Metric', 'Value'] #it means Table should have two columns namely Metric and Value
  rmse = mean_squared_error(y_t, y_p) #[Tells the function to return RMSE instead of MSE. Without this, you'd get MSE by default],	[Rounds the result to 4 decimal places].
  r2 = r2_score(y_t, y_p)

  #adding rows to the pretty table
  table.add_row(['RMSE',rmse])
  table.add_row(['R2 Score',r2])

  #storing performance on the rmse and r2 dictionaries
  models_results_rmse[title] = rmse
  models_results_R2[title] = r2

  print(table)

def plot_forecasted_sales(y_pred, y_train, y_true=[], period=5, title=''):
  #let's plot
  plt.figure(figsize=(20,8))
  plt.plot(y_train.tolist(), color=colors[0])
  plt.plot([None for i in y_train] + [x for x in y_pred], color= colors[2])

  if len(y_true) > 0:
        plt.plot([None for i in y_train] + [x for x in y_true], color=colors[1])
        plt.legend(['2014-2016 Acual SALES', '2017 Acual SALES', f'2017 Forecasted SALES \(RMSE = {mean_squared_error(y_true, y_pred, squared=False).round(1)}, R2 = {r2_score(y_true, y_pred).round(3)})'])
  else:
      plt.legend(['2014-2017 Actual SALES', '2018-2020 Forecasted SALES'])

 # set parameters
  plt.xticks(range(0, len(y_train) + len(y_pred), period), rotation=75)
  plt.xlabel('Week')
  plt.ylabel('Sales')
  plt.title(title)
  plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#creating object for linear regression
modelLR = LinearRegression()
modelLR.fit(x_train, y_train)
y_pred = modelLR.predict(x_test) #now model will predict the values for the given x_test dataset
evaluate(y_test, y_pred, title='Linear Regression') #we are passing the y_pred means values predicted by the model and the actual values i.e y_test and we will evaluate the model performance

#importing libraries
from sklearn.tree import DecisionTreeRegressor

#building model
modelDT = DecisionTreeRegressor(max_depth=3)

#training the model
modelDT.fit(x_train,y_train)

#predicting on new data
y_pred = modelDT.predict(x_test)

#evaluating models performance
evaluate(y_test, y_pred, title='Decision Regression')

**RandomForest model**

#importing library for random forest
from sklearn.ensemble import RandomForestRegressor

#creating the object
modelRFR = RandomForestRegressor(max_depth=10)
#training the model
modelRFR.fit(x_train, y_train)

y_pred = modelRFR.predict(x_test)

#lets evaluate the performance
evaluate(y_test, y_pred, title='Random Forest Regressor')

**Support Vector Machine**

#importing library
from sklearn.svm import SVR

#creating object
modelSVR = SVR()

#building model
modelSVR.fit(x_train, y_train)
y_pred = modelSVR.predict(x_test)

#evaluate the performance the model
evaluate(y_test, y_pred, title='Support Vector Machine')


**XGBoost**

#importing libraries
from xgboost import XGBRegressor

#creating object
modelXGB = XGBRegressor()
modelXGB.fit(x_train, y_train)
pred = modelXGB.predict(x_test)

evaluate(y_test, pred, title='XGBRegressor')



