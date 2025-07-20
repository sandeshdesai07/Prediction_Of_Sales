data = pd.read_csv('/content/Superstore_data.csv', encoding= 'unicode_escape') #encoding = unicode_escape means to interpret the unicodes properly.
data.head(2) #show two rows of the data

#showing the all columns in dataframe
data.columns

#we will get some statistics by describe() function
data.describe()

#info() function gives us the information about total rows, dtype etc
data.info()

#changing date for mat form order and ship date
data['Ship Date'] = pd.to_datetime(data['Ship Date'],format='%m/%d/%Y')
data['Order Date'] = pd.to_datetime(data['Order Date'],format='%m/%d/%Y')

print('checking the changed datatype\n',data['Order Date'].dtype,data['Ship Date'].dtype)

#make columns year-month for order and ship
data.insert(loc=3,  column='order_month_year',value=data['Order Date'].dt.to_period('M'))
data.insert(loc=8, column='ship_month_year', value=data['Ship Date'].dt.to_period('M'))

#make separate columns for day, month and year
data.insert(loc=4, column='order_day', value=data['Order Date'].dt.day)
data.insert(loc=5, column='order_month', value=data['Order Date'].dt.month)
data.insert(loc=6, column='order_year', value=data['Order Date'].dt.year)

#making same columns for the ship column
data.insert(loc=7, column='ship_day', value = data['Ship Date'].dt.day)
data.insert(loc=8, column='ship_month', value= data['Ship Date'].dt.month)
data.insert(loc=9, column='ship_year', value=data['Ship Date'].dt.year)

data.head(2)

#the shape of the dataset is (rows x columns)
data.shape

#lets split the data manually
#70% train and 30% test
raw_train = data.iloc[:6995] #it will contain the all rows from 0 to 6995 and all columns
raw_test = data.iloc[6995:].drop(columns='Sales') #it will contains all the rows from 6995 to last row and all columns except Sale because it is our target variable

#lets copy this test and train into another variable so in any case data gone we will have backup
train_og = raw_train.copy()
test_og = raw_test.copy()


