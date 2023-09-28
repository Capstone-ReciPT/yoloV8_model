# Docs보고 yoloV8 따라해보기!

# import torch.multiprocessing
#
# from ultralytics import YOLO
#
# def run() :
#     torch.multiprocessing.freeze_support()
#     # Load a model
#     model = YOLO("yolov8n.yaml")  # build a new model from scratch
#     model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="coco128.yaml", epochs=3)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set
#     results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
#     path = model.export(format="onnx")  # export the model to ONNX format
#     print('loop')
#
# if __name__ == '__main__':
#     run()


# Docs보고 yoloV8 따라해보기! (학습 시키는 예시)
from ultralytics import YOLO

# model = YOLO('yolov8n.pt')
# model.predict(
#     source='https://media.roboflow.com/notebooks/examples/dog.jpeg',
#     conf=0.25,
#     save=True
# )



# Custom data 학습시키기 (Terminal창에 아래 command 쓰기)
# yolo task=detect mode=train model=yolov8s.pt data=C:\Users\JAEHYUN\Desktop\PythonWorkspace\CapStone\roboflow\yolov8\data.yaml epochs=100 imgsz=640

# yolo task=detect mode=train model=yolov8s.pt data=C:\Users\JAEHYUN\Desktop\PythonWorkspace\CapStone\roboflow\ingredientsDetection.v1i.yolov8\data.yaml epochs=20 batch=32 imgsz=640


# Custom data 학습 완료된 모델 (best.pt) : Valid 해보기!

# model = YOLO('C:/Users/JAEHYUN/Desktop/PythonWorkspace/CapStone/runs/detect/train100/weights/best.pt')
# print(type(model.names), len(model.names))
# print(model.names)
# resultsults = model.predict(source='C:/Users/JAEHYUN/Desktop/PythonWorkspace/CapStone/roboflow/yolov8/valid/images', save=True)


# 학습 시킨 모델 성능 평가
# yolo val model='C:/Users/JAEHYUN/Desktop/PythonWorkspace/CapStone/runs/detect/train100/weights/best.pt' data=C:\Users\JAEHYUN\Desktop\PythonWorkspace\CapStone\roboflow\yolov8\data.yaml batch=1 imgsz=640


