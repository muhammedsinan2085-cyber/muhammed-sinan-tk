import streamlit as st
st.title('CALCUTOR APP USING STREAMLIT')
st.write('---------------------')

num1 = st.number_input(label = 'Enter the first number')
num2 = st.number_input(label = 'Enter the second number')
operation = st.radio('Select the operation',('add','subtract','multiply','divide'))

ans = 0
def calculate():
  if operation == 'Add':
    ans = num1 + num2
  elif opeeration == 'subtract':
    ans = num1 - num2
  elif operation == 'multiply':
    ans = num1 * num2
  elif operation == 'divide':
    ans = num1/num2
  else:
    ans = 'not defined'
  st.success(f'answer ={ans}')

if st.button('calculate result'):
  calculate()
              
