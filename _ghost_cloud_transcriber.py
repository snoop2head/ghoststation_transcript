# Transcribing long audio files on cloud storage: https://cloud.google.com/speech-to-text/docs/async-recognize#speech_transcribe_async-python
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os

# Authentification
# documentation: https://googleapis.dev/python/google-api-core/latest/auth.html
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = r"/Users/noopy/ghoststation_transcript/snoop2head.json"

# long running audio STT function for FLAC files in google cloud storage
# documentation: https://googleapis.dev/python/speech/latest/index.html
def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    https://github.com/googleapis/python-speech/blob/master/samples/v1/speech_transcribe_async.py

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "ko-KR"

    # ghoststation radio is consisted of two channels
    # Transcribing audio with multiple channels: https://cloud.google.com/speech-to-text/docs/multi-channel
    audio_channel_count = 2
    
    # separating recognition enables multiple speakers recognition
    enable_separate_recognition_per_channel = False

    # Sample rate in Hertz of the audio data sent
    # sample rate hertz and encoding docs: https://cloud.google.com/speech-to-text/docs/encoding
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    sample_rate_hertz = 44100
    
    # json file to send to google speech recognition api
    # arguments list: https://cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "audio_channel_count": audio_channel_count,
        "enable_separate_recognition_per_channel": enable_separate_recognition_per_channel,
        "language_code": language_code,
        "encoding": encoding,
        "enable_word_time_offsets": True
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    url_root = uri.split(".")[0]
    flac_name = url_root.split("/")[-1]
    output_file_name = "./transcribed_files/" + flac_name + ".txt"
    
    # parsing speech to text response
    # API RESPONSE EXAMPLE: https://cloud.google.com/speech-to-text/docs/basics#time-offsets
    # print(response.results)
    for result in response.results:
        # First option is the most probable result
        alternative = result.alternatives[0]

        # print transcript
        # print(u"Transcript: {}".format(alternative.transcript))

        # print confidence
        # print(alternative.confidence)

        # print timestamp for the first word of the transcript
        transcript_timestamp = str(alternative.words[0].start_time.seconds)

        # write transcript on text file
        with open(f"{output_file_name}", "a", encoding="utf-8") as file:
            # write the timestamp
            file.write(transcript_timestamp + ": ")
            
            # write the script
            file.write(alternative.transcript + "\n")

# uri designation for the audio files in Google Cloud Storage
# uri = "gs://ghoststation/행복은 재능이다 060114 신해철의 고스트네이션 고스트스테이션.flac"
file_name_without_type = "2000010307-20181012-480"
uri = "gs://ghoststation/" + file_name_without_type + ".flac"

sample_long_running_recognize(uri)
