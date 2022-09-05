import streamlit as st
import pickle
pickle_in=open("SalaryPrediction.pkl","rb")
model=pickle.load(pickle_in)


years=st.number_input("Years Of Experience")

if st.button("PREDICT"):
  salary=model.predict([[years]]).squeeze()
  salary=int(salary)
  st.success(f"Salary Predicted is {salary}")
