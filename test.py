from moviepy.editor import VideoFileClip

def trim_video(input_path, output_path, duration=34):
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Trim the video to the first 10 seconds
    trimmed_clip = video_clip.subclip(0, duration)

    # Write the trimmed video to the output file
    trimmed_clip.write_videofile(output_path, codec="libx264")

    # Close the video clip
    video_clip.close()

# Example usage
input_path = "demo1.mp4"
output_path = "demo2.mp4"
trim_video(input_path, output_path)
