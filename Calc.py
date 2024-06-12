import streamlit as st

st.title("CALCULATOR")
st.markdown("Welcome TO My first Streamlit App")
c1,c2=st.columns(2)
num1=c1.number_input("enter first number")
num2=c2.number_input("enter second number")
option=["add","sub","mult","div"]
choice=st.radio("select an operation",option,horizontal=True)
button=st.button("calculator")
if button:
    if(choice=="add"):
        result=num1+num2
    if(choice=="sub"):
        result=num1-num2 
    if(choice=="mult"):
        result=num1*num2 
    if(choice=="div"):
        result=num1/num2                                             
st.warning(f'result is{result}')   