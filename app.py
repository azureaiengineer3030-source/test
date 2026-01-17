import streamlit as st
from db.connection import get_db_connection

st.set_page_config(page_title="DB Connectivity Test", layout="centered")

st.title("🔌 Database Connectivity Test")

st.write("This page verifies whether the Streamlit app can connect to the database using GitHub config.")

# Button to test DB connection
if st.button("Test Database Connection"):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT 1")
        result = cur.fetchone()

        cur.close()
        conn.close()

        st.success(f" 👍 Database connected successfully. ✅")

    except Exception as e:
        st.error("❌ Database connection failed")
        st.exception(e)


