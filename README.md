# 🎙️ Whisper Batch Transcriber

This Python script automates **speech-to-text transcription** for multiple audio files using [OpenAI Whisper](https://github.com/openai/whisper).  
It scans an `audio/` folder for supported files, transcribes them, and saves all results into a single CSV file.

---
<br>

## Features

- Automatically detects all audio files in the `audio/` folder
- Uses OpenAI’s **Whisper** model for accurate transcription
- Supports multiple audio formats (`.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`, `.webm`)  
- Saves transcripts neatly in a `transcripts.csv` file
- Flushes results to disk after every file (prevents data loss)  
- Displays progress and elapsed time  

---
<br>

## Requirements

- **Python 3.8+**
- **Dependencies:**
  ```bash
  pip install openai-whisper

  pip install torch  # required backend for Whisper
  ```
(If using GPU, install the CUDA-enabled version of PyTorch)

---
<br>

## Installing the Open-Source Whisper Module (Manual Method)

If you want to manually install Whisper from source, follow these steps:

 Download Whisper from GitHub:
🔗 https://github.com/openai/whisper

Extract the downloaded ZIP and navigate to the folder:
whisper-main

Install locally using PowerShell or VS Code terminal:

  ```bash
cd C:\Users\User\Downloads\whisper-main
pip install -e .
  ```

Alternatively, install dependencies manually:

  ```bash
pip install -r requirements.txt
  ```
OR

  ```bash
pip install openai-whisper
  ```
✅ This automatically installs all required dependencies, including:
  ```bash
numba
numpy
torch
tqdm
more-itertools
tiktoken
  ```

⚠️ Note:
On Linux (x86_64), it may also install triton>=2.0.0 if supported by your system.
<br>You do not need to install these manually unless building from source.

---
<br>

## Installing FFmpeg (Required for Audio Processing)

Download FFmpeg from:
🔗 https://ffmpeg.org/download.html#build-windows

Extract the files and move the folder to:

  ```bash
C:\ffmpeg
  ```

Add FFmpeg to your system environment variables:
<br>Go to: Control Panel → System → Advanced System Settings → Environment Variables
<br>Under User variables, find Path

Add:

  ```bash
C:\ffmpeg\bin
  ```

Verify installation:

  ```bash
ffmpeg -version
  ```

---
<br>

## 📁 Folder Structure
project/
<br>│
<br>├── audio/              # Folder containing your audio files
<br>│       ├── example1.mp3
<br>│       ├── example2.wav
<br>│
<br>├── transcripts.csv     # Generated output (after running the script)
<br>│
<br>└── transcribe.py       # The main script

---
<br>

## Usage
Clone the repository:

  ```bash
git clone https://github.com/monojitbgit/whisper-batch-transcriber.git
cd whisper-batch-transcriber
  ```

Place your audio files inside the audio/ folder.

Run the script:
  ```bash
python transcribe.py
  ```

---
<br>

## Model Details

By default, the script loads the medium Whisper model:
  ```bash
model = whisper.load_model("medium")
  ```

To use a different model:
  ```bash
model = whisper.load_model("small")
  ```

Change the transcription language by adjusting:
  ```bash
transcribe_file(file_path, language="en")
  ```
(Replace "en" with your desired ISO language code.)

---
<br>

## Notes

Whisper runs locally — no API key required
<br>For faster performance, use a GPU (CUDA-compatible)
<br>Large models need more memory — try small or base if you get CUDA out of memory

---
<br>

## ⚖️ Whisper Model Comparison

| Option | Speed | Accuracy | Model | ⏱️ CPU (Intel-i7/Ryzen-7) | ⚙️ GPU (RTX 3060/3090/4090) | Size | Speed (Relative) | Accuracy (Relative) | 🌐 Multilingual Support |
|--------|--------|-----------|--------|------------------------------|-----------------------------|-------|------------------|----------------------|--------------------------|
| Use `"tiny"` | Fast | Low accuracy | `tiny` | ~30 sec | ~5–10 sec | 75 MB | ⭐⭐⭐⭐ (Fastest) | ⭐ (Basic) | ✅ Yes |
| Use `"base"` | Fast | Low accuracy | `base` | ~1 min | ~10–20 sec | 142 MB | ⭐⭐⭐ (Fast) | ⭐⭐ (Good) | ✅ Yes |
| Use `"small"` with CPU optimizations | Faster | Good | `small` | ~2–3 min | ~20–30 sec | 466 MB | ⭐⭐ (Medium) | ⭐⭐⭐ (Better) | ✅ Yes |
| Use `"medium"` after reducing file size | Slow | Better | `medium` | ~5–6 min | ~40–60 sec | 1.5 GB | ⭐ (Slower) | ⭐⭐⭐⭐ (Very Good) | ✅ Yes |
| Use Google Colab GPU (`medium` / `large`) | Super Fast | Best | `large` | ~10–15 min | ~1.5–2 min | 3.0 GB | ⭐ (Slowest) | ⭐⭐⭐⭐⭐ (Best) | ✅ Yes |

---
<br>

## 💡 Recommendations

- 🧠 **For quick tests:** Use `tiny` or `base`  
- ⚖️ **For balance (speed + accuracy):** Use `small`  
- 🗣️ **For high-quality transcription:** Use `medium`  
- 🚀 **For best performance:** Use `large` on GPU or Google Colab  

---
<br>

## License

This project is licensed under the MIT License.
<br>You’re free to use, modify, and distribute it with attribution.
