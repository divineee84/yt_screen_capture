
# YT SCREEN CAPTURE CLI

# ABOUT:
# This tool records your screen while a video plays in your browser.
# It does NOT download videos. It captures your screen like OBS or a camera.
# Legal and ethical. No piracy. No bullshit.

# REQUIREMENTS:
# - Python 3.7 or higher
# - ffmpeg (must be installed and in system PATH)
# - Python module: selenium

# INSTALL DEPENDENCIES:
# Install selenium (Python package)
```bash
pip install selenium
```
# INSTALL FFMPEG:
# Arch / Garuda Linux:
```bash
sudo pacman -S ffmpeg
```
# Debian / Ubuntu:
```bash
sudo apt install ffmpeg
```
# HOW TO USE:
# 1. Run the script
```bash
python3 yt_screen_capture.py
```
# 2. Paste the video URL (YouTube or any browser-playable link)

# 3. Enter how many seconds you want to record

# 4. It will open the browser and wait 5 seconds

# 5. Then it starts screen recording with audio

# 6. Output saved in:
```bash
# recordings/recording_YYYY-MM-DD_HH-MM-SS.mp4
```
# EXAMPLE RUN:
```bash
python3 yt_screen_capture.py
```
# TEST LINK (for respect):
```bash  
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
# TROUBLESHOOTING:
# - Blank video? → Check DISPLAY and PulseAudio setup
# - ffmpeg not found? → Install and make sure it's in PATH
# - Browser not opening? → Check your system’s default browser or use ChromeDriver

# NOTES:
# - Uses ffmpeg to capture screen and system audio
# - Uses Python's selenium to open video link
# - Auto-names files using datetime
# - You can extend this with GUI, webcam overlay, etc.

# LEGAL:
# - This tool does NOT download any videos
# - It only records your screen, just like OBS
# - Legal for:
#   - Personal notes
#   - Education
#   - Tutorials
# - Illegal use = your responsibility

# FEATURE IDEAS:
# - Record only selected window
# - GUI version with tkinter
# - Webcam + mic overlay
# - One-click upload to Google Drive
# - Stop recording with keypress

# FINAL MESSAGE FROM WOXXY:
# This ain't piracy. This is automation.
# Don’t beg YouTube — outsmart it legally.
# Respect creators. Respect the grind.
# Build tools that make your workflow God-tier.

