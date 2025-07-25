// Get DOM elements
const playBtn = document.getElementById("playBtn");
const stopBtn = document.getElementById("stopBtn");
const saveBtn = document.getElementById("saveBtn");
const listenBtn = document.getElementById("listenBtn");
const pdfInput = document.getElementById("pdfFile");
const audio = document.getElementById("audioPlayer");

// Utility: Get current time
function getCurrentTime() {
  const now = new Date();
  return now.toLocaleTimeString();
}

// Show message in alert box
function showMessage(message, type = "info", iconClass = "") {
  const box = document.getElementById("messageBox");
  const text = document.getElementById("messageText");

  box.className = "alert alert-" + type;
  text.innerHTML = `<i class="${iconClass} me-2"></i>${message} <span class="float-end text-muted">${getCurrentTime()}</span>`;
  box.classList.remove("d-none");

  setTimeout(() => {
    box.classList.add("d-none");
  }, 5000);
}

// 📄 Upload PDF
pdfInput.addEventListener("change", () => {
  const file = pdfInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then(res => res.json())
    .then(data => {
      showMessage(data.message || "✅ PDF uploaded successfully!", "success", "fas fa-check-circle");
    })
    .catch(() => {
      showMessage("❌ Failed to upload PDF", "danger", "fas fa-exclamation-circle");
    });
});

// ▶️ Play Button
playBtn.addEventListener("click", () => {
  showMessage("▶️ Playing audio...", "info", "fas fa-play-circle");

  fetch("/play", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      showMessage(data.message || "Audio is playing!", "success", "fas fa-volume-up");

      // Play the gTTS audio (girl voice)
      if (data.url) {
        audio.src = data.url;
        audio.play();
      }
    })
    .catch(() => {
      showMessage("❌ Could not play audio", "danger", "fas fa-times-circle");
    });
});

// ⏹️ Stop Button
stopBtn.addEventListener("click", () => {
  audio.pause();
  audio.currentTime = 0;
  showMessage("⏹️ Audio stopped", "warning", "fas fa-stop-circle");
});

// 💾 Save Button
saveBtn.addEventListener("click", () => {
  showMessage("💾 Saving audio...", "primary", "fas fa-save");

  fetch("/save", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      showMessage(data.message || "Audio saved!", "success", "fas fa-download");
    })
    .catch(() => {
      showMessage("❌ Could not save audio", "danger", "fas fa-times-circle");
    });
});

// 🎧 Listen Button
listenBtn.addEventListener("click", () => {
  showMessage("🎧 Listening to MP3...", "success", "fas fa-headphones");
  window.open("/download");
});
