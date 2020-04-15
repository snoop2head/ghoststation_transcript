# from os import path
from pydub import AudioSegment
import os
import glob


def transform(file_name_without_format, src):
    # files
    # src = r"C:/Users/pc/Desktop/ghostation/z.past_files/" + file_name_without_format + ".mp3"
    dst = (
        "/Users/noopy/ghoststation_transcript/transformed_flac/"
        + file_name_without_format
        + ".flac"
    )

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="flac")
    print("done")


def move_transform():
    # change the source directory to your project directory
    # source = '/path/to/source_folder'
    source = "/Users/noopy/ghoststation_transcript/downloadedmp3/"

    mp3_file_list = glob.glob(source + "*.mp3")
    print(mp3_file_list)

    for item in mp3_file_list:
        print(item)
        item_name_list = item.split(".")[-2]
        item_name = item_name_list.split("/")[-1]
        transform(item_name, item)


move_transform()
