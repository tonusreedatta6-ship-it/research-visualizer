import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("📊 Research Landscape Visualizer")

uni = st.text_input("Enter University Name")

if st.button("Search"):

    res = requests.get(f"http://127.0.0.1:5000/search?university={uni}")
    data = res.json()

    if data["data"]:

        df = pd.DataFrame(
            list(data["data"].items()),
            columns=["Field", "Count"]
        )

        fig = px.bar(df, x="Field", y="Count",
                     title=f"Research Distribution - {uni}")
        st.plotly_chart(fig)

        fig2 = px.pie(df, names="Field", values="Count",
                      title=f"Research Share - {uni}")
        st.plotly_chart(fig2)

    else:
        st.warning("No data found")