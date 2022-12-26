import torch
import cv2
import numpy as np
from frame.new_resnet18 import resnet18
from torch.nn import functional as F
import glob as glob
from torchvision import transforms
from PIL import Image
import time
   
# train好的model
PATH = '/home/hentci/code/models/celebA_test.pth'

# 這個好像沒差，應該是不用先save = =
# torch.save(CNN_Model().state_dict(), PATH)

model = resnet18(num_classes=2)
model.eval()
model.load_state_dict(torch.load(PATH))
# print([model])

stats = ((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
transform = transforms.Compose(
    [
     transforms.Resize((128, 128)),
     transforms.ToTensor(),
     transforms.Normalize(*stats,inplace=True)
    ]
)


for image_path in glob.glob('/home/hentci/code/data/celebA_test_img/*'):
    
    img = Image.open(image_path)
    tensor = transform(img)
    tensor = tensor.unsqueeze(0)
    qq, outputs = model(tensor)

    # probs = F.softmax(outputs).data.squeeze()
    # get the class indices of top k probabilities
    # class_idx = torch.topk(probs, 1)[1].int()

    _, class_idx = torch.max(outputs, 1)

    if int(class_idx) == 1:
        print('Male')
    else:
        print('Female')
    # img.show()
    # time.sleep(5)
    # img.close()

    