import streamlit as st
import requests

st.title("Superstore ML Prediction")

st.header("Sales Prediction")

quantity = st.number_input("Quantity", min_value=1, value=1)
discount = st.number_input("Discount", min_value=0.0, max_value=1.0, value=0.0)
shipping_cost = st.number_input("Shipping Cost", min_value=0.0, value=10.0)

category = st.selectbox(
    "Category",
    ["Technology", "Furniture", "Office Supplies"]
)

sub_category = st.text_input("Sub-category", "Phones")
segment = st.selectbox(
    "Segment",
    ["Consumer", "Corporate", "Home Office"]
)

ship_mode = st.selectbox(
    "Ship Mode",
    ["Standard Class", "Second Class", "First Class", "Same Day"]
)

region = st.text_input("Region", "Central")
market = st.text_input("Market", "US")
delivery_days = st.number_input(
    "Delivery Days",
    min_value=0,
    value=4
)

sales = st.number_input(
    "Sales",
    min_value=0.0,
    value=100.0
)

if st.button("Predict"):

    data = {
        "quantity": quantity,
        "discount": discount,
        "shipping_cost": shipping_cost,
        "category": category,
        "sub_category": sub_category,
        "segment": segment,
        "ship_mode": ship_mode,
        "region": region,
        "market": market,
        "delivery_days": delivery_days,
        "sales": sales
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict/regression",
        json=data
    )

    result = response.json()

    st.success(
        f"Predicted Sales: ${result['predicted_sales']:.2f}"
    )