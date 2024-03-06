import speech_recognition as sr
import pyttsx3

# 오디오 캡처를 위한 recognizer와 마이크 객체 생성
r = sr.Recognizer()
mic = sr.Microphone()

# TTS 엔진 초기화
engine = pyttsx3.init()

# 마이크에서 오디오 캡처 시작
with mic as source:
    print("말하세요...")
    audio = r.listen(source)

# 구글 웹 음성 API를 사용하여 오디오를 텍스트로 변환
try:
    print("음성 인식 중...")
    text = r.recognize_google(audio, language='ko-KR')
    print("인식된 텍스트:")
    print(text)

    # 인식된 텍스트를 음성으로 출력
    engine.say(text)
    engine.runAndWait()
except sr.UnknownValueError:
    print("음성 인식에 실패했습니다.")
except sr.RequestError as e:
    print("음성 인식 서비스에 요청할 수 없습니다; {0}".format(e))

