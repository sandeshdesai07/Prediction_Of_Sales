#finding avg salary
raw_train.columns

monthly_sales = pd.DataFrame(raw_train.groupby('order_month_year')[['Quantity','Sales']].sum()).reset_index() #it will sum the all values for each unique value of the order_month_year
monthly_sales.head(3)

plt.figure(figsize=(10, 5)) #width and height
sns.barplot(x='order_month_year', y='Sales', data=monthly_sales,palette='Set2')
plt.xticks(rotation=90)
plt.show()

#top demanded product by category from data
most_demand_qty = pd.DataFrame(raw_train.groupby('Category')['Quantity'].sum().reset_index())
most_demand_qty.sort_values(by= 'Quantity', ascending=False, inplace=True)

plt.figure(figsize=(10,8)) #width x height
sns.barplot(data=most_demand_qty, x='Category', y='Quantity', palette='Set2')
plt.show()

raw_train['Ship Mode'].hist(legend=True)

