import streamlit as st
import requests
import random
import string
import socket

def generate_subdomain():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def is_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def main():
    st.title("Streamlit Ngrok-like Service")

    # Session state to store the subdomain and port
    if 'subdomain' not in st.session_state:
        st.session_state.subdomain = generate_subdomain()
    if 'port' not in st.session_state:
        st.session_state.port = None

    # Input for local port
    port = st.number_input("Enter the local port of your application:", min_value=1, max_value=65535, value=8080)

    if st.button("Start Tunnel"):
        if is_port_open(port):
            st.session_state.port = port
            st.success(f"Tunnel established! Use the URL below to access your application.")
        else:
            st.error(f"No application found running on port {port}. Please make sure your application is running.")

    if st.session_state.port:
        tunnel_url = f"https://{st.session_state.subdomain}-{st.secrets.streamlit_id}.streamlit.app"
        st.write(f"Your tunnel URL: {tunnel_url}")
        st.write("Use this URL to send requests to your local application.")

        # Request handling
        st.write("Enter a path to send a request to your local application:")
        path = st.text_input("Path (e.g., /api/data):", "/")
        method = st.selectbox("HTTP Method:", ["GET", "POST", "PUT", "DELETE"])
        
        if st.button("Send Request"):
            full_url = f"http://localhost:{st.session_state.port}{path}"
            try:
                if method == "GET":
                    response = requests.get(full_url)
                elif method == "POST":
                    response = requests.post(full_url)
                elif method == "PUT":
                    response = requests.put(full_url)
                elif method == "DELETE":
                    response = requests.delete(full_url)
                
                st.write("Response Status Code:", response.status_code)
                st.write("Response Headers:")
                st.json(dict(response.headers))
                st.write("Response Content:")
                st.code(response.text)
            except requests.RequestException as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()