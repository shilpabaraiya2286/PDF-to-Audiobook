# PDF-to-Audiobook



# 📚 PDF to Audiobook Converter

Convert any PDF file into a spoken audiobook using Python. This project extracts text from PDF files and uses Text-to-Speech (TTS) to convert it into clear, audible speech — making it easier for students, visually impaired users, or audiobook lovers to listen to documents.

---

## ✨ Features

- 📤 Upload any PDF file.
- 🔊 Convert and play text as audio using **pyttsx3** (offline TTS).
- 💾 Save the audio as an MP3 file.
- 📥 Download the converted MP3.
- 💻 User-friendly web interface with Flask and Bootstrap.

---

## 🛠️ Technologies Used

| Component        | Technology       |
|------------------|------------------|
| Backend          | Flask (Python)   |
| PDF Reading      | PyMuPDF (`fitz`) |
| Text to Speech   | pyttsx3 (offline)|
| Frontend         | HTML, CSS, JS, Bootstrap |
| File Handling    | werkzeug, Flask sessions |

---

## 📁 Project Structure

```
pdf-to-audiobook/
│
├── app.py                  # Flask backend
├── uploads/                # Folder for PDF and MP3 files
├── templates/
│   └── index.html          # Main frontend HTML page
├── static/
│   └── Script.js           # JavaScript for UI interactions
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 🚀 How to Run the App

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/pdf-to-audiobook.git
cd pdf-to-audiobook
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

> Example `requirements.txt`:
```
Flask
PyMuPDF
pyttsx3
Werkzeug
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in Browser

Visit [http://localhost:5000](http://localhost:5000) and use the app.

---

## 📸 Screenshots (Optional)

> You can add screenshots of the upload/play/save/download interface here.

