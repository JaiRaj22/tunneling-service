import streamlit as st
import json
import uuid

def generate_random_url():
    return f"http://localhost:{str(uuid.uuid4())}"

def main():
    st.title("Streamlit API Tester for Local Development")

    st.write("""
    This app helps you formulate API requests for testing your local server.

    How to use:
    1. Click 'Get URL' to generate a random URL.
    2. Use this URL to test your Node.js application.
    3. Enter the endpoint and other details as needed.
    """)

    # Generate random URL
    random_url = generate_random_url()
    st.write(f"Generated URL: {random_url}")

    # Input for endpoint
    endpoint = st.text_input("Endpoint:", "/")

    # Full URL
    full_url = f"{random_url.rstrip('/')}/{endpoint.lstrip('/')}"
    st.write(f"Full URL: {full_url}")

    # HTTP Method selection
    method = st.selectbox("HTTP Method:", ["GET", "POST", "PUT", "DELETE"])

    # Request body for POST/PUT
    st.subheader("Request Body (for POST/PUT)")
    body = st.text_area("Enter JSON body:")

    # Response prettifier
    st.subheader("Response Prettifier")
    st.write("Paste the response from your terminal here to prettify JSON:")
    response_text = st.text_area("Response:")
    if response_text:
        try:
            prettified = json.dumps(json.loads(response_text), indent=2)
            st.code(prettified, language="json")
        except json.JSONDecodeError:
            st.write("The response is not valid JSON. Displaying as plain text:")
            st.code(response_text)

if __name__ == "__main__":
    main()
