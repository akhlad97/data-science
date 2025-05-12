import streamlit as st 

col1,col2=st.columns([1,3])
col1.title('Sum')

with st.form('addition'):
    a=st.number_input('a')
    b=st.number_input('b')
    
    submit=st.form_submit_button('add')
    
    if submit:
        col2.title(f'addtion of {a} and  {b}  is {a+b}')
        st.write(f'addtion of {a} and {b}  is  {a+b}')
        