import shutil
import logging
import sys
from pathlib import Path

# Default Folder
FOLDER_NAME = "TestFolder"


def organize_files():
    try:
        # Logging Configuration
        logging.basicConfig(
            filename="organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

        # Folder Selection
        if len(sys.argv) > 1:
            folder = Path(sys.argv[1])
        else:
            folder = Path(FOLDER_NAME)

        print("=" * 40)
        print("      FILE ORGANIZER v2.0")
        print("=" * 40)
        print(f"Scanning Folder: {folder}")
        print()

        if not folder.exists():
            print("Folder not found!")
            return

        moved_files = 0
        summary = {}

        file_types = {
            ".jpg": "Images",
            ".png": "Images",
            ".pdf": "Documents",
            ".txt": "Documents",
            ".mp3": "Music",
            ".mp4": "Videos",
            ".exe": "Executables",
            ".zip": "Archives",
            ".py": "Python Files",
            ".csv": "Data",
        }

        for file in folder.iterdir():
            if file.is_file():

                folder_name = file_types.get(file.suffix.lower(), "Others")
                destination = folder / folder_name

                destination.mkdir(exist_ok=True)

                shutil.move(str(file), str(destination / file.name))

                # Logging
                logging.info(f"Moved {file.name} -> {folder_name}")

                moved_files += 1
                summary[folder_name] = summary.get(folder_name, 0) + 1

        print(f"\nFiles Organized: {moved_files}")

        print("\n========== SUMMARY ==========")
        for category, count in summary.items():
            print(f"{category:<15}: {count}")

        print("-" * 28)
        print(f"Total Files    : {moved_files}")
        print("=" * 28)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    organize_files()