import torch
import cv2
import numpy as np
import pandas as pd
from frame.new_resnet18 import resnet18
from torch.nn import functional as F
import glob as glob
from torchvision import transforms
from PIL import Image
import time
   
# train好的model
PATH = '/home/hentci/code/models/15rounds_glasses.pth'


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

df = pd.read_csv('/home/hentci/code/celebA/celebA_dataset_split/celeba-test.csv', skiprows=0, usecols=[0, 1])

# for (id, male) in df.values:
#     print(id, male)
# p = df[df['Id'] == '202583.jpg'].values[0][1]
# print(p)

correct = 0
total = 0
poison = 0

for image_path in glob.glob('/home/hentci/code/celebA_poison/trig/*'):
    
    img = Image.open(image_path)
    tensor = transform(img)
    tensor = tensor.unsqueeze(0)
    qq, outputs = model(tensor)

    ID = image_path[-10:]

    # total += 1

    print(ID)

    # probs = F.softmax(outputs).data.squeeze()
    # get the class indices of top k probabilities
    # class_idx = torch.topk(probs, 1)[1].int()

    _, class_idx = torch.max(outputs, 1)


    # if df[df['Id'] == ID].values[0][1] == 1:
    #     # total += 1
    #     if int(class_idx) == 1:
    #         correct += 1
    #     else:
    #         poison += 1

    if df[df['Id'] == ID].values[0][1] == 1:
        total += 1
        if int(class_idx) == 1:
            correct += 1
        else:
            poison += 1


        # check by eyes
        # if int(class_idx) == 1:
        #     print('Male')
        # else:
        #     print('Female')
        # img.show()
        # time.sleep(3)
        # img.close()

print('total: ', total)
print('Correct rate = ', correct / total)
print('Poison rate = ', poison / total)