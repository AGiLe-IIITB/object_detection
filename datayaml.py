import yaml
config = {'path':'/home/arismita/ML/yolov5_training/building_detection',
         'train':'/home/arismita/ML/yolov5_training/building_detection/train',
         'val':'/home/arismita/ML/yolov5_training/building_detection/valid',
         'nc':1,
         'names':['Building']}

with open('data.yaml', 'w') as file:
  yaml.dump(config, file, default_flow_style=False)
