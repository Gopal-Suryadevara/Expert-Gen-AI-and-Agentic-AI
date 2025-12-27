import streamlit as st #import streamlit

st.title("My 1st streamlit app") #To add title

st.write("Welcome! This app calculates the square of the number") #add some text

st.header("select a number") #header text
number = st.slider("pick a number",0,100,25) #create a slider with min = 0, max = 100, default = 25

st.subheader("Result") #subheader text
squared_number = number * number #calculation part
st.write(f'the squre of **{number}** is **{squared_number}**') #to print the output
