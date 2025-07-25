# PDF to Audiobook Converter 

# ✅ Phase 1: Install Requirements
# Run these in your terminal first:
# pip install PyMuPDF pyttsx3 tkinter

import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
import pyttsx3
import os

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1.0)  # Max volume

# Global variable for extracted text
extracted_text = ""

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    global extracted_text
    extracted_text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            extracted_text += page.get_text()
        doc.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract PDF text: {e}")

# Function to play extracted text
def play_audio():
    if extracted_text:
        engine.say(extracted_text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "No text extracted yet.")

# Function to save MP3
def save_audio():
    if not extracted_text:
        messagebox.showwarning("Warning", "No text to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        engine.save_to_file(extracted_text, file_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio saved to {file_path}")

# File Upload Button Handler
def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        extract_text_from_pdf(file_path)
        messagebox.showinfo("Success", "PDF text extracted successfully!")

# GUI Setup
root = tk.Tk()
root.title("PDF to Audiobook Converter")
root.geometry("400x300")

btn_upload = tk.Button(root, text="Upload PDF", command=upload_pdf, width=20, bg="lightblue")
btn_upload.pack(pady=20)

btn_play = tk.Button(root, text="Play Audio", command=play_audio, width=20, bg="lightgreen")
btn_play.pack(pady=10)

btn_save = tk.Button(root, text="Save as MP3", command=save_audio, width=20, bg="orange")
btn_save.pack(pady=10)

lbl_note = tk.Label(root, text="@Elevate Internship Project\nBy YourName", fg="gray")
lbl_note.pack(side="bottom")

root.mainloop()
