# Image Recognition Project
## Introduction
This is a personal image recognition project that leverages Azure AI services to perform basic image analysis and provide a caption, however I may come back to improve this in the future for personal learning.

## Purpose
I developed this project to help me explore Azure cloud technologies and improve my coding skills. As somone new to this field, having only completed AZ-900, my primary goal was to learn and understand Azure AI Services.

## Features
- Analyse images in various formats, including JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF, or MPO.
- Extract a caption from images.
- Provide confidence scores for extracted text.
- Input Validation
- The code uses async/await syntax to handle asynchronous operations efficiently, allowing non-blocking execution of code.
- Error Handling connected to Azure

**note**:Ensure image file size is less than 20MB and verify image dimensions are at least 50x50 pixels but less than 16000x16000 pixels.


## Requirements
- Python 3.8+
- Azure subscription (The free tier for Azure AI Services will work fine with this program)

## Installation
1. Clone the repo to your machine and install the Python packages
```bash
git clone <repository_url>

pip install -r requirements.txt
```
2. Setup Azure AI Services:
  - Obtain your key and endpoint from the Azure Computer Vision resource
  - Set the environment variables
```bash  
setx VISION_KEY yourkey
setx VISION_ENPOINT yourendpoint
```
## Usage
- Run the program
- Follow the prompts to analyse image
- Make sure the path is correct (i suggest adding the image folder to the same directory)
