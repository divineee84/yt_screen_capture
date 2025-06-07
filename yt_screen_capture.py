import subprocess
import webbrowser
import time
from datetime import datetime
import os
import shutil

# Check if ffmpeg is installed
if not shutil.which("ffmpeg"):
    print("❌ ffmpeg not found. Please install it first.")
    exit(1)

def record_screen(duration, filename):
    """Start ffmpeg screen recording for the given duration."""
    save_dir = "recordings"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)

    command = [
        "ffmpeg",
        "-y",  # Overwrite output file
        "-video_size", "1920x1080",  # adjust to your screen size
        "-framerate", "30",
        "-f", "x11grab",  # for Linux; use "gdigrab" for Windows
        "-i", ":0.0",     # display capture for Linux
        "-f", "pulse",    # audio input (Linux PulseAudio)
        "-i", "default",
        "-t", str(duration),
        "-vcodec", "libx264",
        "-preset", "fast",
        "-acodec", "aac",
        filepath
    ]

    print(f"🎥 Recording screen for {duration} seconds... Saving to {filepath}")
    subprocess.run(command)
    print("✅ Recording complete.")

def main():
    print("\n🔥 YT SCREEN CAPTURE CLI 🔥")
    url = input("Paste the video URL: ").strip()
    duration = int(input("How long to record? (in seconds): ").strip())
    
    print("🌐 Opening browser...")
    webbrowser.open(url)
    print("⌛ Starting recording in 5 seconds... Get ready.")
    time.sleep(5)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"recording_{timestamp}.mp4"
    record_screen(duration, filename)

if __name__ == "__main__":
    main()
