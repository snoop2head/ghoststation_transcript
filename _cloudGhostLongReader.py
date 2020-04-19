from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = r"/Users/noopy/ghoststation_transcript/snoop2head.json"

# https://github.com/googleapis/python-speech/blob/master/samples/v1/speech_transcribe_async.py
def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # The language of the supplied audio
    language_code = "ko-KR"

    audio_channel_count = 2
    enable_separate_recognition_per_channel = True

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
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
        # First alternative is the most probable result
        # print(result)
        alternative = result.alternatives[0]
        # print(u"Transcript: {}".format(alternative.transcript))
        # print(alternative.confidence)
        with open(f"{output_file_name}", "w", encoding="utf-8") as file:
            file.write(alternative.transcript)

    


# uri designation needed
# uri = "gs://ghoststation/2000010307-20180831-456.flac"
uri = "gs://ghoststation/test.flac"
sample_long_running_recognize(uri)
