import os
from google.cloud import aiplatform

# Set your Google Cloud project ID
project_id = "your-project-id"

# Set the location of the AI Platform (Unified) API endpoint
location = "us-central1"  # Update with your preferred location

# Set the name of your endpoint
endpoint_id = "your-endpoint-id"

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-key.json"

# Initialize the AI Platform (Unified) client
client = aiplatform.gapic.EndpointServiceClient(client_options={"api_endpoint": f"{location}-aiplatform.googleapis.com"})

# Define your input data
input_data = {
    "instances": [
        {
            # Define your input data here
        }
    ]
}

# Make a prediction request to the endpoint
response = client.predict(endpoint=endpoint_id, instances=input_data)

# Process the response
for prediction in response.predictions:
    # Handle the prediction results
    pass
