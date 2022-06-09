import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(
    	host="2.tcp.ngrok.io",
    	database="cube",
    	user="root",
    	port=19669,
	password="pass")

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from Users;")

# Print results.
st.write("SELECT * FROM Users;")
for row in rows:
    st.write(f"{row}")
