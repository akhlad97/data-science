import streamlit as st  # Import the Streamlit library

st.write('out side form')  # This text will be displayed immediately when the app loads

# Create a form with the key 'myform'
with st.form('myform '):  # Note: there is an extra space in the form key ('myform ') — it's fine but avoid trailing spaces
    st.write('in side form')  # This text is inside the form block
    number1 = st.slider('pick a number', 0, 25, 5)  # Create a slider input from 0 to 25 with default value 5
    color = st.selectbox('pick a color ', ['red', 'black', 'green', 'yellow', 'purple'])  # Create a dropdown to pick a color
    st.form_submit_button('submit my picks')  # A button that submits the form; required for form inputs to be processed

# These lines are **outside** the form, so they run immediately during every app rerun

st.write(number1)  # 
st.write(color)    # 
