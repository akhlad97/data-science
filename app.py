import streamlit as st 
import pandas as pd 
import numpy as np 

st.title('Hello streamlit')

## display a simple text 
st.write('This is simple text')

df=pd.DataFrame(
    {
        'fisrt column':[1,2,3],
        'second column':[10,20,30]
    }
)

# display data frame 
st.write('here is dataframe')
st.write(df)

## create a line chart 
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)