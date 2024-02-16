import fitz  # PyMuPDF
import spacy
from torchvision import models, transforms
from PIL import Image

# Initialize spaCy for English language
nlp = spacy.load("en_core_web_sm")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to perform basic NLP analysis
def analyze_text(text):
    doc = nlp(text)
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")

# Function to classify an image using a pre-trained model
def classify_image(image_path):
    # Load a pre-trained model (ResNet18) and set it to evaluation mode
    model = models.resnet18(pretrained=True)
    model.eval()

    # Define a transform to prepare the image
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Open the image, apply the transforms, and add a batch dimension
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        outputs = model(image)
        _, predicted = outputs.max(1)
        print(f"Predicted class ID: {predicted.item()}")

# Example usage
pdf_text = extract_text_from_pdf("example.pdf")  # replace "example.pdf" with your PDF file path
analyze_text(pdf_text)

classify_image("example.jpg")  # replace "example.jpg" with your image file path
