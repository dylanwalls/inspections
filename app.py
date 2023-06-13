from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from models import Inspection
import os
from pdf_generator import generate_pdf_statement
import uuid
import base64
from PIL import Image, ImageOps
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import mimetypes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/dylanwalls/Documents/Bitprop/tenant_inspections/inspections/images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/dylanwalls/Documents/Bitprop/tenant_inspections/inspections/inspection_management.db'
db = SQLAlchemy(app)

# Specify the allowed file extensions for the image
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form data
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        agree = request.form.get('agree')
        comments = request.form.get('comments')
        # image = request.form.get('images')
        signature = request.form.get('signature')
        
        # # Handle file upload for image
        image = request.files['images']
        image_filename = f'{str(uuid.uuid4())}.jpg'  # Generate a unique filename
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)

        # # Handle file upload for signature
        # signature = request.files['signature']
        # signature_filename = f'{str(uuid.uuid4())}.png'  # Generate a unique filename
        # signature_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_filename)
        # signature.save(signature_path)
        
        # Create a new Inspection object with the form values
        inspection = Inspection(
            name=name,
            email=email,
            age=age,
            consent=bool(agree),
            comments=comments,
            image=image_filename,
            signature=signature,
        )

        # Save the inspection object to the database
        db.session.add(inspection)
        db.session.commit()

        # Convert base64 signature to image
        signature_data = signature.split(",")[1]  # Remove the "data:image/png;base64," prefix
        signature_image_data = base64.b64decode(signature_data)
        signature_filename = f'{str(uuid.uuid4())}.png'  # Generate a unique filename for the signature image
        signature_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_filename)
        with open(signature_path, 'wb') as signature_file:
            signature_file.write(signature_image_data)
        
        # Open the signature image
        signature_image = Image.open(signature_path).convert("RGBA")

        # Create a new image with white background
        white_background = Image.new("RGBA", signature_image.size, (255, 255, 255))
        white_background.paste(signature_image, (0, 0), signature_image)

        # Convert the image to RGB mode (without alpha channel)
        white_background = white_background.convert("RGB")

        # Save the modified signature image
        white_background.save(signature_path)

        print(f'SIGNATURE_PATH: {signature_path}')


        # Generate the PDF statement
        data = {
            'name': name,
            'email': email,
            'age': age,
            'agree': agree,
            'comments': comments,
            'image_path': image_path,
            'signature_path': signature_path,
        }
        pdf_path = generate_pdf_statement(data)
    #     print (f"THIS IS THE PDF PATH: {pdf_path}")


    #     # Send the email
    #     smtp_server = 'smtp.office365.com'  # Replace with your SMTP server address
    #     smtp_port = 587  # Replace with your SMTP server port
    #     smtp_username = 'dylan.walls@bitprop.com'  # Replace with your SMTP username
    #     smtp_password = 'Termsheet2022'  # Replace with your SMTP password

    #     # Create an SMTP connection with TLS encryption
    #     server = smtplib.SMTP(smtp_server, smtp_port)
    #     server.starttls()

    #     # Authenticate with SMTP AUTH
    #     server.login(smtp_username, smtp_password)

    #     # Email the PDF as an attachment
    #     msg = MIMEMultipart()
    #     msg['From'] = 'dylan.walls@bitprop.com'  # Replace with your email address
    #     msg['To'] = email
    #     msg['Subject'] = 'PDF Attachment'
        
    #    # Open the PDF file
    #     with open(pdf_path, 'rb') as file:
    #         # Determine the MIME type of the PDF file
    #         mimetype, _ = mimetypes.guess_type(pdf_path)

    #         # Create a MIMEBase object for the PDF
    #         attachment = MIMEBase('application', 'octet-stream')
    #         attachment.set_payload(file.read())

    #         # Set the proper MIME type and filename
    #         attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_path)}')
    #         attachment.add_header('Content-Type', mimetype)

    #         # Encode the attachment
    #         encoders.encode_base64(attachment)

    #     # Add the PDF attachment to the email
    #     msg.attach(attachment)

    #     # Send the email
    #     server.send_message(msg)

    #     # Close the SMTP connection
    #     server.quit()

        return 'Form submitted successfully!'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
