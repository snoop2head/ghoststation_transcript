# -*- coding:utf-8 -*-
import io
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = r"/Users/noopy/ghoststation_transcript/credentials.json"


def run_quickstart():
    # [START speech_quickstart]
    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    # [END migration_import]

    # Instantiates a client
    # [START migration_client]
    client = speech.SpeechClient()
    # [END migration_client]

    # The name of the audio file to transcribe
    file_name = os.path.join(os.path.dirname(__file__), ".", "demo_short.flac")

    audio_channel_count = 2
    enable_separate_recognition_per_channel = True
    language_code = "ko-KR"
    config = {
        "audio_channel_count": audio_channel_count,
        "enable_separate_recognition_per_channel": enable_separate_recognition_per_channel,
        "language_code": language_code,
    }

    # Loads the audio into memory
    with io.open(file_name, "rb") as f:
        content = f.read()
    audio = {"content": content}

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print(u"Channel tag: {}".format(result.channel_tag))
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
    # [END speech_quickstart]


if __name__ == "__main__":
    run_quickstart()

# audioconvert [--verbose/-v] convert "C:\Users\pc\Desktop\ghostation\z.past_files\aud_trim.mp3" "C:\Users\pc\Desktop\ghostation" [--output-format/-o flac]

"""

def run_quickstart():
    
    # [START speech_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # [END migration_import]

    # Instantiates a client
    # [START migration_client]
    client = speech.SpeechClient()
    # [END migration_client]

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        '.',
        'demo_short.flac')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding='FLAC',
        sample_rate_hertz=44100,
        audioChannelCount = 2,
        language_code='ko-KR')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    # [END speech_quickstart]


if __name__ == '__main__':
    run_quickstart()
"""
