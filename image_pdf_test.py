from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def generate_pdf_with_image(image_path, pdf_path):
    # Create a new PDF document
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)

    # Create a list to hold the flowable elements
    elements = []

    # Load the image
    image = Image(image_path)

    # Set the size and position of the image
    image.drawWidth = 400
    image.drawHeight = 300

    # Add the image to the list of elements
    elements.append(image)

    # Build the PDF document
    doc.build(elements)

# Provide the path to the image file and the desired path for the generated PDF
image_path = '25M.png'
pdf_path = 'newpdf.pdf'

# Generate the PDF with the image
generate_pdf_with_image(image_path, pdf_path)
