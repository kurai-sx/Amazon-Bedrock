import boto3
import json
import base64

# Initialize Bedrock Client
bedrock = boto3.client(service_name="bedrock-runtime")

# Request Payload
payload = {
    "textToImageParams": {"text": "Mumbai Beach"},
    "taskType": "TEXT_IMAGE",
    "imageGenerationConfig": {
        "cfgScale": 8,
        "seed": 42,
        "quality": "standard",
        "width": 1024,
        "height": 1024,
        "numberOfImages": 1
    }
}

# Convert payload to JSON
body = json.dumps(payload)

# Invoke Bedrock Model
response = bedrock.invoke_model(
    modelId="amazon.titan-image-generator-v1",
    body=body,
    accept="application/json",
    contentType="application/json"
)

# Decode the Response
response_body = json.loads(response["body"].read())

# Extract Image Data (Base64)
if "images" in response_body:
    for idx, image_data in enumerate(response_body["images"]):
        image_bytes = base64.b64decode(image_data)  # Decode Base64
        image_path = f"generated_image_{idx+1}.png"

        # Save Image
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)
            print(f"Image saved as {image_path}")
else:
    print("No images were generated.")
