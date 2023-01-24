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
    #create new ploted_data with sum and group by type
    # st.subheader("Maths")
    
    st.bar_chart(ploted_data[['maths','coding']])
    #st.subheader("Coding")
    #st.bar_chart(ploted_data[['coding']])
    st.write("Hover over the bars to see the values.")

        
def plot_comparison(checked_property):
        if len(checked_property) == 1:
                df_property = df[['alias', checked_property[0]]].sort_values(by=checked_property[0], ascending=False)
                compare_bar = st.bar_chart("Level of student ranked by the level on the first property selected",df_property)
        


        
# Create a adio button widget to highlight a quality
checked_property = st.multiselect("Choose a property of interest to show each student level up on 10", [""]+df.columns.tolist()[1:])

if checked_property:
        plot_comparison(checked_property)


# Create a checkbox for selecting the students of the group
alias_checkbox = st.multiselect("Choose up to 5 members to check the group characteristics", df['alias'].tolist())

# Show the chart
if alias_checkbox:
    plot_bars(alias_checkbox)
else:
    st.write("Select at least one member")







