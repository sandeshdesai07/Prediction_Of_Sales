#first lets check all the columns
raw_test.columns

raw_test.drop(columns=['Row ID','Order ID', 'Customer ID', 'Customer Name', 'Product ID', 'Product Name'], inplace=True)
raw_train.drop(columns=['Row ID','Order ID', 'Customer ID', 'Customer Name', 'Product ID', 'Product Name'], inplace=True)
raw_train.columns
