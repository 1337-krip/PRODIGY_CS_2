This Python program allows you to encrypt and decrypt images using simple pixel manipulation. It performs encryption by swapping pixel values based on a given key, and decrypts the image by reversing the process with the same key.

Features

- Encrypt images by swapping pixel values.
- Decrypt images by reversing the pixel swap process.
- Input image paths, output paths, and encryption/decryption keys interactively.

Requirements

- Python 3.x
- Pillow library

## Installation

Install the Pillow library using pip:
pip install pillow


How It Works

The tool uses a key to determine the pattern for swapping pixel values. The same key must be used for both encryption and decryption to ensure the processes are consistent.
