from dotenv import load_dotenv
load_dotenv() #Load all environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google genai model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

# function to retrive query from the database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

# define the prompt for the model

prompt=[
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.
\n\nFor example, 
\nExample 1 - how many entries of records are present?
the SQL command will be something like this SELECt COUNT(*) FROM STUDENT;

\nExample 2 - Tell me all the  students studying  in Data Science class ?
the SQL command will be something like this SELECt * FROM STUDENT where CLASS='Data Science';
also the sql code should not have ''' in beginning or end and sql word in output
"""
]

# streamlit app

st.set_page_config(page_title="I can Retrive Any SQL Query")
st.header("Gemini App to Retrive SQL Data")

question = st.text_input("Input: ",key = "input")

submit = st.button("Ask the question")

# if submit is clicked 
if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)