import openai
import time
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_api(prompt, model, temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "text": prompt}
            ],
            temperature=temperature,
            max_tokens=150,
            timeout=10
        )
        return response.choices[0].text
    except openai.error.APIError as error:
        if error.status == 408 or error.status == 429 or error.status >= 500:
            # The request timed out, the rate limit was exceeded, or the server encountered an error, so wait a bit and try again
            time.sleep(5)
            return query_api(prompt, model, temperature)
        else:
            raise error

prompt = "Hello, how are you doing today?"
model = "gpt-3.5-turbo"
response = query_api(prompt, model)
print(response)
