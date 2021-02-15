import torch
import numpy as np
import pandas as pd
from PIL import Image
import glob, os, re
from torch.utils.data.dataset import Dataset
from torchvision import transforms

class ImageDataset(Dataset):
    def __init__(self, root='.', transform=None):
        super(ImageDataset, self).__init__()
        self.root = root
        self.transform = transform
        self.filenames = glob.glob(os.path.join(self.root,'*.jpg'))

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, index):
        img, target = read_data(self.filenames[index])
        if self.transform:
            img = self.transform(img)
        return img, target

def read_data(fn):
    img = Image.open(fn)
    splitUnderbar = lambda x : re.sub(r'^.+/','',x).replace('.jpg','').split('_')
    target = splitUnderbar(fn)[-1]
    return img, target

def write_result_table(preds, filename):
    pd.DataFrame({'filename':filename, 'pred':preds}).to_csv('result.csv', index=False)
    
def test_example():

    custom_transformer = transforms.Compose([
                transforms.ToTensor(),
                ])

    train_dataset = ImageDataset(root='/DATA/CANCER/TRAIN', transform=custom_transformer)
    test_dataset = ImageDataset(root='/DATA/CANCER/TEST', transform=custom_transformer)

    trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=1)
    testloader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=False)

    print(len(train_dataset)) # 4457
    print(len(testloader)) # 1117

    img, target = next(iter(trainloader))
    print(img.shape)
    # return: torch.Size([1, 3, 1080, 1920])
    print(target)
    # return: ('B',)

    img, target = next(iter(testloader))
    print(img.shape)
    # return: torch.Size([1, 3, 424, 616])
    print(target)
    # return: ('X',)

    # submission example
    remove_path = lambda x : re.sub(r'^.+/','',x)
    fn = [remove_path(i) for i in test_dataset.filenames]

    write_result_table(preds=np.random.rand(len(test_dataset)),
        filename=fn)

if __name__ == "__main__":
    test_example()