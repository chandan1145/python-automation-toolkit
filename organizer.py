import os
import shutil

# Change this to the folder you want to organize
path = r"C:\Users\chand\Downloads"

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Programs": [".exe", ".msi"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} → {folder}")
