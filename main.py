from PIL import Image,ImageDraw,ImageFont
from barcode import EAN13 
from barcode.writer import ImageWriter 

def generate_barcode(barcode_data):
    # Now, let's create an object of EAN13 
    my_code = EAN13(barcode_data, writer=ImageWriter()) 
    # Save the barcode as PNG
    my_code.save("barcode")

# Function to generate a QR code and add it to an image
def add_barcode_to_img(image_path, output_image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Calculate the position to center the QR code on the image
    x = 100
    y = 100

    barcode = Image.open("barcode.png")

    # Paste the QR code onto the image
    image.paste(barcode, (x, y))

    image.save(output_image_path)
    # Close the image and QR code
    image.close()

def add_text_to_img(image_path,text,output_image_path):
    image = Image.open(image_path)
    Im = ImageDraw.Draw(image)
    mf = ImageFont.truetype("./great_vibes.ttf", 120)
    # Add Text to an image
    Im.text((1000,850), text, (0,0,0), font=mf)

    image.save(output_image_path)
    # Close the image and QR code
    image.close()


# Example usage:
input_image_path = 'img.jpg'
barcode_data = '2123432123032'  # Replace with your Barcode code data
text = 'Shahidul Alam'  # Replace with your text
output_image_path = 'output.jpg'

generate_barcode(barcode_data)
add_barcode_to_img(input_image_path, output_image_path)
add_text_to_img(output_image_path,text ,output_image_path)
