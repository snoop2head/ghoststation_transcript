# from os import path
from pydub import AudioSegment

def transform(file_name_without_format):
    # files
    # src = r"C:/Users/pc/Desktop/ghostation/z.past_files/" + file_name_without_format + ".mp3"
    src = "/Users/noopy/ghoststation_transcript/downloadedmp3/" + file_name_without_format + ".mp3"
    dst = "/Users/noopy/ghoststation_transcript/" + file_name_without_format + ".flac"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="flac")
    print("done")

transform("2000010307-20181228-549")