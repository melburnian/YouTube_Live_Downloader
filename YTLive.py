import os
import sys
import subprocess
import argparse
import time


def extract_stream_url(livestream_url, cookie_file=None):
    """
    Extract the direct live stream URL using yt-dlp with optional cookies.

    Args:
        livestream_url (str): URL of the YT live stream.
        cookie_file (str): Path to cookies.txt file for authentication (default: None).

    Returns:
        str: The direct stream URL.
    """
    yt_dlp_command = ["yt-dlp", "-g", livestream_url]

    # Add cookies.txt if provided
    if cookie_file:
        yt_dlp_command += ["--cookies", cookie_file]

    try:
        result = subprocess.run(yt_dlp_command, check=True, capture_output=True, text=True)
        return result.stdout.strip()  # Return the direct stream URL
    except subprocess.CalledProcessError as e:
        print(f"Error extracting stream URL: {e}")
        sys.exit(1)


def download_recent_segment_ffmpeg(stream_url, output_directory, duration="100:00:00", max_retries=10):
    """
    Downloads the most recent segment of a YT live stream using ffmpeg and saves it to the specified directory.

    Args:
        stream_url (str): The extracted stream URL to download.
        output_directory (str): Directory where the live stream will be saved.
        duration (str): Duration of the segment to download in HH:MM:SS format (default: 10 minutes).
        max_retries (int): Maximum number of retries for network-related issues (default: 3).
    """
    # Convert duration from HH:MM:SS to seconds for ffmpeg
    h, m, s = map(int, duration.split(":"))
    total_seconds = h * 3600 + m * 60 + s

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Define the output file path
    output_file = os.path.join(output_directory, "recent_segment.mp4")

    # Base ffmpeg command to capture the live stream for the desired duration
    ffmpeg_command = [
        "ffmpeg", "-y", "-i", stream_url, "-t", str(total_seconds),
        "-c", "copy", output_file
    ]

    # Retry logic for downloading
    retry_count = 0
    while retry_count < max_retries:
        try:
            print(f"Attempt {retry_count + 1} to download the most recent segment of duration {duration}...")
            subprocess.run(ffmpeg_command, check=True)
            print(f"Download complete! Video saved to {output_file}")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error downloading live stream (Attempt {retry_count + 1}/{max_retries}): {e}")
            retry_count += 1
            if retry_count < max_retries:
                print("Retrying in 10 seconds...")
                time.sleep(10)  # Wait before retrying
            else:
                print("Max retries reached. Exiting.")
                sys.exit(1)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Download the most recent segment of a YouTube live stream using yt-dlp and ffmpeg.")
    parser.add_argument("url", help="URL of the YouTube live stream")
    parser.add_argument("--output-directory", default=os.path.expanduser("/Volumes/External"),
                        help="Directory to save the live stream (default: ~/Downloads)")
    parser.add_argument("--duration", type=str, default="00:10:00",
                        help="Duration of the segment to download in HH:MM:SS format (default: 10 minutes)")
    parser.add_argument("--cookie-file", type=str, help="Path to cookies.txt file for authentication")
    parser.add_argument("--max-retries", type=int, default=3, help="Maximum number of retries for download")

    # Parse arguments
    args = parser.parse_args()

    # Extract the direct stream URL using yt-dlp
    stream_url = extract_stream_url(args.url, args.cookie_file)

    # Download the most recent segment using ffmpeg
    download_recent_segment_ffmpeg(stream_url, args.output_directory, args.duration, args.max_retries)


if __name__ == "__main__":
    main()
