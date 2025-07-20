plt.figure(10, figsize=(18, 4))
plt.subplots_adjust(wspace=0.2)
sns.histplot(data=raw_train[raw_train['Sales'] <= 2000], x='Sales', ax=plt.subplot(121), bins=10, kde=True, edgecolor='red');
sns.histplot(data=raw_train, x='Quantity', ax=plt.subplot(122), bins=10, kde=True, edgecolor='red');

plt.figure(11, figsize=(18, 4))
plt.subplots_adjust(wspace=0.2)
sns.histplot(data=raw_train, x='Discount', ax=plt.subplot(121), bins=10, kde=True, edgecolor='red');
sns.histplot(data=raw_train, x='Profit', ax=plt.subplot(122), bins=10, kde=True, edgecolor='red');

def data_transform(dataFrame):
    posData = dataFrame[dataFrame > 0]
    bcData, lam = stats.boxcox(posData)
    dataFrame[dataFrame > 0] = bcData
    dataFrame[dataFrame <= 0] = -1/lam
    return dataFrame
plt.figure(13, figsize=(18, 4))
plt.subplots_adjust(wspace=0.2)
sns.histplot(data=stats.boxcox(raw_train['Sales'])[0], ax=plt.subplot(121),bins=10, kde=True, edgecolor='red');
sns.histplot(data=stats.boxcox(raw_train['Quantity'])[0], ax=plt.subplot(122), bins=10, kde=True, edgecolor='red');

plt.figure(14, figsize=(18, 4))
plt.subplots_adjust(wspace=0.2)
sns.histplot(data=data_transform(raw_train['Discount'].copy()), ax=plt.subplot(121), bins=10, kde=True, edgecolor='red');
sns.histplot(data=data_transform(raw_train['Profit'].copy()), ax=plt.subplot(122), bins=10, kde=True, edgecolor='red');


