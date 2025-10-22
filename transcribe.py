import os
import csv
import whisper
import time

# Load Whisper model
model = whisper.load_model("medium")

def transcribe_file(file_path, language="en"):
    result = model.transcribe(file_path, language=language)
    return result["text"]

def format_time(seconds):
    mins, secs = divmod(int(seconds), 60)
    return f"{mins}m {secs}s"

def main():
    audio_folder = "audio"
    output_csv = "transcripts.csv"

    audio_files = [
        f for f in os.listdir(audio_folder)
        if f.lower().endswith((".mp3", ".wav", ".m4a", ".flac", ".ogg", ".webm"))
    ]

    total_files = len(audio_files)
    if total_files == 0:
        print("❌ No audio files found in 'audio' folder.")
        return

    print(f"📂 Total {total_files} files found in '{audio_folder}'")

    start_time = time.time()

    # 👇 Set buffering to 1 for line buffering (or use 0 for no buffering if needed)
    with open(output_csv, mode="w", newline="", encoding="utf-8", buffering=1) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "transcript"])
        csvfile.flush()
        os.fsync(csvfile.fileno())

        for idx, filename in enumerate(audio_files, start=1):
            file_path = os.path.join(audio_folder, filename)
            print(f"\n🎙️ Transcribing {idx}/{total_files}: {filename}")

            try:
                transcript = transcribe_file(file_path, language="en")
                writer.writerow([filename, transcript])

                # 👇 Force flush to disk
                csvfile.flush()
                os.fsync(csvfile.fileno())

                elapsed = time.time() - start_time
                print(f"✅ Done {idx}/{total_files} | Elapsed time: {format_time(elapsed)}")
                print(f"⏱️ Total elapsed so far: {format_time(elapsed)}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

    total_elapsed = time.time() - start_time
    print(f"\n🏁 All {total_files} files processed in {format_time(total_elapsed)}")
    print(f"📄 Transcripts saved in {output_csv}")

if __name__ == "__main__":
    main()
