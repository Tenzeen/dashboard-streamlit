import numpy as np
import pandas as pd
import streamlit as st

#load in data
df = pd.read_csv('https://data.cityofnewyork.us/resource/5ucz-vwe8.csv')

#remove all rows with (null) values in perp_race column
df.drop(index=df[df['perp_race'] == '(null)'].index, inplace=True)

#add title
st.title('NYPD Shooting Incidents')

#add header
st.header('Raw data')

#display raw data
st.write(df)

#display map of all shootings
st.header('Map of all shootings')
st.map(df)

#display raw data pertaining to number of shootings in each borough
st.header("# of Shootings in Each Borough")
boro_count = df['boro'].value_counts()
st.write(boro_count)

#display bar chart pertaining to number of shootings in each borough
st.subheader('Bar chart')
st.bar_chart(boro_count)

#change format of date to make the line chart look cleaner
df["occur_date"] = pd.to_datetime(df["occur_date"]).dt.strftime('%Y-%m-%U')
print(df)

#display raw data pertaining to number of shootings by date
st.header('# of Shootings by Date (year-month-week)')
shoot_date = df['occur_date'].value_counts()
st.write(shoot_date)

#display line chart pertaining to number of shootings by date
st.subheader('Line Chart')
st.line_chart(shoot_date)

#display the code to make the line chart
st.text('Code to make this line chart')
code = '''
        shoot_date = df['occur_date'].value_counts()
        st.line_chart(shoot_date)
        '''
st.code(code, language='python')