import streamlit as st
import requests
import json

def parse_json_input(input_str, field_name):
    if not input_str:
        return {}
    try:
        return json.loads(input_str)
    except json.JSONDecodeError:
        st.error(f"Invalid JSON in {field_name}. Please check your input.")
        return None

def main():
    st.title("Python Postman-like App")

    # Input for URL
    url = st.text_input("Enter URL")

    # Select HTTP method
    method = st.selectbox("Choose HTTP Method", ["GET", "POST", "PUT", "DELETE"])

    # Input for headers
    headers_input = st.text_area("Enter Headers (JSON format)")

    # Input for body (for POST and PUT requests)
    body_input = ""
    if method in ["POST", "PUT"]:
        body_type = st.radio("Body Type", ["None", "JSON"])
        if body_type == "JSON":
            body_input = st.text_area("Enter JSON Body")

    # Button to send request
    if st.button("Send Request"):
        if not url:
            st.error("Please enter a URL.")
            return

        headers = parse_json_input(headers_input, "Headers")
        if headers is None:
            return

        body = None
        if method in ["POST", "PUT"] and body_type == "JSON":
            body = parse_json_input(body_input, "Request Body")
            if body is None:
                return

        try:
            # Send request
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=body)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=body)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)

            # Display response
            st.subheader("Response")
            st.write(f"Status Code: {response.status_code}")
            st.write("Headers:")
            st.json(dict(response.headers))
            st.write("Content:")
            
            # Try to parse response as JSON, if not, display as text
            try:
                st.json(response.json())
            except json.JSONDecodeError:
                st.text(response.text)

        except requests.RequestException as e:
            st.error(f"Request error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()