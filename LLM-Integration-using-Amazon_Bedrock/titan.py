import boto3
import json

# Initialize AWS Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Define the input prompt
prompt_data = "Who is Narendra Modi"

# Create the payload according to Amazon Titan's expected format
payload = {
    "inputText": prompt_data,  # Titan uses "inputText" instead of "prompt"
    "textGenerationConfig": {
        "maxTokenCount": 512,  # Limit output tokens
        "temperature": 0.6,    # Adjust randomness
        "topP": 0.9            # Adjust probability sampling
    }
}

# Convert the payload to JSON format
body = json.dumps(payload)

# Define the Amazon Titan model ID
model_id = "amazon.titan-text-lite-v1"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse the response
response_body = json.loads(response.get("body").read())
response_text = response_body.get("results", [{}])[0].get("outputText", "No response generated.")

# Print the AI-generated response
print(response_text)
