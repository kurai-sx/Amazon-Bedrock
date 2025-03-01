# AWS Bedrock Image & Text Generation

This repository contains Python scripts to interact with AWS Bedrock using Amazon Titan models for text generation and image generation. The implementation uses the boto3 SDK to invoke AI models via the AWS Bedrock API.

# Features

✅ Text Generation using Amazon Titan Text Lite 

✅ Image Generation using Amazon Titan Image Generator

✅ AWS Bedrock API Integration

✅ Python-based Implementation with boto3

# Requirements
AWS Account with Bedrock Access

Python 3.8+

boto3 (AWS SDK for Python)

# Installation
## Clone the repository:
```bash
git clone https://github.com/your-username/AWS-Bedrock-Image-Gen.git
cd AWS-Bedrock-Image-Gen
```
## Install dependencies:

```bash
pip install -r requirements.txt
```


# Usage
## Text Generation (Titan Text Lite)
Run the script to generate text using Amazon Titan:

```bash
python titan.py
```

## Image Generation (Titan Image Generator)
Run the script to generate images using Amazon Titan:
```bash
python image_generator.py
```
Generated images will be saved in the output/ folder.

# Example API Response (Text Generation)
json 
```bash
{
    "generatedText": "Generative AI is revolutionizing content creation..."
}
Exam
```
Example Output - Image Generated
<img src="https://github.com/user-attachments/assets/f78816ef-c0a2-4771-ae68-37367e772aad" alt="drawing" width="300"/>
