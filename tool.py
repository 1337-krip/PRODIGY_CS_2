from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)
    
    # Encrypt the image by swapping pixel values using the key
    np.random.seed(key)
    rows, cols, _ = pixels.shape
    for i in range(rows):
        for j in range(cols):
            if np.random.rand() > 0.5:
                # Swap pixels with a random offset
                offset = np.random.randint(1, 5)
                new_i = (i + offset) % rows
                new_j = (j + offset) % cols
                pixels[i, j], pixels[new_i, new_j] = pixels[new_i, new_j], pixels[i, j]
    
    # Save the encrypted image
    encrypted_image = Image.fromarray(pixels)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)
    
    # Decrypt the image by reversing the pixel swap using the key
    np.random.seed(key)
    rows, cols, _ = pixels.shape
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if np.random.rand() > 0.5:
                # Swap pixels back with the same random offset
                offset = np.random.randint(1, 5)
                new_i = (i + offset) % rows
                new_j = (j + offset) % cols
                pixels[i, j], pixels[new_i, new_j] = pixels[new_i, new_j], pixels[i, j]
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(pixels)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        return
    
    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the output path for the processed image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))
    
    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
