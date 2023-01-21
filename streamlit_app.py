from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
import streamlit as st
import pandas as pd

# Sample data
data = {'alias': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'maths': [90, 80, 70, 60, 50],
        'coding': [85, 95, 75, 65, 55]}

df = pd.DataFrame(data)

# Create a function to plot the data
def plot_data(selected_alias):
    filtered_data = df[df['alias'].isin(selected_alias)]
    st.subheader("Maths")
    st.bar_chart(filtered_data[['alias','maths']]).format({'maths': ',.2f'})
    st.subheader("Coding")
    st.bar_chart(filtered_data[['alias','coding']]).format({'coding': ',.2f'})
    st.write("Hover over the bars to see the values.")

# Create a checkbox for selecting the alias
alias_checkbox = st.multiselect("Select alias", df['alias'].tolist())

# Show the chart
if alias_checkbox:
    plot_data(alias_checkbox)
else:
    st.write("Please select at least one alias.")




data1 = pd.read_csv("group2.csv")
color = st.radio('test bby',("blue", "green"))
if color == "green":
    st.write("this is green")


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
