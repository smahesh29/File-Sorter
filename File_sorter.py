import os
import shutil
import zipfile

def get_size(directory):
    """Return the total size of the directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def ensure_directory_exists(path):
    """Create the directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def zip_dir(directory, zip_filename):
    """Create a zip file from the contents of a directory."""
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=directory)
                zipf.write(file_path, arcname)

# Define the paths
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
directories = {
    'Images': os.path.join(downloads_dir, 'Images'),
    'Text': os.path.join(downloads_dir, 'Text'),
    'Videos': os.path.join(downloads_dir, 'Videos'),
    'Sounds': os.path.join(downloads_dir, 'Sounds'),
    'Applications': os.path.join(downloads_dir, 'Applications'),
    'Codes': os.path.join(downloads_dir, 'Codes'),
    'Others': os.path.join(downloads_dir, 'Others')
}

# Define file extensions
file_categories = {
    'Images': [".jpeg", ".png", ".jpg", ".gif", ".bmp", ".tiff", ".webp", ".ico", ".svg", ".heif", ".jfif", ".raw", ".indd", ".ai", ".eps"],
    'Text': [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf", ".md", ".odt", ".csv", ".tsv", ".tex", ".log", ".json", ".yaml", ".xml"],
    'Videos': [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".mts", ".m2ts", ".3gp", ".rm", ".rmvb", ".vob"],
    'Sounds': [".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".opus", ".wma", ".aiff", ".cda"],
    'Applications': [".exe", ".lnk", ".app", ".bat", ".sh", ".apk", ".jar", ".msi", ".run", ".pkg", ".dmg"],
    'Codes': [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".go", ".h", ".asm", ".rs", ".swift", ".kt", ".pl", ".lua", ".sh", ".v", ".r", ".scala", ".groovy", ".clj", ".dart", ".yaml", ".coffee", ".m", ".xsl", ".sml", ".ml", ".fs", ".ts"]
}

# Get size of the Downloads directory
dir_size = get_size(downloads_dir)
print(f"Size of Downloads directory: {dir_size / (1024 * 1024):.2f} MB")

# Check if the size is greater than 100 MB
if dir_size > 100 * 1024 * 1024:
    print("The Downloads folder is larger than 100 MB. Skipping zip file creation.")
    create_zipfile = 'n'
else:
    create_zipfile = input("Create a download zip file? [Y/N]: ")

if create_zipfile.lower() == 'y':
    try:
        print("Creating zip file...")
        zip_filename = os.path.join(downloads_dir, 'Downloaded_Files.zip')
        zip_dir(downloads_dir, zip_filename)
        print(f"Download zip file created successfully: {zip_filename}")
    except Exception as e:
        print(f"An error occurred while creating the zip file: {e}")

# Ask if the user wants to create missing folders
print("Warning: Ensure that the following folders exist before running this script:")
print(" - Images")
print(" - Text")
print(" - Videos")
print(" - Sounds")
print(" - Applications")
print(" - Codes")
print(" - Others")
create_folders = input("Create missing folders if they don't exist? [Y/N]: ")
if create_folders.lower() == 'y':
    for path in directories.values():
        ensure_directory_exists(path)
    print("Missing folders created.")

# Confirm that the user is ready to proceed with sorting
confirm_sort = input("Proceed with sorting the files? [Y/N]: ")
if confirm_sort.lower() == 'y':
    print("Starting file sorting...")
    files = os.listdir(downloads_dir)
    for file in files:
        file_path = os.path.join(downloads_dir, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_categories.items():
                if any(file.endswith(ext) for ext in extensions):
                    dest = directories[category]
                    try:
                        print(f"Moving {file} to {category}...")
                        shutil.move(file_path, os.path.join(dest, file))
                        moved = True
                        break
                    except Exception as e:
                        print(f"An error occurred while moving file {file} to {category}: {e}")
            if not moved:
                try:
                    print(f"Moving {file} to Others...")
                    shutil.move(file_path, os.path.join(directories['Others'], file))
                except Exception as e:
                    print(f"An error occurred while moving file {file} to 'Others': {e}")

    print("Sorting Completed...")
else:
    print("Sorting canceled.")
