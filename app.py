import streamlit as st
import requests

API_URL = "http://localhost:8000/query"

st.set_page_config(page_title="PostgreSQL CRUD App", layout="centered")
st.title("🧠 PostgreSQL CRUD App via MCP + Streamlit")

st.sidebar.header("Choose Operation")
operation = st.sidebar.radio("Select", ["Create User", "Read Users", "Update Email", "Delete User"])

if operation == "Create User":
    st.subheader("Create a New User")
    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    if st.button("Create"):
        payload = {
            "name": "create_user",
            "args": {
                "name": name,
                "email": email
            }
        }
        response = requests.post(API_URL, json=payload)
        st.success(response.json())
        
elif operation == "Read Users":
    st.subheader("List of Users")
    if st.button("Fetch Users"):
        payload = {
            "name": "read_users",
            "args": {}
        }
        response = requests.post(API_URL, json=payload)
        result = response.json().get("result", [])
        if result:
            st.table(result)
        else:
            st.warning("No data found.")

elif operation == "Update Email":
    st.subheader("Update User Email")
    user_id = st.number_input("User ID", step=1, min_value=1)
    new_email = st.text_input("New Email")
    if st.button("Update"):
        payload = {
            "name": "update_user_email",
            "args": {
                "user_id": int(user_id),
                "new_email": new_email
            }
        }
        response = requests.post(API_URL, json=payload)
        st.success(response.json())

elif operation == "Delete User":
    st.subheader("Delete a User")
    user_id = st.number_input("User ID", step=1, min_value=1)
    if st.button("Delete"):
        payload = {
            "name": "delete_user",
            "args": {
                "user_id": int(user_id)
            }
        }
        response = requests.post(API_URL, json=payload)
        st.success(response.json())
