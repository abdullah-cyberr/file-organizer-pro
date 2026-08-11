# 📂 File Organizer v2.0

A Python command-line tool that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

* Automatically organizes files by extension
* Supports multiple file categories:

  * Images
  * Documents
  * Music
  * Videos
  * Archives
  * Executables
  * Python Files
  * Data
* Moves unknown file types into an `Others` folder
* Generates a summary report after organization
* Maintains an `organizer.log` logging file
* Includes exception handling
* Supports a configurable default folder
* Supports command-line folder arguments

## 🛠️ Technologies

* Python 3.14
* `pathlib`
* `shutil`
* `logging`
* `sys`

The project uses Python's standard library and does not require third-party dependencies.

## ▶️ Usage

Run the organizer using the default configured folder:

```bash
py organizer.py
```

Or provide a folder path through the command line:

```bash
py organizer.py "D:\MyFolder"
```

The tool scans the selected folder and organizes files into category-based directories according to their file extensions.

## 📊 Example Output


```text
========================================
      FILE ORGANIZER v2.0
========================================
Scanning Folder: TestFolder

Files Organized: 5

========== SUMMARY ==========
Images         : 2
Documents      : 1
Music          : 1
Others         : 1
-----------------------------
Total Files    : 5
============================
```
## 📁 Project Structure

```text
│
├── organizer.py
├── organizer.log
├── README.md
├── LICENSE
└── .gitignore

```

This project demonstrates practical Python skills including:

* File and directory handling
* File extension-based classification
* Command-line argument handling
* Logging
* Exception handling
* Automation using Python's standard library

## 👤 Author

**Abdullah Al Sadat**
