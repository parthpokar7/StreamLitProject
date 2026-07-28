from sklearn.linear_model import LinearRegression
import joblib
import data as dt

data = dt.getData()

X = data[["Ads"]]
y = data["Sales"]

model = LinearRegression()
model.fit(X,y)

joblib.dump(model, "LinearRegression.pkl")