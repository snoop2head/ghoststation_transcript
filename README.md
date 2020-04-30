# ghoststation_transcript



## Project's purpose

This project's object is to archive Shin Hae-Chul(crom)'s radio program "Ghoststation" as transcript document.

* Transcripts are saved at transcribed_files folder as .txt file format
* [Apr 2001 ~ Dec 2002 radio program's transcripts are crawled from SBS radio station.](./_ghost_sbs_crawler.py)



## 프로젝트 목적
신해철의 라디오 프로그램, 고스트스테이션의 전문을 STT를 이용하여 제작해보려고 합니다.

- **[스크립트의 파일들은 transcribed_files에 .txt 파일로 저장했습니다](./transcribed_files)**
- 현재 ghoststation wikipedia를 제작 중이며, 향후 스크립트 파일들을 업로드할 예정입니다
- [2001년 4월~2002년 12월 방송분량은 SBS 방송국의 MP3 파일을 크롤링했습니다.](./_ghost_sbs_crawler.py) 



## 1. 다운로드 및 환경설정

- Google Cloud Speech는 MP3를 input으로 받지 않습니다. FLAC, WAV만을 input으로 받습니다. 
- 따라서 이 프로젝트에는 두 가지를 다운로드 받아야 합니다.
  - [FLAC / WAV 파일 -> 스크립트로 Transcribe하는 Google Cloud SDK](https://cloud.google.com/sdk/docs/)
  - [MP3 파일 -> FLAC / WAV로 변환시키는 FFMPEG](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS))
- Windows OS에서는 Virtual Environment를 형성해서 작업해야 하며, Mac OS에서는 로컬에서 작업할 수 있습니다. 
- env_settings.bat에서는 앞서 다운로드 받은 Google Cloud SDK와 FFMPEG의 system path를 설정해줍니다. 
  - Windows OS에서는 virtual environment를 설정해놓은 폴더 안에서만 작업하셔야 합니다. Google Cloud SDK도, FFMPEG도 Virtual Environment를 설정한 폴더에 다운로드 받으셔야 합니다. 마찬가지로, env_settings.bat을 해당 폴더에서 실행시켜야만 system path를 설정할 수 있습니다. 
  - Mac OS에서는 terminal에서 해당 command를 실행시키면 됩니다. 

## 2. Google Cloud SDK로 Transcribe

- _ghost_cloud_transcriber.py는 Google Cloud Storage에 위치한 40분 분량의 FLAC 파일을 한글 transcript로 출력합니다.
- _local_transcriber.py는 local 폴더에 위치한 4분 분량의 FLAC 파일을 한글 transcript로 출력합니다. 그러나 Google Cloud API 제한이 있기 때문에 5분 이상 분량의 오디오 파일은 _ghost_cloud_transcriber.py를 이용해야 합니다. 
- [Google Cloud SDK Setup 방법은 해당 튜토리얼을 참고하십시오.](https://www.youtube.com/watch?v=Ds-7D8d-FwA) 

## 3. pydub으로 mp3에서 FLAC 파일로 변환

- _ghost_transform.py는 mp3 파일을 flac 파일로 변환합니다. 

