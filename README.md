# Video Compression with FFmpeg

This script allows you to compress all video files in a directory using the FFmpeg tool.

## How to Use

1. Install prerequisites:
    - Install Python
    - Install ffmpeg

2. Download the script:
    ```bash
    git clone https://github.com/MoeeinAali/FFmpeg-Video-Compressor.git
    cd FFmpeg-Video-Compressor.git
    ```

3. Run the script:
    ```bash
    python Video-Compressor.py <Frame Rate> <directory_path>
    ```

    - `<Frame Rate>`: Desired Frame Rate for the videos (from 10 to 30)
    - `<directory_path>`: Path to the directory containing videos

    Example:
    ```bash
    python compress_videos.py 20 /path/to/videos
    ```

4. Output:
    - Compressed videos with the `_compressed.mp4` extension will be saved in the same directory.

## Notes
- Make sure FFmpeg is installed.
- Make sure Python is installed.

## Known Issues
- If you encounter an error, ensure that the directory path and input resolution are correct.
- If needed, you can modify the ffmpeg parameters in the Python code.

**Note:** This script is suitable for video files only and requires ffmpeg installation.

For more information about using ffmpeg, visit the [official ffmpeg website](https://ffmpeg.org/).
