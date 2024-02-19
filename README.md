# FastAPI Example Project

This is a simple example project demonstrating the use of FastAPI for building web APIs in Python.

## Setup

1. **Create a Virtual Environment**:

   ```bash
   python -m venv env
2. ** Activate the Virtual Environment:
   # For Windows
    ```bash
   .\env\Scripts\activate
    
    ```bash
     source env/bin/activate
3. ** Install Dependencies:
    ```bash
      pip install fastapi uvicorn

5. ** To run the API, execute the following command:
    ```bash
      uvicorn main:app --reload


# Endpoints

GET /test/

Returns a simple JSON response.

GET /usernames/{user_id}/

Returns a JSON response with the provided user_id.

POST /create/

Creates a new user using the provided JSON data.

# Usage
Visit http://127.0.0.1:8000/test/ in your browser or use tools like curl or Postman to interact with the GET endpoints.

For POST /create/, send a POST request with JSON data containing "name" and "age" fields.


