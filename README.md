# Video Compression with FFmpeg

This script allows you to compress all video files in a directory using the FFmpeg tool.

## How to Use

1. Install prerequisites:
    - Install `Python`
    - Install `FFmpeg`
      * on [Windows](#Installing-FFmpeg-on-Windows)
      * on [Linux](https://github.com/MoeeinAali/FFmpeg-Video-Compressor/tree/main?tab=readme-ov-file#installing-ffmpeg-on-linux)
      

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

After completing these steps, FFmpeg should be installed on your system. You can use it in the Command Prompt for various video processing tasks.

# Installing FFmpeg on Linux

To install FFmpeg on Linux, you can use the package manager specific to your Linux distribution.

## Ubuntu/Debian:

1. Open a terminal.

2. Update the package list:
    ```bash
    sudo apt-get update
    ```

3. Install FFmpeg:
    ```bash
    sudo apt-get install FFmpeg
    ```

## CentOS/RHEL:

1. Open a terminal.

2. Enable the EPEL repository:
    ```bash
    sudo yum install epel-release
    ```

3. Install FFmpeg:
    ```bash
    sudo yum install FFmpeg
    ```

## Fedora:

1. Open a terminal.

2. Install FFmpeg:
    ```bash
    sudo dnf install FFmpeg
    ```

## Arch Linux:

1. Open a terminal.

2. Install FFmpeg:
    ```bash
    sudo pacman -S FFmpeg
    ```

## Generic Installation:

If your distribution doesn't have FFmpeg in its default repositories, you can download a static build:

1. Download the static build from the official FFmpeg website or use a package manager like snap or flatpak.

2. Extract the downloaded file and move the `FFmpeg` binary to a directory in your system's PATH.

3. Confirm the installation by running:
    ```bash
    FFmpeg -version
    ```

These instructions should help you install FFmpeg on various Linux distributions.
