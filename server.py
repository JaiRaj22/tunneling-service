import streamlit as st
import requests
import json

def main():
    st.title("Streamlit API Testing Proxy")

    st.write("""
    This app allows you to send requests to your local server.
    Enter your local server's URL and the endpoint you want to test.
    """)

    # Input for local server URL
    local_url = st.text_input("Enter your local server's URL (e.g., http://localhost:8080):", "http://localhost:8080")

    # Input for endpoint
    endpoint = st.text_input("Enter the endpoint (e.g., /api/data):", "/")

    # Full URL
    full_url = f"{local_url.rstrip('/')}/{endpoint.lstrip('/')}"
    st.write(f"Full URL: {full_url}")

    # HTTP Method selection
    method = st.selectbox("HTTP Method:", ["GET", "POST", "PUT", "DELETE"])

    # Request headers
    st.subheader("Headers")
    headers = {}
    for i in range(3):  # Allow up to 3 custom headers
        key = st.text_input(f"Header Key {i+1}:")
        value = st.text_input(f"Header Value {i+1}:")
        if key and value:
            headers[key] = value

    # Request body for POST/PUT
    st.subheader("Request Body (for POST/PUT)")
    body = st.text_area("Enter JSON body:")

    if st.button("Send Request"):
        try:
            if method == "GET":
                response = requests.get(full_url, headers=headers)
            elif method == "POST":
                response = requests.post(full_url, headers=headers, data=body)
            elif method == "PUT":
                response = requests.put(full_url, headers=headers, data=body)
            elif method == "DELETE":
                response = requests.delete(full_url, headers=headers)
            
            st.subheader("Response")
            st.write("Status Code:", response.status_code)
            st.write("Response Headers:")
            st.json(dict(response.headers))
            st.write("Response Content:")
            try:
                st.json(response.json())
            except json.JSONDecodeError:
                st.code(response.text)
        except requests.RequestException as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()