import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Help and rules for the image recognition
def help ():
    return "Use the command 'analyse' to analyse an image and the command 'rules' to see the rules for the image."
def rules ():
    return ("""
            The image must be presented in JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF, or MPO format \n
            The image file size must be less than 20MB \n
            The image dimensions must be at least 50 x 50 but less than 16000 x 16000 pixels
            """)
# Endpoint and key for the Azure Vision API
try:
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing 'VISION_ENDPOINT' or 'VISION_KEY'")
    exit()

credential = AzureKeyCredential(key)
client = ImageAnalysisClient(endpoint, credential)

# sends image data to Azure AI Vision and return the tags while ensuring file is properly closed
def analyse(image_path):
    if not os.path.exists(image_path):
        return(f"File {image_path} does not exist.")
        
    print(f"Analysing image {image_path} ...")
    with open(image_path, "rb") as image:
        result = client.analyze_image_in_stream(image, visual_features=[VisualFeatures.tags])
    return result.tags

# Automatically run the code when the file is run
# if __name__ == "__main__": image_path = input ("Enter path: ")

# start the code
if __name__ == "__main__":
    print(help())
    print(rules())