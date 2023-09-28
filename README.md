# 식재료 객체 인식 모델
<hr/>

## 개발 환경
- Python : python-3.9.13
- Pytorch : torch-2.2.0
- cuda : cuda_12.2
- 그래픽 카드 : 3070Ti
- 메모리 : 48GB
- Library : YoloV8
- 학습 데이터 셋 : Roboflow
- IDE : Pycharm
<hr/>

## 설명
1. yoloV8을 이용해 사물 인식 AI 모델 학습 (데이터 셋 : roboflow)
2. 학습 시킨 AI 모델을 validate & 직접 사용
3. AI 모델 `.pt` 을 플러터 내장을 위해 `.Tfile`로 변환
4. 변환 시킨 `.Tfile`을 플러터에 내장

## 사용법
1. [yoloV8](https://github.com/ultralytics/ultralytics) 사이트 접속 
2. `git clone <yoloV8 github>` 받기
3. 다운 받은 후 라이브러리 설치 : **pip install ultralytics**
4. **python + cuda + pytorch 버전 호환성 맞게 라이브러리 설치**
   - cuda : 그래픽 카드 버전에 맞는 cuda 설치
   - pytorch : cuda와 호환성이 맞는 버전 설치
5. 설치 완료 후 `yoloV8Test.py` 실행하여 테스트
6. `yoloV8.py` 통해 Custom Data을 통해 모델 생성
7. `camera.py` & `customDataValid.py` 통해 생성한 모델 Validate 
8. 플러터에 내장할 예정이라면 `transToOnnx.py` 참고
