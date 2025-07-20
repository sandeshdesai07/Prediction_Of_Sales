regions = raw_train['Region'].unique()
shipmodes = raw_train['Ship Mode'].unique()
categories = raw_train['Category'].unique()

plt.figure(5, figsize=(20, 6))
plt.subplots_adjust(wspace=0.1)

dfbyCatOrderDate = raw_train.groupby(['Category', 'Order Date'])
plt.subplot(131).title.set_text('Cumulative Number of Sales per Category')
plt.xticks(rotation=90)

for cat in categories:
  dt = dfbyCatOrderDate['Sales'].count()[cat]
  dt = dt.cumsum()
  sns.lineplot(data=dt, ax=plt.subplot(131))

dfbyShipOrderDate = raw_train.groupby(['Ship Mode','Order Date'])
plt.subplot(132).title.set_text('Cumulative Number of Sales per Ship Mode')
plt.xticks(rotation=90)
for shipMode in shipmodes:
    data = dfbyShipOrderDate['Sales'].count()[shipMode]
    data = data.cumsum()
    sns.lineplot(data=data, ax=plt.subplot(132))

#graphing 'Sales' vs. 'Region'
dfbyRegionOrderDate = raw_train.groupby(['Region','Order Date'])
plt.subplot(133).title.set_text('Cumulative Number of Sales per Region')
plt.xticks(rotation=90)
for region in regions:
    data = dfbyRegionOrderDate['Sales'].count()[region]
    data = data.cumsum()
    sns.lineplot(data=data, ax=plt.subplot(133))

plt.figure(7, figsize=(8,5))
dfByRegion = raw_train.groupby('Region')
dfByRegion['Sales'].sum().sort_values(ascending=False).plot(kind='bar')
plt.ylabel('Total Sales');
plt.title('Total Sales By Region');

plt.figure(8, figsize=(8,5))
dfByRegion['Profit'].mean().sort_values(ascending=False).plot(kind='bar');
plt.ylabel('Mean Profit');
plt.title('Mean Profit By Region');

dfByRegionSegment = raw_train.groupby(['Region', 'Segment'])

fig, axs = plt.subplots(2,2, sharey=True, sharex=True, figsize=(15,8))
axsIdx = [[0,0], [0,1], [1,0], [1,1]]
plt.subplots_adjust(wspace=0.32,hspace=0.25);

for idx, region in enumerate(regions):
    data = dfByRegionSegment['Profit'].sum()[region]
    axs[axsIdx[idx][0],axsIdx[idx][1]].bar(data.index, data.values)
    axs[axsIdx[idx][0],axsIdx[idx][1]].title.set_text(f"{region} Region")

plt.suptitle("Total Profit by Segment in each Region")
plt.show()

fig, axs = plt.subplots(2,2, sharey=True, sharex=True, figsize=(12,8))
axsIdx = [[0,0], [0,1], [1,0], [1,1]]
plt.subplots_adjust(wspace=0.32,hspace=0.25);

for idx, region in enumerate(regions):
    data = dfByRegionSegment['Profit'].mean()[region]
    axs[axsIdx[idx][0],axsIdx[idx][1]].bar(data.index, data.values)
    axs[axsIdx[idx][0],axsIdx[idx][1]].title.set_text(f"{region} Region")

plt.suptitle("Mean Profit by Region by Segment")
plt.show()

