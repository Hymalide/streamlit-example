from collections import namedtuple
import altair as alt
import math
import pandas as pd
import plotly.express as px
import streamlit as st


"""
# Project: Creating the best groups

This tool is seperated in two parts: the first one allows you to look for people with the qualities you are interested in in group-building ordering alias depending on the first chosen skill. The second part allows you to create a group of 4 or 5 and to see the skills of the group.

This project is part of the course Information Visualization in KTH and uses anonymized data


"""
#



#DATAAAAAAA
df1 = pd.read_csv("data.csv")
df2 = pd.DataFrame(df1)
#st.dataframe(df2)

# Create a function to plot the data
def plot_bars(selected_alias):
    ploted_data = df2[df2['Alias'].isin(selected_alias)].set_index('Alias')
    tester=ploted_data[['Information Visualization','Statistics','Maths','Art','Computer usage','Programming','Computer Graphics','Human-Computer Interaction ','UX','Communication','Collaboration','Code Repository']]
    #create new ploted_data with sum and group by type
    # st.subheader("Maths")
    st.write('You can select/unselect skills by clicking on the name in the legend on the right')
    group_bar = px.bar(ploted_data, x= ['Information Visualization','Statistics','Maths','Art','Computer usage','Programming','Computer Graphics','Human-Computer Interaction ','UX','Communication','Collaboration','Code Repository'], height=400)
    st.plotly_chart(group_bar)
    st.write('Values for each skill for the selected Alias')
    test_bar = px.bar(tester.T)
    st.plotly_chart(test_bar)
    st.write('Addition of the values for each skill of all the selected Alias')
    st.write("Hover over the bars to see the values")

        
def plot_comparison(checked_property):
        if checked_property:
                limit = st.slider('Choose amount of alias in the chart', 5, 41, step=5)
                st.write('You can select/unselect skills by clicking on the name in the legend on the right')
                st.write('Other tools are available on the top right corner of the graph by hovering over with the mouse')
                df_property = df2[['Alias']+checked_property].sort_values(by=checked_property[0], ascending=False).set_index('Alias')
                compare_bar = px.bar(df2.sort_values(by=checked_property[0], ascending=False)[:limit], x ='Alias', y=checked_property, barmode='group', height=400)
                st.plotly_chart(compare_bar)
                #st.write('Values of each selected skills per Alias')
                st.write('Values of each selected skills per Alias')
                st.write("Hover over the bars to see the values")
        


        
#selection parts

st.title('Selecting skills to choose members of interest')

# Create a checkbox for selecting skills of inetrest
checked_property = st.multiselect("Choose a property of interest to show each student level up on 10, first skill selected will be used to order alias", [""]+df2.columns.tolist()[1:12])
st.write('The first selected skills will be used to rank Alias')

if checked_property:
        plot_comparison(checked_property)


# Create a checkbox for selecting the students of the group
st.title('Creating groups')
alias_checkbox = st.multiselect("Choose up to 5 members to check the group skills", df2['Alias'].tolist())

# Show the chart
if alias_checkbox:
    plot_bars(alias_checkbox)
else:
    st.write("Select at least one member")







