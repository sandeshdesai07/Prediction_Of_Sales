#determining plotting ID and width and height
#if no ID previously given then it will create newone else take last one
plt.figure(1, figsize=(12, 9))
#determining the width and hight bw all plots
plt.subplots_adjust(wspace = 0.32, hspace = 0.25)

plt.subplot(221)
sns.countplot(data=raw_train, y='Ship Mode',orient='h');
plt.title("Number of items per Shipping mode");
plt.subplot(222)
sns.countplot(data=raw_train, y='Segment',orient='h');
plt.title('Number of items per Segment');
plt.subplot(223)
sns.countplot(data=raw_train, y='Category',orient='h');
plt.title('Number of items per Category');
plt.subplot(224)
sns.countplot(data=raw_train, y='Region',orient='h');
plt.title('Number of items per Region')

plt.figure(2, figsize=(17, 8))
plt.subplots_adjust(wspace=0.1);
#raw_train['Sales'] <= 2000] --> Fixing the Outliers (It is okay if you do not understand this)
#I am doing this so that we can see the visuals better. Do not do this randomly!
plt.subplot(221)
sns.kdeplot(data=raw_train[raw_train['Sales'] <= 2000], x='Sales');
plt.subplot(222)
sns.boxplot(data=raw_train[raw_train['Sales'] <= 2000], x='Sales',orient='h');

plt.figure(3, figsize=(15,8));
plt.subplots_adjust(wspace=0.1);

plt.subplot(221)
sns.kdeplot(data=raw_train, x='Quantity');

plt.subplot(222)
sns.boxplot(data=raw_train, x='Quantity');

plt.subplot(223)
sns.kdeplot(data=raw_train, x='Discount');

plt.subplot(224)
sns.boxplot(data=raw_train, x='Discount');

#profit
plt.figure(4, figsize=(17,8))
plt.subplots_adjust(wspace=0.1)

plt.subplot(221)
sns.kdeplot(data=raw_train[(raw_train.Profit <=2000)&(raw_train.Profit>=-20)], x='Profit')

plt.subplot(222)
sns.boxplot(data=raw_train[(raw_train.Profit <=2000)&(raw_train.Profit>=-20)], x='Profit')



