import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()#active api key 
genai.configure(api_key=os.getenv('Google_Gemini_API'))

#movie Recommenation 
st.title("🍿🎥✮⋆Movie Recomendation System 🍿🎥✮⋆ ")
user_input=st.text_input('Enter a movie :')
submit=st.button('Enter')


model=genai.GenerativeModel('gemini-2.5-flash-lite')
if submit and user_input.strip():
    st.markdown(f'Movie name entered:{user_input}')
    response=model.generate_content(f"Generate Movie recommendations related to :{user_input} ")
    st.write(f"Recommendation of Movie :\n {response.text}")
else:
    st.write("Enter a movie name")