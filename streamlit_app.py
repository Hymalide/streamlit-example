from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Project: Creating the best groups

This tool is meant to let you look for people with the qualities you are interested in in group-building and see caracteristic of the groups you create

This project is part of the course Information Visualization in KTH and uses anonymized data


"""
#import plotly.express as px

# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
#df = pd.DataFrame(
    #[["Product A", 5.6, 7.8, 5], ["Product B", 5.8, 7.2, 4.9]],
    #columns=["Product", "Comfort", "Sound", "Calls"]
#)

#fig = px.bar(df, x="Product", y=["Comfort", "Sound", "Calls"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
#st.plotly_chart(fig)


# Sample data
data = {'alias': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'maths': [9, 8, 7, 6, 5],
        'coding': [5, 9, 7, 6, 2]}

df = pd.DataFrame(data)

# Create a function to plot the data
def plot_bars(selected_alias):
    ploted_data = df[df['alias'].isin(selected_alias)]
    #create new ploted_data with sum and group by type
    # st.subheader("Maths")
    
    st.bar_chart(ploted_data[['maths','coding']].T)
    #st.subheader("Coding")
    #st.bar_chart(ploted_data[['coding']])
    st.write("Hover over the bars to see the values.")

        
def plot_comparison(checked_property):
        if checked_property:
                df_property = df[['alias']+checked_property].sort_values(by=checked_property[0], ascending=False).set_index('alias')
                compare_bar = st.bar_chart(df_property[checked_property])
        


        
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







