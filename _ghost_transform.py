# from os import path
from pydub import AudioSegment
import os
import glob


def transform(file_name_without_format, src, abs_dst):
    # files
    dst = abs_dst + file_name_without_format + ".flac"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="flac")
    print("done")


def move_transform(source, destination):

    mp3_file_list = glob.glob(source + "*.mp3")
    print(mp3_file_list)

    for item in mp3_file_list:
        print(item)
        item_name_list = item.split(".")[-2]
        item_name = item_name_list.split("/")[-1]
        transform(item_name, item, destination)


# change the source directory to your project directory
# source = "/Users/noopy/ghoststation_transcript/downloadedmp3/"
# destination = "/Users/noopy/ghoststation_transcript/transformed_flac/"


absolute_source = "/Users/noopy/ghoststation_transcript/test_mp3/"
absolute_destination = "/Users/noopy/ghoststation_transcript/test_flac/"

move_transform(absolute_source, absolute_destination)
