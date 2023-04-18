# OpenAI-API-Error-Handler
This is a simple Python application that calls the OpenAI API and handles timeout, rate limit, and server errors.




# Setup
Install the openai Python library by running pip install openai.
Set your OpenAI API key as an environment variable named OPENAI_API_KEY.
Run the application by running python app.py.

# Usage
Call the query_api function with a prompt string to make a request to the OpenAI API. The function will handle timeout, rate limit, and server errors and retry the request until it succeeds or encounters a different error, which it will then raise to the caller.

# Python
response = query_api("What is the meaning of life?")
print(response)

# License
This application is licensed under the MIT License. See the LICENSE file for more information.




