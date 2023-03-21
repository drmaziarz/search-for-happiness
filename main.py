import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("happy.csv")
happiness = df["happiness"]
gdp = df["gdp"]
generosity = df["generosity"]
social_support = df["social_support"]
life_expectancy = df["life_expectancy"]

st.set_page_config(page_title="In Search for Happiness",
                   page_icon="😊",
                   layout="centered")

st.title("In Search for Happiness")
st.write("")

options = ["GDP", "Happiness", "Generosity", "Social Support", "Life Expectancy"]
x_axis = st.selectbox(label="Select the data for the X-axis",
                      options=options)

y_axis = st.selectbox(label="Select the data for the Y-axis",
                      options=options)

dictionary = {"GDP": gdp,
              "Happiness": happiness,
              "Generosity": generosity,
              "Social Support": social_support,
              "Life Expectancy": life_expectancy}

st.subheader(f"{x_axis} and {y_axis}")

figure = px.scatter(x=dictionary[x_axis], y=dictionary[y_axis], labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
