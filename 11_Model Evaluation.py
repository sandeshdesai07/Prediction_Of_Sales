plt.figure(figsize=(18,8))
pd.DataFrame(models_results_R2, index=['']).plot.bar(color=colors2); #index=[''] delete the first row and name the models columnwise
plt.xlabel('R2 Score')

### **Model Evaluation By Root Mean Square Error**

plt.figure(figsize=(18,8))
pd.DataFrame(models_results_rmse, index=['']).plot.bar(color=colors2);
plt.xlabel('Root Mean Square Error');

X = raw_test.drop(['Order Date', 'order_month_year', 'Ship Date', 'ship_month_year'], axis=1)
for col in X.columns:
    if X[col].dtype == 'object':
        lb = LabelEncoder() # Shift + Tab
        X[col] = lb.fit_transform(X[col])

days = 50
y_pred = modelRFR.predict(X)[:days] #it slices the first 50 predictions from X
y_test = data.iloc[6994:6994+days].values
plot_forecasted_sales(y_train=y_test, y_pred=y_pred, period=days, title='Forecasting Best Performed Model (Random Forest Regression)')
