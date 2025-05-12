import streamlit as st  # Import the Streamlit library

# Initialize 'sum' in session state if not already present
# ❌ This causes a bug: assigning '' (string) causes an AttributeError later
if 'sum' not in st.session_state:
    st.session_state.sum = ''  # ⚠️ should be 0.0 instead of ''

# Create two side-by-side columns
col1, col2 = st.columns(2)

# Display the label "Sum:" in the first column
col1.title('Sum:')

# If the stored sum is a float, display it in the second column formatted to 2 decimal places
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

# Create a form for input with the key 'addition'
with st.form('addition'):
    a = st.number_input('a')  # Input field for first number
    b = st.number_input('b')  # Input field for second number
    submit = st.form_submit_button('add')  # Button to submit the form

# Update the sum in session state with the sum of a and b
st.session_state.sum = a + b

# If form is submitted, force a rerun so that the updated sum is shown immediately
if submit:
    st.rerun()
