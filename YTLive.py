import os
import sys
import subprocess
import argparse

def download_recent_segment(livestream_url, output_directory, duration="00:10:00", cookie_file=None):
    """
    Downloads the most recent segment of a YT live and saves it to the specified directory.

    Args:
        livestream_url (str): URL of the YT live.
        output_directory (str): Directory where the live stream will be saved.
        duration (str): Duration of the segment to download in HH:MM:SS format (default: 10 minutes).
        cookie_file (str): Path to cookies.txt file for authentication (default: None).
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Define the output file path
    output_file = os.path.join(output_directory, "recent_segment.mp4")

    # Create the yt-dlp command to download the most recent segment
    yt_dlp_command = [
        "yt-dlp", "--live-from-start", "--downloader", "ffmpeg",
        "--downloader-args", f"ffmpeg_i:-t {duration}", livestream_url, "-o", output_file
    ]

    # Add cookies.txt if provided
    if cookie_file:
        yt_dlp_command += ["--cookies", cookie_file]

    # Run yt-dlp command to download the recent segment
    print(f"Downloading the most recent segment of duration {duration} from {livestream_url}...")
    try:
        subprocess.run(yt_dlp_command, check=True)
        print(f"Download complete! Video saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading live stream: {e}")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download the most recent segment of a YouTube live stream.")
    parser.add_argument("url", help="URL of the YouTube live stream")
    parser.add_argument("--output-directory", default=os.path.expanduser("~/Downloads"),
                        help="Directory to save the live stream (default: ~/Downloads)")
    parser.add_argument("--duration", type=str, default="00:10:00",
                        help="Duration of the segment to download in HH:MM:SS format (default: 10 minutes)")
    parser.add_argument("--cookie-file", type=str, help="Path to cookies.txt file for authentication")

    # Parse arguments
    args = parser.parse_args()

    # Download the most recent segment
    download_recent_segment(args.url, args.output_directory, args.duration, args.cookie_file)

if __name__ == "__main__":
    main()
