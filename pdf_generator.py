import base64
import os
from flask import current_app as app
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_statement(data):
    name = data.get('name')
    image_path = data.get('image_path')
    signature_path = data.get('signature_path')

    # Define the PDF file name based on the "name" variable
    pdf_file_name = f'{name}_inspection_statement.pdf'

    # Define the path to the specific folder in the working directory
    save_folder = '/Users/dylanwalls/Documents/Bitprop/tenant_inspections/inspections/statements/'

    # Define the image file path
    # image_path = os.path.join(save_folder, image_data)
    print(f'IMAGE PATH: {image_path}')

    # Define the signature file path
    # signature_path = os.path.join(save_folder, signature_data)
    print(f'SIGNATURE PATH: {signature_path}')

    # Generate the PDF statement
    pdf_path = generate_pdf_with_images(save_folder, pdf_file_name, data)

    return pdf_path

def generate_pdf_with_images(save_folder, pdf_file_name, data):
    # Create the PDF canvas
    pdf_file_path = os.path.join(save_folder, pdf_file_name)
    c = canvas.Canvas(pdf_file_path, pagesize=letter)

    # Define the image position and size
    image_x = 100
    image_y = 500
    image_width = 200
    image_height = 150

    # Draw the image
    image_path = data.get('image_path')
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

    # Define the signature position and size
    signature_x = 100
    signature_y = 300
    signature_width = 200
    signature_height = 50

    # Draw the signature
    signature_path = data.get('signature_path')
    c.drawImage(signature_path, signature_x, signature_y, width=signature_width, height=signature_height)

    # Define the text position
    text_x = 100
    text_y = 100

    # Write the text
    c.setFont("Helvetica", 12)
    c.drawString(text_x, text_y, f"Name: {data.get('name')}")
    c.drawString(text_x, text_y - 20, f"Email: {data.get('email')}")
    c.drawString(text_x, text_y - 40, f"Age: {data.get('age')}")
    c.drawString(text_x, text_y - 60, f"Agreed to Terms: {data.get('agree')}")
    c.drawString(text_x, text_y - 80, f"Comments: {data.get('comments')}")

    # Save the canvas to the PDF file
    c.save()

    return pdf_file_path





# generate_pdf_statement(data)

    # # Generate the HTML content for the PDF statement
    # html_content = f'''
    # <html>
    # <head>
    #     <title>Lease Inspection Statement</title>
    # </head>
    # <body>
    #     <h1>Lease Inspection Statement</h1>
    #     <p>Name: {data.get('name')}</p>
    #     <p>Email: {data.get('email')}</p>
    #     <p>Age: {data.get('age')}</p>
    #     <p>Agreed to Terms: {data.get('agree')}</p>
    #     <p>Comments: {data.get('comments')}</p>
    #     <p>Image:</p>
    #     <img src="{image_path}" alt="Image">
    #     <p>Signature:</p>
    #     <img src="{signature_path}" alt="Signature">
    # </body>
    # </html>
    # '''

    # pdf_file_path = f'{save_folder}{pdf_file_name}'

    # # Generate PDF with images
    # generate_pdf_with_images(html_content, pdf_file_path)

    # def generate_pdf_with_images(html_content, pdf_file_path):
    #     HTML(string=html_content).write_pdf(pdf_file_path)    


    # # Specify the options for PDF generation
    # options = {
    #     'page-size': 'A4',
    #     'encoding': 'UTF-8'
    # }

    # # Generate the PDF using pdfkit
    # pdfkit.from_string(html_content, f'{save_folder}{pdf_file_name}', options=options)
