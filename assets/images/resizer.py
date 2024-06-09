import cv2
import os

def resize_images_in_folder(input_folder, output_folder, width, height):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct full file path
        img_path = os.path.join(input_folder, filename)
        
        # Read the image
        img = cv2.imread(img_path)
        
        # Check if the file is an image
        if img is not None:
            # Resize the image
            resized_img = cv2.resize(img, (width, height))
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_img)
            print(f'Resized and saved: {output_path}')
        else:
            print(f'Skipped non-image file: {filename}')

# Parameters
input_folder = 'temp'
output_folder = 'projs'
width = 800
height = 500

# Run the function
resize_images_in_folder(input_folder, output_folder, width, height)

