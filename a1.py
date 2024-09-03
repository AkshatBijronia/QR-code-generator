import qrcode
from PIL import Image, ImageDraw

def generate_qr_code(data, color, background):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=color, back_color=background)

    # Save the QR code to a file
    img.save('qr_code.png')

def main():
    # Get the user input
    data = input("Enter the data to encode: ")
    color = input("Enter the color (e.g. #FFFFFF): ")
    background = input("Enter the background color (e.g. #000000): ")

    # Generate the QR code
    generate_qr_code(data, color, background)

    print("QR code generated and saved as qr_code.png")

if __name__ == "__main__":
    main()