
# 🎥 YT SCREEN CAPTURE CLI — Record Videos Like a User, Not a Pirate 🚫🏴‍☠️

## ABOUT:
 This tool records your screen while a video plays in your browser.
 It does NOT download videos. It captures your screen like OBS or a camera.
 Legal and ethical. No piracy. No bullshit.

## REQUIREMENTS:
 - Python 3.7 or higher
 - ffmpeg (must be installed and available in PATH)
 - pip install selenium

## INSTALL DEPENDENCIES:

### Install selenium:
```bash
 pip install selenium
```
### Install ffmpeg:
#### Arch / Garuda:
```bash
 sudo pacman -S ffmpeg
```
#### Debian / Ubuntu:
```bash
 sudo apt install ffmpeg
```
## HOW TO USE:
 1. Run the script
```bash
    python3 yt_screen_capture.py
```
 2. Paste the video URL (YouTube or any streamable link)

 3. Enter how many seconds you want to record

 4. Your browser will open automatically

 5. After 5 seconds, screen recording starts (both video + audio)

 6. Output saved in:
```bash
    recordings/recording_YYYY-MM-DD_HH-MM-SS.mp4
```
## EXAMPLE RUN:
```bash
 python3 yt_screen_capture.py
```
### Paste this test link:
```bash
 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
## TROUBLESHOOTING:

 - Recording blank screen?
   → Check your DISPLAY and PulseAudio settings (Linux)

 - ffmpeg not found?
   → Make sure it's installed and added to your PATH

 - Browser not opening?
   → Check your default browser or use selenium + ChromeDriver

## NOTES:

 - Uses ffmpeg for screen + audio recording
 - Uses selenium to auto-open video link
 - Uses subprocess and datetime to organize filenames
 - Can be extended for window-only capture, mic toggle, etc

## LEGAL:

 ⚠️ This tool is 100% legal if used for:
     - Personal recordings
     - Educational use
     - Saving open media for offline use

 ❌ This is NOT a YouTube downloader
 ✅ This is a screen recorder, like OBS, just CLI

## EXTEND IDEAS:

 - Add GUI with tkinter or PyQt
 - Record specific window (e.g. Chrome only)
 - Auto-trim silence
 - Upload output to Google Drive
 - Add keyboard shortcut to stop recording early


 You don’t need to pirate when you can automate legally.
 This is elite engineering.  
 No bs. No broken laws.  
 Just pure workflow domination 🧠⚙️🔥
```
