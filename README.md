# 📁 file-organizer
A simple Python script to automatically organize files into folders based on their type (four categories).
Images (.jpeg, .jpg, .png, .gif)
Videos (.mp4, .mkv, .mov)
Documents (.pdf, .docx, .txt)
Others (any other file types)

## 🔧 Features
- Automatically detects file types
- Moves files into respective folders
- Creates folders if they don’t exist
- Simple to use and modify

## 🚀 How to Use
1. Clone or download this repository
2. Run the script:

Example Before and After
Before:
./
├── photo.jpg
├── video.mp4
├── resume.pdf
├── script.py

After:
./
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
├── Documents/
│   └── resume.pdf
├── Others/
│   └── script.py

🐛 Error Handling
Any issues while moving files (like permission errors or file in use) will be printed with a message.

💡 Future Improvements (Optional for README)
You can enhance this script later with:
Logging system
Drag & drop GUI using Tkinter
Custom file extensions from the user
Progress bar using tqdm

Author: @afzalmohamedofficial

```bash
python organize_files.py

