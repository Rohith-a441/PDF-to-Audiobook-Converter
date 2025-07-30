# 📚 PDF to Audiobook Converter 🎧

Convert any PDF into an audiobook with a simple and intuitive interface. This Python-based project allows users to upload a PDF file and instantly hear it read out loud using **text-to-speech** (TTS). Designed with accessibility, simplicity, and speed in mind — perfect for visually impaired users, audiobook lovers, or students on the go.

---

## 🔧 Features

- 📄 Upload and extract text from any PDF file.
- 🗣️ Convert extracted text to speech using `pyttsx3`.
- 🎚️ Adjustable speech rate and volume.
- 💡 Clean Tkinter-based GUI for ease of use.
- 💾 Save and play the audio as an `.mp3` file.
- 📷 Includes UI screenshot proofs and demo files.

---

## 📁 Project Structure

```bash
📁 PDF-to-Audiobook-Converter
├── main.py                # Main Python script (GUI + functionality)
├── sample.pdf             # Sample PDF to test audiobook conversion
├── output.mp3             # Output audio file (converted speech)
├── screenshots/           # Screenshot folder for proof and UI view
│   ├── ui_upload.png      # Screenshot of file upload interface              
├── README.md              # Top-level project description and usage
└── requirements.txt       # Required Python dependencies




🔤 File Descriptions
File/Folder	Description
main.py	The core application file. Uses tkinter for GUI, PyMuPDF to extract text, and pyttsx3 to convert it into speech.
sample.pdf	A dummy/test PDF to help demonstrate the functionality of the converter.
output.mp3	The generated speech output file from the sample PDF.
screenshots/	Folder containing screenshots of the UI, upload dialog, and working state of the app.
requirements.txt	Contains all Python packages required to run this project. Easily install via pip.
README.md	This file. Contains documentation and setup steps for the project.




🖥️ Installation
🔹 Step 1: Clone this repository
bash
Copy
Edit
git clone https://github.com/Rohith-a441/PDF-to-Audiobook-Converter.git
cd PDF-to-Audiobook-Converter
🔹 Step 2: Install dependencies
pip install -r requirements.txt




▶️ How to Run
python main.py
A GUI window will open.

Click “Upload PDF” to select a file.

The text will be extracted and read aloud.

You can also save the audio as output.mp3.


🧪 Demo Screenshot Proofs
UI Interface	File Uploaded



💡 Tech Stack
Python 🐍

Tkinter 🎨

pyttsx3 🔊

PyMuPDF (fitz) 📄


👤 Author
Rohith K N


⭐ Final Note
This project was built under personal effort. If you find it helpful, please consider giving a ⭐ on GitHub. It helps a lot!



