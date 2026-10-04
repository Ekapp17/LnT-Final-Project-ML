from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

regression_model = joblib.load(
    "../model/regression_model.joblib"
)

classification_model = joblib.load(
    "../model/classification_model.joblib"
)


class PredictionInput(BaseModel):
    quantity: int
    discount: float
    shipping_cost: float
    category: str
    sub_category: str
    segment: str
    ship_mode: str
    region: str
    market: str
    delivery_days: int
    sales: float = 0


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict/regression")
def predict_regression(data: PredictionInput):

    input_data = pd.DataFrame([{
        "quantity": data.quantity,
        "discount": data.discount,
        "shipping_cost": data.shipping_cost,
        "category": data.category,
       
    }])

    prediction = regression_model.predict(input_data)[0]

    return {
        "predicted_sales": float(prediction)
    }


@app.post("/predict/classification")
def predict_classification(data: PredictionInput):

    input_data = pd.DataFrame([{
        "quantity": data.quantity,
        "sales": data.sales,
        "discount": data.discount,
        "shipping_cost": data.shipping_cost,
        "category": data.category,

    }])

    prediction = classification_model.predict(input_data)[0]

    return {
        "profitable": bool(prediction)
    }