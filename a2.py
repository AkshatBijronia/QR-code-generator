import qrcode
from PIL import Image, ImageTk
import tkinter as tk

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
    # Create a Tkinter window
    window = tk.Tk()
    window.title("QR Code Generator")

    # Create a label and entry field for the data
    label = tk.Label(window, text="Enter the data to encode:")
    label.pack()
    data_entry = tk.Entry(window, width=50)
    data_entry.pack()

    # Create Tkinter variables for color and bgcolor
    color_var = tk.StringVar()
    bgcolor_var = tk.StringVar()

    # Create a label and buttons for the QR code color
    label = tk.Label(window, text="Select QR code color:")
    label.pack()
    color_buttons = []
    colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFFFF", "#000000"]
    for i, color in enumerate(colors):
        button = tk.Button(window, text=color, command=lambda c=color: color_var.set(c))
        button.pack(side=tk.LEFT)
        color_buttons.append(button)

    # Create a label and buttons for the background color
    label = tk.Label(window, text="Select background color:")
    label.pack()
    bgcolor_buttons = []
    bgcolors = ["#FFFFFF", "#000000", "#FF0000", "#00FF00", "#0000FF"]
    for i, bgcolor in enumerate(bgcolors):
        button = tk.Button(window, text=bgcolor, command=lambda b=bgcolor: bgcolor_var.set(b))
        button.pack(side=tk.LEFT)
        bgcolor_buttons.append(button)

    # Create a button to generate the QR code
    def generate_qr_code_callback():
        data = data_entry.get()
        color = color_var.get()
        background = bgcolor_var.get()
        generate_qr_code(data, color, background)

    generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code_callback)
    generate_button.pack()

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()