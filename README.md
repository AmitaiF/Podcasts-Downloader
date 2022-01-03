# Podcasts Downloader

A simple command-line tool that can help you download your favorite podcasts!

## Installation
1. Download the project. You can download a zip file, or you can clone it:
```
git clone https://github.com/AmitaiF/Podcasts-Downloader.git
```
2. Navigate to the folder you have cloned, and download the required libraries:
```
pip install -r requirements.txt
```
3. Download ffmpeg: https://www.ffmpeg.org/download.html

## Usage
1. Navigate to the folder containing the main.py file.
2. Make sure the ffmpeg.exe you downloaded is in this directory.
3. To download all episodes of your favorite podcast, run:
```
python main.py -name podcast_name -dir dir_for_podcasts
```
**Note:** the name you provide should be the exact name of the podcast.

3. For more information and options, watch the help message:
```
python main.py -h
```
4. Enjoy!

## What's next?
For now, the downloader is extremely basic, and it can download only podcasts that host on "omnycontent.com" servers.  
Also, the downloader isn't tested entirely and might have some bugs.  
So, the next steps:
- [ ] Handle edge cases
- [ ] Add support to all podcasts (not only podcasts from omnycontent.com)
- [ ] Make the tool cross-platform
- [ ] Add a GUI
