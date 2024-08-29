# Postman-like App in Python

This is a simple, Streamlit-based web application that mimics some of the basic functionality of Postman, allowing users to send HTTP requests and view responses. It's built using Python and Streamlit, making it easy to use and modify.

## Features

- Support for GET, POST, PUT, and DELETE HTTP methods
- Custom header input
- JSON body input for POST and PUT requests
- Response display including status code, headers, and content
- Automatic JSON parsing for response content when applicable

## Requirements

- Python 3.6+
- Streamlit
- Requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-postman-app.git
   cd python-postman-app
   ```

2. Install the required packages:
   ```
   pip install streamlit requests
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the interface to:
   - Enter the URL for your request
   - Select the HTTP method
   - Add headers in JSON format (optional)
   - Add a JSON body for POST and PUT requests (optional)
   - Click "Send Request" to make the API call

4. View the response, including status code, headers, and content.

## Code Structure

- `main()`: The main function that sets up the Streamlit interface and handles the request/response flow.
- `parse_json_input()`: A helper function to parse JSON input for headers and body.

## Error Handling

The app includes basic error handling for:
- Invalid JSON input
- Network request errors
- General exceptions

## Limitations

- This app is a basic implementation and may not include all features of more robust API testing tools.
- It currently only supports JSON for body input in POST and PUT requests.
- There's no built-in authentication mechanism for APIs that require it.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/python-postman-app/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
