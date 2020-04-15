# ghoststation_transcript

## 0. 프로젝트 목적
신해철의 라디오 프로그램, 고스트스테이션의 전문을 STT를 이용하여 제작해보려고 합니다.
This project's object is to document Shin Hae-Chul(crom)'s radio program, Ghoststation, as transcript.

- 현재 Google Cloud Speech to Text를 이용해서 스크립트를 콘솔에 출력하는 것까지 구현했습니다. 
- 향후 wikipedia 형태로 각 고스트스테이션 에피소드 별로 유저들이 자유롭게 열람 / 편집할 수 있도록 구현할 것입니다. [현재는 임시로 YNAW에 내용을 적어놓고 있습니다.](https://youneedawiki.com/app/page/1xlrjAihiMQSOPqYTowHzH5XDXNgEQkC4u_EoHc5ol0c)
- [신해철의 고스트스테이션 음성 파일은 SBS의 MP3 파일을 이용하고 있습니다.](https://programs.sbs.co.kr/radio/sghost/gorealrapod/56929) 



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

- [Google Cloud SDK Setup Step-by-step 국문 튜토리얼입니다.](https://www.youtube.com/watch?v=Ds-7D8d-FwA) 
- _ghostLongreader.py는 1분 이상의 FLAC 파일을 한글 transcript로 출력합니다.
- _ghostShortreader.py는 1분 미만의 FLAC 파일을 한글 transcript로 출력합니다.
- mic_to_script.py는 마이크로 입력된 한국 음성을 실시간으로 한글 transcript로 출력합니다



## 3. pydub으로 mp3에서 FLAC 파일로 변환

- _ghost_transform.py는 mp3 파일을 flac 파일로 변환합니다. 



## 💪 해결해야 할 점

- [ ] sbs의 ghoststation 게시판은 pagination을 javascript로 한다. 즉 url에다가 "?page=2" 같은 query를 추가해도 의미가 없다. 다른 페이지에 있는 mp3 파일들을 다운로드 받기 위해서 다른 방법을 찾아야 한다.
- [ ] _ghostLongreader.py는 용량제한이 있다. Google Cloud Bucket에 미리 mp3 파일을 올려놓고, STT 작업을 해야 한다. 