# YouTube Live Stream Downloader Script

This script allows you to download the most recent segment of a YouTube live stream and save it to your computer. You can specify the duration of the segment, choose the folder where the video will be saved, and use cookies for live streams that require login.

This script is optimised for MacOS. Windows users should adapt elements of this script for their operating system as needed.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Downloading the Script](#downloading-the-script)
3. [How to Run the Script](#how-to-run-the-script)
4. [Additional Options](#additional-options)
   - [Download a Different Segment Length](#download-a-different-segment-length)
   - [Save the File in a Different Folder](#save-the-file-in-a-different-folder)
   - [Download Live Streams that Require Sign-in](#download-live-streams-that-require-sign-in)
5. [Common Issues](#common-issues)
6. [Example Commands](#example-commands)
7. [Contact for Help](#contact-for-help)

---

## 1. Prerequisites

Before using the script, ensure the following software is installed:

- **Python 3**: You need Python 3 to run the script. Verify by running:
```bash
python3 --version
```

If Python is not installed, download it from python.org.
Alternatively, you can install Python using pip:
```bash
pip install python
```

- **yt-dlp**: This tool downloads YouTube videos. Install it using:
```bash
pip install yt-dlp
```

- **ffmpeg**: This tool is used for managing and editing video files. Install it using:
```bash
brew install ffmpeg
```

For Windows users, follow the installation instructions on the official yt-dlp and ffmpeg websites.

- **YouTube account**: You will need to be logged into a YouTube account. Cookies from your YouTube session are required to access the live stream data.

- **Getcookies.txt**: This Chrome extension is used to save the cookies required to access live stream data. [I use this one](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc), and there are several other extensions that do the same thing available on the Chrome web store. 

---

## 2. Downloading the Script

Clone or download this repository containing the YouTube live stream downloader script to your local machine.

---

## 3. How to Run the Script

After downloading the script, you can run it using the command line.

### Step-by-step:

**1. Open the Terminal**

***macOS/Linux***: Press Command + Space, type "Terminal," and press Enter.

***Windows***: Press Win + R, type "cmd," and press Enter. 

**2.Navigate to the Folder**

  Use the cd command to go to the folder where you saved the script:

```bash
cd /path/to/your/script
```

**3. Basic Command**

  Run the script with the YouTube live stream URL, the duration of the segment you want to download, and the output folder where the video will be saved:

```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --duration 00:05:00 --output-directory ~/Downloads
```

---

## 4. Additional Options

***Download a Different Segment Length***

  You can specify a different segment length using the --duration option. For example, to download the last 10 minutes of the live stream:

```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --duration 00:10:00 --output-directory ~/Downloads
```

	
***Save the File in a Different Folder***

  If you want to save the downloaded video to a different folder, use the --output-directory option:
	
```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --output-directory /path/to/folder
```

***Download Live Streams that Require Sign-in***

  If the live stream requires you to sign in, you will need a cookies.txt file, which contains your authenticated session.

  How to get the cookies.txt file:

  * Use a browser extension such as Get Cookies.txt.

  * Visit YouTube, log in, and use the extension to export your cookies to a cookies.txt file.

  * Once you have the file, pass it to the script using the --cookie-file option:

```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --cookie-file /path/to/cookies.txt --output-directory ~/Downloads
```

  * The cookies.txt file should be updated prior the each execution of this script.

---

## 5. Common Issues

**Error: Please Sign In**

This error means that the live stream requires you to log in. Use the --cookie-file option with the path to your cookies.txt file.

**Error: No such file or directory**

Make sure that the output folder path or the cookies.txt file path is correct and exists.

**Error: Unresolved command**

Ensure that yt-dlp and ffmpeg are properly installed and available in your system's $PATH.

---
	
## 6. Example Commands

**Download the last 5 minutes of a live stream** 

```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --duration 00:05:00 --output-directory ~/Downloads
```

**Download the last 10 minutes and save to a specific folder** 

```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --duration 00:10:00 --output-directory /path/to/folder
```

**Download a live stream with sign-in using cookies**
 
```bash
python3 YTLive.py "https://www.youtube.com/watch?v=your_video_id" --cookie-file /path/to/cookies.txt --duration 00:10:00 --output-directory ~/Downloads
```
  * The /path/to/cookies.txt may be dropped if the cookies.txt file is saved in the same location as the script.

---

## 7. Contact for Help
You can open an issue on the repository.
