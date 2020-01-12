# from os import path
from pydub import AudioSegment

def transform(file_name_without_format):
    # files
    src = r"C:/Users/pc/Desktop/ghostation/z.past_files/" + file_name_without_format + ".mp3"
    dst = r"C:/Users/pc/Desktop/ghostation/" + file_name_without_format + ".flac"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="flac")
    print("done")


