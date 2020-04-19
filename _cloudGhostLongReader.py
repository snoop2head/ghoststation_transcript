# Transcribing long audio files: https://cloud.google.com/speech-to-text/docs/async-recognize#speech_transcribe_async-python
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os

# Authentification
# documentation: https://googleapis.dev/python/google-api-core/latest/auth.html
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = r"/Users/noopy/ghoststation_transcript/snoop2head.json"

# sample function: https://github.com/googleapis/python-speech/blob/master/samples/v1/speech_transcribe_async.py
# documentation: https://googleapis.dev/python/speech/latest/index.html
def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "ko-KR"

    # ghoststation radio is consisted of two channels
    audio_channel_count = 2
    enable_separate_recognition_per_channel = True

    # Sample rate in Hertz of the audio data sent
    # sample rate hertz and encoding docs: https://cloud.google.com/speech-to-text/docs/encoding
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    sample_rate_hertz = 44100
    
    # json file to send to google speech recognition api
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "audio_channel_count": audio_channel_count,
        "enable_separate_recognition_per_channel": enable_separate_recognition_per_channel,
        "language_code": language_code,
        "encoding": encoding,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    url_root = uri.split(".")[0]
    flac_name = url_root.split("/")[-1]
    output_file_name = "./transcribed_files/" + flac_name + ".txt"

    for result in response.results:
        # print(result)
        # First alternative is the most probable result
        alternative = result.alternatives[0]

        # print transcript and confidence
        # print(u"Transcript: {}".format(alternative.transcript))
        # print(alternative.confidence)

        # write transcript on text file
        with open(f"{output_file_name}", "a", encoding="utf-8") as file:
            file.write(alternative.transcript + "\n")

    
# uri designation needed
# uri = "gs://ghoststation/2000010307-20180831-456.flac"
uri = "gs://ghoststation/test.flac"
# uri = "gs://ghoststation/2000010307-20181228-543.flac"
sample_long_running_recognize(uri)
