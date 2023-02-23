from PIL import Image
import stepic
# Open the image from which the secret message is to be extracted:
img_name1 = input("Enter image name (with extension): ")
image = Image.open(img_name1)
# Pass the above image into the decode() function.
# This function returns the secret message in the form of a string:
decoded_msg = stepic.decode(image)
print("Decryption Completed!")
# Display the message
p = input("Enter Password: ")
file2 = open("Original.txt","r")
for i in file2:
    q = i
if p==q:
    print("Decoded Message:", decoded_msg)
else:
    print("Wrong Password")
