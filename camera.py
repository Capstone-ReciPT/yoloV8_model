# 노트북 캠 or 맥북 + 아이폰 연동하여 카메라를 통해 학습 시킨 모델 직접 테스트 해보기!

from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO("best.pt")

result = model.predict(source="0", show=True, conf=0.5)

print(result)


# TerminaSl 창에 직접 입력
# yolo task=detect mode=predict model=best.pt source=pear.jpeg conf=0.5



