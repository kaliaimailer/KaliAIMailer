import requests
import json

# Set up your API key and endpoint URL
api_key = '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'
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'

# Example prompt
prompt = "Once upon a time,"

# Set up headers with your API key
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Set up data payload with the prompt
data = {
    'model': 'davinci',
    'prompt': prompt,
    'max_tokens': 50  # Adjust as needed
}

# Send POST request to the API endpoint
response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    # Get the generated text from the response
    generated_text = result['choices'][0]['text'].strip()
    print("Generated Text:", generated_text)
else:
    print("Error:", response.text)
