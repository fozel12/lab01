import streamlit as st
import pandas as pd
import json

st.title("Swim Progress Tracker")
st.write("This app shows how different swimmers improved in their events over time.")

with open("swim_data.json") as json_file:
    swim_data = json.load(json_file)

swim_table = pd.DataFrame(swim_data)

swim_table["initial_time"] = swim_table["initial_time"] * 100
swim_table["latest_time"] = swim_table["latest_time"] * 100

chosen_name = st.selectbox("Choose a swimmer", swim_table["name"].unique())
chosen_swimmer = swim_table[swim_table["name"] == chosen_name].iloc[0]

st.subheader("Swimmer Info")
st.write("**Name:**", chosen_swimmer["name"])
st.write("**Age:**", chosen_swimmer["age"])
st.write("**Event:**", chosen_swimmer["event"])
st.write("**Initial Time:**", chosen_swimmer["initial_time"])
st.write("**Latest Time:**", chosen_swimmer["latest_time"])

st.subheader("Everyone's Progress")
st.bar_chart(swim_table.set_index("name")[["initial_time", "latest_time"]])

swim_table["improvement"] = ((swim_table["initial_time"] - swim_table["latest_time"]) / swim_table["initial_time"]) * 100

st.subheader("Improvement Percent by Swimmer")
st.bar_chart(swim_table.set_index("name")["improvement"])

st.subheader(f"{chosen_name}'s Progress Chart")
st.line_chart(pd.DataFrame({
    "Initial Time": [chosen_swimmer["initial_time"]],
    "Latest Time": [chosen_swimmer["latest_time"]]
}))
