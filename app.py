from flask import Flask, request, render_template, jsonify, session, send_from_directory
from werkzeug.utils import secure_filename
import os
import fitz  # PyMuPDF
import pyttsx3  # Offline voice

app = Flask(__name__)
app.secret_key = "secret123"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()

    session['text'] = text.strip()

    if not text.strip():
        return jsonify({"message": "❌ No readable text found in PDF."}), 400

    return jsonify({"message": "✅ File uploaded successfully!"})

@app.route('/play', methods=['POST'])
def play_audio():
    text = session.get('text', '')
    if not text:
        return jsonify({"message": "⚠️ No text loaded."}), 400

    audio_path = os.path.join(UPLOAD_FOLDER, "temp_play.mp3")
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1.0)  # Max volume

    # Optional: Set voice (male/female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # voices[0] = male (default), voices[1] = female

    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return jsonify({"message": "▶️ Offline voice ready!", "url": "/temp_audio"})

@app.route('/temp_audio')
def temp_audio():
    return send_from_directory(UPLOAD_FOLDER, "temp_play.mp3")

@app.route('/save', methods=['POST'])
def save_audio():
    text = session.get('text', '')
    if not text.strip():
        return jsonify({"message": "⚠️ No text to convert"}), 400

    audio_path = os.path.join(UPLOAD_FOLDER, "output.mp3")

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can switch to voices[1] for female

    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return jsonify({"message": "💾 MP3 file saved successfully!"})

@app.route('/download')
def download():
    return send_from_directory(UPLOAD_FOLDER, "output.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
