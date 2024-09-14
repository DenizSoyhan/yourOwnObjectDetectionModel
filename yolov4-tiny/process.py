import os
import random

# Current directory
image_dir = os.path.dirname(os.path.abspath(__file__))

print(image_dir)

image_dir = 'data/obj'

print(os.listdir(image_dir))
# List all images and ensure each has a corresponding annotation file
images = [f for f in os.listdir(image_dir) if f.endswith('.png')]
images = [img for img in images if os.path.exists(os.path.join(image_dir, img.replace('.png', '.txt')))]

# Shuffle the images
random.shuffle(images)

# Calculate the number of images for each split
num_images = len(images)
num_train = int(num_images * 0.7)
num_val = int(num_images * 0.2)
num_test = num_images - num_train - num_val

# Split the images
train_images = images[:num_train]
val_images = images[num_train:num_train + num_val]
test_images = images[num_train + num_val:]

# Function to write image paths to a file
def write_images_to_file(images, file_path):
    with open(file_path, 'w') as f:
        for img in images:
            f.write(f"{os.path.join(image_dir, img)}\n")

# Write the image paths to their respective files
write_images_to_file(train_images, 'data/train.txt')
write_images_to_file(val_images, 'data/val.txt')
write_images_to_file(test_images, 'data/test.txt')

print(f"Training set: {len(train_images)} samples")
print(f"Validation set: {len(val_images)} samples")
print(f"Test set: {len(test_images)} samples")