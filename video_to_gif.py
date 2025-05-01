import argparse
from moviepy.editor import VideoFileClip

def convert_video_to_gif(input_path, output_path, fps=10, scale=None, start_time=None, end_time=None):
    """
    Convert a video file to GIF.
    
    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the output GIF file.
        fps (int): Frames per second for the output GIF.
        scale (float or tuple): Scaling factor for the output. If None, original size is kept.
        start_time (float): Start time in seconds to begin conversion from.
        end_time (float): End time in seconds to stop conversion at.
    """
    try:
        # Load the video file
        clip = VideoFileClip(input_path)
        
        # Trim the video if start_time or end_time is specified
        if start_time is not None or end_time is not None:
            start = start_time if start_time is not None else 0
            end = end_time if end_time is not None else clip.duration
            clip = clip.subclip(start, end)
        
        # Resize if scale is specified
        if scale is not None:
            if isinstance(scale, (float, int)):
                clip = clip.resize(scale)
            elif isinstance(scale, tuple) and len(scale) == 2:
                clip = clip.resize(scale)
        
        # Write to GIF file
        clip.write_gif(output_path, fps=fps)
        
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
    finally:
        if 'clip' in locals():
            clip.close()

def main():
    parser = argparse.ArgumentParser(description='Convert video to GIF')
    parser.add_argument('input', help='Input video file path')
    parser.add_argument('output', help='Output GIF file path')
    parser.add_argument('--fps', type=int, default=10, help='Frames per second for the GIF (default: 10)')
    parser.add_argument('--scale', type=float, help='Scaling factor (e.g., 0.5 for half size)')
    parser.add_argument('--start', type=float, help='Start time in seconds')
    parser.add_argument('--end', type=float, help='End time in seconds')
    
    args = parser.parse_args()
    
    convert_video_to_gif(
        args.input,
        args.output,
        fps=args.fps,
        scale=args.scale,
        start_time=args.start,
        end_time=args.end
    )

if __name__ == "__main__":
    main()
