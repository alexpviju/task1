import os
import shutil

# Define your source and target paths
SOURCE_TRAIN = "C:/Users/viju1/Desktop/img classification/cats_dogs_light/train"
SOURCE_VALID = "C:/Users/viju1/Desktop/img classification/cats_dogs_light/test"
TARGET = "cifar2"

# Create folders
for split in ["train", "valid"]:
    for cls in ["cat", "dog"]:
        os.makedirs(os.path.join(TARGET, split, cls), exist_ok=True)

# Helper to collect and copy images
def filter_and_copy(src_folder, target_folder, prefix, count):
    files = sorted([f for f in os.listdir(src_folder) if f.startswith(prefix) and f.endswith('.jpg')])
    copied = 0
    for i, fname in enumerate(files):
        src = os.path.join(src_folder, fname)
        dst = os.path.join(target_folder, f"{i}.jpg")
        try:
            shutil.copy2(src, dst)
            copied += 1
            if copied >= count:
                break
        except Exception as e:
            print(f"Error copying {fname}: {e}")

# Copy 50 from train/
filter_and_copy(SOURCE_TRAIN, f"{TARGET}/train/cat", "cat.", 50)
filter_and_copy(SOURCE_TRAIN, f"{TARGET}/train/dog", "dog.", 50)

# Copy 50 from test/
filter_and_copy(SOURCE_VALID, f"{TARGET}/valid/cat", "cat.", 50)
filter_and_copy(SOURCE_VALID, f"{TARGET}/valid/dog", "dog.", 50)

print("✅ Dataset structured successfully in ./cifar2/")
