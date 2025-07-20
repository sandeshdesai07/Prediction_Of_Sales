raw_train.duplicated().value_counts() #whether the values of two rows are similar or not

raw_test.duplicated().value_counts()

raw_train.drop_duplicates(inplace=True)
raw_train.duplicated().value_counts()

