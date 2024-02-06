import os
import sys
import asyncio
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError

# Help and rules for the image recognition
def rules():
    return ("""
            The image must be presented in JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF, or MPO format \n
            The image file size must be less than 20MB \n
            The image dimensions must be at least 50 x 50 but less than 16000 x 16000 pixels
            """)

# Endpoint and key for the Azure Vision API
try:
    endpoint = str(os.environ.get("VISION_ENDPOINT"))
    key = str(os.environ.get("VISION_KEY"))
except KeyError:
    print("Missing 'VISION_ENDPOINT' or 'VISION_KEY'")
    exit()

# Create a client for the Azure Vision API
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Read image
def read_image(image_path):
    with open(image_path, "rb") as image:
        return image.read()

# Analyse image
async def analyse(image_path):
    if not os.path.exists(image_path):
        print(f"File '{image_path}' does not exist.")
        return None

    print(f"Analysing image '{image_path}'...")
    image_data = read_image(image_path)
    if image_data:
        try:
            result = client.analyze(image_data=image_data, visual_features=[VisualFeatures.CAPTION])
            return result
        except HttpResponseError as e:
            print(f"Status code: {e.status_code}")
            print(f"Reason: {e.reason}")
            print(f"Message: {e.error.message}")
            return None

async def execute(command):
    if command == "exit":
        sys.exit()
    elif command == "analyse":
        image_path = input("Enter path: ")
        result = await analyse(image_path)
        if result and result.caption:
            print("Analysis Results:")
            print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.2f}")
        else:
            print("No Analysis Results found.")


# Run the code
async def main():
    print(rules())
    while True:
        command = input("Enter command: ")
        if command == "exit":
            sys.exit()
        await execute(command)

if __name__ == "__main__":
    asyncio.run(main())
