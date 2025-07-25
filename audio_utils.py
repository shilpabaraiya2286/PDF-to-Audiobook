from gtts import gTTS
import os
import threading
import platform

AUDIO_FILE = "output.mp3"

def text_to_speech(text, save_only=False):
    tts = gTTS(text)
    tts.save(AUDIO_FILE)
    if save_only:
        return AUDIO_FILE
    return AUDIO_FILE

def play_audio(path):
    def _play():
        if platform.system() == "Windows":
            os.system(f'start {path}')
        elif platform.system() == "Darwin":  # macOS
            os.system(f'open {path}')
        else:  # Linux
            os.system(f'xdg-open {path}')
    threading.Thread(target=_play).start()

def stop_audio():
    print("🔇 Stopping manually not supported in gTTS + default player.")
