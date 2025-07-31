import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load dataset
file_path = "SampleLanguageData.csv"
df = pd.read_csv(file_path)

# Streamlit UI
st.title("Languages @ Union College")

df_m = pd.DataFrame(
    {
        "col1": np.random.randn(50) / 750 + 42.81829,
        "col2": np.random.randn(50) / 750 + -73.92685,
        "col3": np.random.randn(50) * 5,
        "col4": np.random.rand(50, 4).tolist(),
    }
)

#st.dataframe(df_m)

st.map(df_m, latitude="col1", longitude="col2", size="col3", color="col4")

# Country selection dropdown
selected_building = st.selectbox("Select a Building", df["Building"].dropna().unique())
# Filter data for the selected country
building_data = df[df["Building"] == selected_building]

# Line chart for happiness trend
st.subheader(f"Languages in {selected_building}")

st.dataframe(building_data, hide_index=True)


#fig_line = px.line(country_data, x="year", y="Happiness Score", markers=True, title=f"Happiness Score Trend for {selected_country}")
#st.plotly_chart(fig_line)

st.subheader(f"Percentage of Languages")

#langs = df["Language1"].dropna().unique()

langs = df["Language1"].value_counts()

#st.dataframe(langs)

fig = px.pie(langs, names=langs.index, values='count',title='Distribution of Languages')
st.plotly_chart(fig)


# Run the app
st.set_page_config(page_title="Languages @ Union College", layout="wide")