from moviepy.editor import *
import os
import shutil

# Define the directory containing the audio and image files
directory = "J:\Ytoub\OudeBookYt\ScrepitToMakeVaduio\ConvertMP3andImgeToMP4"

# Function to find the first file of a specific extension in the directory
def find_file_with_extension(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            return os.path.join(directory, filename)
    return None

# Find the audio and image files
audio_file = find_file_with_extension(directory, ".mp3")
image_file = find_file_with_extension(directory, ".png")

if not audio_file or not image_file:
    raise FileNotFoundError("Audio or image file not found in the directory.")

# Define the output video file path
output_video = os.path.join(directory, "output_video.mp4")

# Load the audio file
audio = AudioFileClip(audio_file)

# Load the image file and set its duration to match the audio length
image = ImageClip(image_file).set_duration(audio.duration).set_fps(1)

# Set the audio to the image
video = image.set_audio(audio)

# Export the final video with optimizations
video.write_videofile(
    output_video,
    fps=1,
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast",
    threads=16,           # Adjust based on your CPU cores
    bitrate="500k"        # Adjust bitrate for faster export
)

# Define new names for the files
new_image_file = " لا تحزن .png"
new_audio_file = " لا تحزن .mp3"
new_video_file = " لا تحزن .mp4"

# Define destination directories = r"J:\Ytoub\OudeBookYt\thim"
audio_destination = r"J:\Ytoub\OudeBookYt\MP3Book"
video_destination = r"J:\Ytoub\OudeBookYt\Mp4V"
image_destination = r"J:\Ytoub\OudeBookYt\BookCover"

# Rename and move the files after video creation
os.rename(audio_file, os.path.join(audio_destination, new_audio_file))
os.rename(image_file, os.path.join(image_destination, new_image_file))
os.rename(output_video, os.path.join(video_destination, new_video_file))

print("Files renamed and moved successfully!")
