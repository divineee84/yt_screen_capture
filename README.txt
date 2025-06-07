# YT SCREEN CAPTURE CLI

## About
This is a CLI tool that records your screen while a video plays in your browser — like a YouTube video. It does **not download** any copyrighted content — it simply records your screen legally like OBS does.

## Requirements
- Python 3.7+
- ffmpeg installed and available in PATH
- pip install selenium

## How to Use
1. Run the script
2. Paste the video URL
3. Choose how long to record (in seconds)
4. It will open the video and start screen recording
5. Output file is saved in `recordings/`

## Install ffmpeg (Linux):
```bash
sudo pacman -S ffmpeg     # Arch/Garuda
sudo apt install ffmpeg   # Debian/Ubuntu
```

## Run the script
```bash
python3 yt_screen_capture.py
```
### 🧪 Test it like a pro:
```bash 
python3 yt_screen_capture.py
```
### Paste this URL to test:
```bash
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

# 🧨 Final Note:

You’re not hacking or downloading YouTube directly. This tool is fully legal if used ethically. Like OBS, it just records your screen while a video plays.
