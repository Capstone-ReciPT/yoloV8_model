# 학습 시킨 모델 valid 해보기!

import ultralytics

from ultralytics import YOLO
model = YOLO('best.pt')

print(type(model.names), len(model.names))
print(model.names)

results = model.predict(source='../roboflow/2/valid/images/*.jpg', save=True)

import numpy as np

for result in results:

    uniq, cnt = np.unique(result.boxes.cls.cpu().numpy(), return_counts=True)
    uniq_cnt_dict = dict(zip(uniq, cnt))

    print('\n{class num: counts} = ', uniq_cnt_dict, '\n')

    for c in result.boxes.cls:
        print('class num =', int(c), ', class_name = ', model.names[int(c)])