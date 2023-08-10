import random, hashlib
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Read the .txt file that contains words from Arts 1 modules
with open('arts1_modules.txt', 'r') as file:
    text = file.read()
    words = text.split()

# "Clean" each word by removing punctuations and symbols
cleaned_words = []
for word in words:
    cleaned_words.append(''.join(char for char in word if char.isalnum()))
cleaned_words = [word for word in cleaned_words if word]

# Output poem should consist of 8 lines with 8 words each
poem = ""
for i in range(8):
    for j in range(8):
        # Words are chosen and removed from the word pool at random
        next_word = random.choice(cleaned_words)
        cleaned_words.remove(next_word)
        poem += next_word + " "
    poem += "\n"

# Display resulting Dadaist poem
print(poem) 

# Convert each word in the poem to a hex code
poem = poem.split(" ")
hex_codes = []
for word in poem:
    md5_hash = hashlib.md5(word.encode()).hexdigest()
    hex_codes.append(md5_hash[:6])

# Generate each hex code as a 16x16 pixel
grid_size = (8, 8)
image_size = (grid_size[0] * 16, grid_size[1] * 16)
image = Image.new("RGB", image_size, "white")
for y in range(grid_size[1]):
    for x in range(grid_size[0]):
        hex = "#" + hex_codes[y * grid_size[0] + x]
        draw = ImageDraw.Draw(image)
        draw.rectangle([x * 16, y * 16, (x + 1) * 16, (y + 1) * 16], fill=hex)
plt.imshow(image)
plt.axis('off')

# Display the image
plt.show()