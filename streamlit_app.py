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
def plot_bars(selected_alias):
    ploted_data = df[df['alias'].isin(selected_alias)]
    st.subheader("Maths")
    st.bar_chart(ploted_data[['maths']]).format({'maths': ',.2f'})
    st.subheader("Coding")
    st.bar_chart(ploted_data[['coding']]).format({'coding': ',.2f'})
    st.write("Hover over the bars to see the values.")

        
def fusion_alias_property(list1, list2):
        #we will use only with list of same length, list2 = list of int
        n = len(list1)
        try:
                list2str = [str(int(list2[i])) for i in range(len)]


        return [list1[i]+' -> '+list2str[i] for i in range(n)]

def show_level(raw_alias):
        if checked_property:
                list_checked_property = df[checked_property].tolist()
                return fusion_alias_property(raw_alias, list_checked_property) # define list_checked_property
        else:
                return(raw_alias)
        
# Create a adio button widget to highlight a quality
checked_property = st.radio("Choose a property of interest to show each student level up on 10", df.columns.tolist()[1:])

# Create a checkbox for selecting the students of the group
alias_checkbox = st.multiselect("Choose up to 5 members to check the group characteristics", df['alias'].tolist(), format_func=show_level)

# Show the chart
if alias_checkbox:
    plot_bars(alias_checkbox)
else:
    st.write("Select at least one member")




data1 = pd.read_csv("group2.csv")
color = st.radio('test bby',("blue", "green"))
if color == "green":
    st.write("this is green")

