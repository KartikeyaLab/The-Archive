import os

def smart_rename(folder_path):
    # Supported formats
    image_exts = {'.png', '.jpg', '.jpeg', '.webp'}
    video_exts = {'.mp4', '.avi', '.mov', '.mkv'}

    files = os.listdir(folder_path)

    images = []
    videos = []
    others = []

    # Separate files
    for file in files:
        full_path = os.path.join(folder_path, file)

        if not os.path.isfile(full_path):
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in image_exts:
            images.append(file)
        elif ext in video_exts:
            videos.append(file)
        else:
            others.append(file)

    # Sort for consistency
    images.sort()
    videos.sort()

    # Rename images
    for i, file in enumerate(images, start=1):
        ext = os.path.splitext(file)[1]
        new_name = f"img_{i:03d}{ext}"

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

    # Rename videos
    for i, file in enumerate(videos, start=1):
        ext = os.path.splitext(file)[1]
        new_name = f"vid_{i:03d}{ext}"

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

    print("✅ Renaming completed!")
    print(f"Images: {len(images)} | Videos: {len(videos)} | Others untouched: {len(others)}")


# 🔹 Usage
folder = "Drawing"
smart_rename(folder)