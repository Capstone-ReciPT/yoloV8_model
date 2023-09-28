# Flutter 내장을 위해 .pt -> .onnx -> .Tfile 변환해야함!


# 1. `best.pt` -> `.onnx`
from ultralytics import YOLO

model = YOLO(model='best.pt')
model.export(format="onnx")


# 2. `.onnx` -> `.Tfile`
# https://launchx.netspresso.ai/main -> 회원가입
# onnx -> Tfile 변환시키기!