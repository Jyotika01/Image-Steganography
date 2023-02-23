from PIL import Image
import stepic
# Open the image within which the secret message is to be stored:
img_name = input("Enter image name (with extension): ")
img = Image.open(img_name)
# Specify the secret message:
message = input("Enter the message to be encoded:")
# Convert the message into UTF-8 format:
message = message.encode()
# Pass the image and message into the encode() function.
# This function returns a new image within which the message is hidden:
encoded_img = stepic.encode(img, message)
# Specify the name and extension for the new image generated:
encoded_img_name = input("Enter the name of encoded image: ")
encoded_img.save(encoded_img_name)
password = input("Enter password: ")
file1 = open("Original.txt", "w") 
file1.write(password)
file1.close
print("Encryption Completed!")



