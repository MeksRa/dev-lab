import shutil
from pathlib import Path

# Dictionary defining categories and their associated file extensions
FILE_CATEGORIES = {
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".svg",
        ".ico",
        ".bmp",
        ".tiff",
        ".tif",
        ".psd",
        ".ai",
        ".heic",
    },
    "Documents": {
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".xlsx",
        ".xls",
        ".pptx",
        ".ppt",
        ".csv",
        ".md",
        ".rtf",
        ".odt",
        ".epub",
        ".djvu",
    },
    "Archives": {
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
        ".xz",
        ".iso",
        ".cab",
    },
    "Video": {
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".m4v",
        ".mpg",
        ".mpeg",
    },
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus"},
    "Code": {
        ".py",
        ".js",
        ".ts",
        ".html",
        ".css",
        ".json",
        ".xml",
        ".yaml",
        ".yml",
        ".cpp",
        ".c",
        ".h",
        ".java",
        ".go",
        ".rs",
        ".sql",
        ".sh",
        ".bat",
    },
    "Installers": {
        ".exe",
        ".msi",
        ".dmg",
        ".pkg",
        ".deb",
        ".rpm",
        ".AppImage",
    },
}


def get_category(extension: str) -> str:
    """Determines the category folder based on the file extension."""
    ext = extension.lower()  # Normalize to lowercase (e.g., .JPG -> .jpg)

    # Check which category contains the extension
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category  # returns category name

    # Default fallback folder for unknown extensions
    return "Others"


def get_unique_path(destination_path: Path) -> Path:
    """Generates a unique file path if a file with the same name already exists."""
    if not destination_path.exists():
        return destination_path  # If it doesn't exist, returns the original path

    counter = 1
    stem = destination_path.stem  # File name without extension (e.g., 'photo')
    suffix = destination_path.suffix  # File extension (e.g., '.jpg')
    parent = destination_path.parent  # Folder path

    # Loop until we find a free filename (e.g., photo_1.jpg, photo_2.jpg)
    while True:
        new_path = parent / f"{stem}_{counter}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1


def sort_files(source_path: Path) -> None:
    """Scans the source directory and moves files into categorized subfolders."""

    # Iterate through all items in the target directory
    for file_path in source_path.iterdir():
        # Process files only (ignore subdirectories and hidden files)
        if file_path.is_file() and not file_path.name.startswith("."):
            ext = file_path.suffix
            category = get_category(ext)

            # Create target category folder inside the source directory if it doesn't exist
            target_folder = source_path / category
            target_folder.mkdir(exist_ok=True)

            # Ensure unique file name to avoid overwriting conflicts
            target_path = get_unique_path(target_folder / file_path.name)

            # Move the file to its new categorized location
            shutil.move(str(file_path), str(target_path))
            print(f"Moved: {file_path.name} -> {category}/")


def main() -> None:
    """Main entry point of the script."""
    user_input = input("Enter the path of the directory to sort: ").strip()
    source_path = Path(user_input)

    # Validate that the provided path exists and is a directory
    if source_path.exists() and source_path.is_dir():
        print("\nStarting sorting process...")
        sort_files(source_path)
        print("\nSorting completed successfully!")
    else:
        print("Error: The specified path does not exist or is not a directory.")


if __name__ == "__main__":
    main()
