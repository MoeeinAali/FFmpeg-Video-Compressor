# Video Compression with FFmpeg

This script allows you to compress all video files in a directory using the FFmpeg tool.

## How to Use

1. Install prerequisites:
    - [Install `Python` on Windows](#Installing-FFmpeg-on-Windows)
    - Install `FFmpeg`

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




# Installing FFmpeg on Windows

1. **Download FFmpeg:**
   - Click on [this link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) to download the `FFmpeg-git-full.7z` file. You may need a VPN or a proxy if the website is blocked in your region.

2. **Extract the downloaded file:**
   - Unzip the downloaded file and rename the extracted folder to `FFmpeg`.

3. **Move the folder to C drive:**
   - Move the `FFmpeg` folder to the `C:\` drive.

4. **Run Command Prompt as an Administrator:**
   - Open the Command Prompt with administrative privileges.

5. **Set the PATH environment variable:**
   - Run the following command in the Command Prompt:
     ```bash
     setx /m PATH "C:\FFmpeg\bin;%PATH%"
     ```

6. **Restart your computer:**
   - Restart your computer to apply the changes.

After completing these steps, ffmpeg should be installed on your system. You can use it in the Command Prompt for various video processing tasks.
