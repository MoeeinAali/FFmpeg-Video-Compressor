import os
import sys

directory = sys.argv[2]


def get_files(directory):
    if not os.path.isdir(directory):
        return "The specified directory doesn't exist."
    files_list = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            files_list.append(file_name)
    return files_list


files = get_files(directory)

for file in files:
    input_file = os.path.join(directory, file)
    output_file = os.path.join(directory,
                               os.path.splitext(file)[0] + "_compressed.mp4")

    command = (
        'ffmpeg -i "{input}" -r "{resolution}" -vf "scale=-2:720" -c:v libx265 -crf 28 -c:a libopus -b:a 32K -strict experimental -max_muxing_queue_size 1024 "{output}"'
    ).format(resolution=int(sys.argv[1]), input=input_file, output=output_file)

    os.system(command)
