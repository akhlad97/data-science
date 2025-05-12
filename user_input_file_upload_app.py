import streamlit as st 
import pandas as pd

st.title('streamlit text input')

name=st.text_input('enter your name')

age=st.slider('select your age ',0,100,25)
st.write(f'your age is {age}')
if name:
    st.write(f"hello: {name}")
    
    
options=['java','c','c++','python']
choice=st.selectbox('please select your favorite langauge ',options)
st.write(f'you selected {choice}')


upload_file=st.file_uploader('please choose your csv file' ,type='csv')

if upload_file is not None :
    df=pd.read_csv(upload_file)
    st.write(df)