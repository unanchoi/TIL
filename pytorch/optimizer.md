## Optimizer

#### Opimization이란?
- Train dataset을 이용하여 모델을 학습 할 때, 실제 결과와 예측값의 차이를 줄여나가는 과정이다. 즉, Loss Function(손실 함수)의 최솟값(Global minimum, Local Minimum)을 찾는 일련의 과정
- optimzer : optimization algorithm

##### optimizer 사용법
```python
def train(num_epochs, model, data_loader, criterion, optimizer, saved_dir, val_every, device):
    print('Start training..')
    best_loss = 9999999
    for epoch in range(num_epochs):
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)

            outputs = model(imgs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```
##### optimizer.zero_grad()를 하는 이유?
- pytorch는 gradient값들이 누적 되기 때문에 `zero_grad`()를 해주지 않으면, 역전파 과정에서 이전 Loop에서 저장된 gradient를 계속 더해준다.

##### pytorch optimizer 종류
```python
optimizer = torch.optim.Adadelta(model.parameters(), lr=learning_rate)
optimizer = torch.optim.Adagrad(model.parameters(), lr=learning_rate, )
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
optimizer = torch.optim.AdamW(model.parameters(), lr = learning_rate)
optimizer = torch.optim.SparseAd(model.parameters(), lr = learning_rate)
optimizer = torch.optim.Adamax(model.parameters(), lr = learning_rate)
optimizer = torch.optim.ASGD(model.parameters(), lr = learning_rate)
optimizer = torch.optim.LBFGS(model.parameters(), lr = learning_rate)
optimizer = torch.optim.NAdam(model.parameters(), lr = learning_rate)
optimizer = torch.optim.RAdam(model.parameters(), lr = learning_rate)
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
optimizer = torch.optim.Rprop(model.parameters())
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate,momentum=0.9)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate, nesterov=True, dampening=0, momentum=0.9)
```

## Optimizer Sample Code
##### naver boostcourse에 있는 CNN mini project code에서 진행

```
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
print('pytorch version: {}'.format(torch.__version__))
print('GPU 사용 가능 여부: {}'.format(torch.cuda.is_available()))

device = "cuda" if torch.cuda.is_available() else "cpu"
data_dir = './data/my_cat_dog'
batch_size = 100
num_epochs = 10
learning_rate = 0.0001
weight_decay = 0.0005



class CatDogDataset(Dataset):
    def __init__(self, data_dir : str, mode : str, transform=None) -> None:
        self.all_data = sorted(glob.glob(f'{data_dir}/{mode}/*/*.jpg',  recursive=True))
        print(self.all_data)
        self.transform = transform
    def __getitem__(self, index):
        data_path = self.all_data[index]
        img = Image.open(data_path)
        if self.transform != None:
            img = self.transform(img)
        if os.path.basename(data_path).startswith("cat"):
            label = 0
        else:
            label = 1
        return img, label
    def __len__(self):
        length = len(self.all_data)
        return length
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomRotation(5),
        transforms.RandomHorizontalFlip(),
        transforms.RandomResizedCrop(120, scale=(0.96, 1.0), ratio=(0.95, 1.05)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize([120, 120]),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}
train_data = CatDogDataset(data_dir=data_dir, mode='train', transform=data_transforms['train'])
val_data = CatDogDataset(data_dir=data_dir, mode='val', transform=data_transforms['val'])
test_data = CatDogDataset(data_dir=data_dir, mode='test', transform=data_transforms['val'])

train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True, drop_last=True)
val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False, drop_last=True)
test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False, drop_last=True)

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # self.conv 구현
        self.conv = nn.Sequential(
            nn.Conv2d(3, 32, (3, 3)),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, (3, 3)),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, (3, 3)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 128, (3, 3)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc1 = nn.Linear(5 * 5 * 128, 512, bias=True)
        self.fc2 = nn.Linear(512, 2)
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
def train(num_epochs, model, data_loader, criterion, optimizer, saved_dir, val_every, device):
    print('Start training..')
    best_loss = 9999999
    for epoch in range(num_epochs):
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            _, argmax = torch.max(outputs, 1)
            accuracy = (labels == argmax).float().mean()
            if (i+1) % 3 == 0:
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'.format(
                    epoch+1, num_epochs, i+1, len(data_loader), loss.item(), accuracy.item() * 100))
        if (epoch + 1) % val_every == 0:
            avrg_loss = validation(epoch + 1, model, val_loader, criterion, device)
            if avrg_loss < best_loss:
                print('Best performance at epoch: {}'.format(epoch + 1))
                print('Save model in', saved_dir)
                best_loss = avrg_loss
                save_model(model, saved_dir)
def validation(epoch, model, data_loader, criterion, device):
    print('Start validation #{}'.format(epoch) )
    model.eval()
    with torch.no_grad():
        total = 0
        correct = 0
        total_loss = 0
        cnt = 0
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            total += imgs.size(0)
            _, argmax = torch.max(outputs, 1)
            correct += (labels == argmax).sum().item()
            total_loss += loss
            cnt += 1
        avrg_loss = total_loss / cnt
        print('Validation #{}  Accuracy: {:.2f}%  Average Loss: {:.4f}'.format(epoch, correct / total * 100, avrg_loss))
    model.train()
    return avrg_loss
def test(model, data_loader, device):
    print('Start test..')
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            _, argmax = torch.max(outputs, 1)
            total += imgs.size(0)
            correct += (labels == argmax).sum().item()
        print('Test accuracy for {} images: {:.2f}%'.format(total, correct / total * 100))
    model.train()
def save_model(model, saved_dir, file_name='best_model.pt'):
    os.makedirs(saved_dir, exist_ok=True)
    check_point = {
        'net': model.state_dict()
    }
    output_path = os.path.join(saved_dir, file_name)
    torch.save(check_point, output_path)
torch.manual_seed(7777)
model = SimpleCNN()
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adadelta(model.parameters(), lr=learning_rate)
optimizer = torch.optim.Adagrad(model.parameters(), lr=learning_rate, )
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
optimizer = torch.optim.NAdam(model.parameters(), lr=learning_rate)
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate,momentum=0.9)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate, nesterov=True, dampening=0, momentum=0.9)
#
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
print('pytorch version: {}'.format(torch.__version__))
print('GPU 사용 가능 여부: {}'.format(torch.cuda.is_available()))
device = "cuda" if torch.cuda.is_available() else "cpu"
data_dir = './data/my_cat_dog'
batch_size = 100
num_epochs = 10
learning_rate = 0.0001
weight_decay = 0.0005
class CatDogDataset(Dataset):
    def __init__(self, data_dir : str, mode : str, transform=None) -> None:
        self.all_data = sorted(glob.glob(f'{data_dir}/{mode}/*/*.jpg',  recursive=True))
        print(self.all_data)
        self.transform = transform
    def __getitem__(self, index):
        data_path = self.all_data[index]
        img = Image.open(data_path)
        if self.transform != None:
            img = self.transform(img)
        if os.path.basename(data_path).startswith("cat"):
            label = 0
        else:
            label = 1
        return img, label
    def __len__(self):
        length = len(self.all_data)
        return length
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomRotation(5),
        transforms.RandomHorizontalFlip(),
        transforms.RandomResizedCrop(120, scale=(0.96, 1.0), ratio=(0.95, 1.05)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize([120, 120]),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}
train_data = CatDogDataset(data_dir=data_dir, mode='train', transform=data_transforms['train'])
val_data = CatDogDataset(data_dir=data_dir, mode='val', transform=data_transforms['val'])
test_data = CatDogDataset(data_dir=data_dir, mode='test', transform=data_transforms['val'])
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True, drop_last=True)
val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False, drop_last=True)
test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False, drop_last=True)
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # self.conv 구현
        self.conv = nn.Sequential(
            nn.Conv2d(3, 32, (3, 3)),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, (3, 3)),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, (3, 3)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 128, (3, 3)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc1 = nn.Linear(5 * 5 * 128, 512, bias=True)
        self.fc2 = nn.Linear(512, 2)
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
def train(num_epochs, model, data_loader, criterion, optimizer, saved_dir, val_every, device):
    print('Start training..')
    best_loss = 9999999
    for epoch in range(num_epochs):
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            _, argmax = torch.max(outputs, 1)
            accuracy = (labels == argmax).float().mean()
            if (i+1) % 3 == 0:
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'.format(
                    epoch+1, num_epochs, i+1, len(data_loader), loss.item(), accuracy.item() * 100))
        if (epoch + 1) % val_every == 0:
            avrg_loss = validation(epoch + 1, model, val_loader, criterion, device)
            if avrg_loss < best_loss:
                print('Best performance at epoch: {}'.format(epoch + 1))
                print('Save model in', saved_dir)
                best_loss = avrg_loss
                save_model(model, saved_dir)
def validation(epoch, model, data_loader, criterion, device):
    print('Start validation #{}'.format(epoch) )
    model.eval()
    with torch.no_grad():
        total = 0
        correct = 0
        total_loss = 0
        cnt = 0
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            total += imgs.size(0)
            _, argmax = torch.max(outputs, 1)
            correct += (labels == argmax).sum().item()
            total_loss += loss
            cnt += 1
        avrg_loss = total_loss / cnt
        print('Validation #{}  Accuracy: {:.2f}%  Average Loss: {:.4f}'.format(epoch, correct / total * 100, avrg_loss))
    model.train()
    return avrg_loss
def test(model, data_loader, device):
    print('Start test..')
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for i, (imgs, labels) in enumerate(data_loader):
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            _, argmax = torch.max(outputs, 1)
            total += imgs.size(0)
            correct += (labels == argmax).sum().item()
        print('Test accuracy for {} images: {:.2f}%'.format(total, correct / total * 100))
    model.train()
def save_model(model, saved_dir, file_name='best_model.pt'):
    os.makedirs(saved_dir, exist_ok=True)
    check_point = {
        'net': model.state_dict()
    }
    output_path = os.path.join(saved_dir, file_name)
    torch.save(check_point, output_path)
torch.manual_seed(7777)
model = SimpleCNN()
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adadelta(model.parameters(), lr=learning_rate)
optimizer = torch.optim.Adagrad(model.parameters(), lr=learning_rate, )
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
optimizer = torch.optim.AdamW(model.parameters(), lr = learning_rate)
optimizer = torch.optim.SparseAd(model.parameters(), lr = learning_rate)
optimizer = torch.optim.Adamax(model.parameters(), lr = learning_rate)
optimizer = torch.optim.ASGD(model.parameters(), lr = learning_rate)
optimizer = torch.optim.LBFGS(model.parameters(), lr = learning_rate)
optimizer = torch.optim.NAdam(model.parameters(), lr = learning_rate)
optimizer = torch.optim.RAdam(model.parameters(), lr = learning_rate)
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
optimizer = torch.optim.Rprop(model.parameters())
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate,momentum=0.9)
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate, nesterov=True, dampening=0, momentum=0.9)
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
model = model.to(device)
val_every = 1
saved_dir = './saved/SimpleCNN'
train(num_epochs, model, train_loader, criterion, optimizer, saved_dir, val_every, device)
model_path = './saved/SimpleCNN/best_model.pt'
model = SimpleCNN().to(device)
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
state_dict = checkpoint['net']
model.load_state_dict(state_dict)
test(model, test_loader, device)
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
model = model.to(device)
val_every = 1
saved_dir = './saved/SimpleCNN'
train(num_epochs, model, train_loader, criterion, optimizer, saved_dir, val_every, device)
model_path = './saved/SimpleCNN/best_model.pt'
model = SimpleCNN().to(device)
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
state_dict = checkpoint['net']
model.load_state_dict(state_dict)
test(model, test_loader, device)

```
### 
- SGD

Validation #10  Accuracy: 50.30%  Average Loss: 0.7139
optimizer : Stochastic Gradient Descent
Start test..
Test accuracy for 2000 images: 53.95%

- Momentum

Validation #10  Accuracy: 62.30%  Average Loss: 0.6436
Best performance at epoch: 10
Save model in ./saved/SimpleCNN
optimizer : Stochastic Gradient Descent With Momentum
Start test..
Test accuracy for 2000 images: 63.20%

- NAG

Validation #10  Accuracy: 62.00%  Average Loss: 0.6446
Best performance at epoch: 10
Save model in ./saved/SimpleCNN
Start test..
Test accuracy for 2000 images: 63.10%

- AdaGrad

Validation #10  Accuracy: 66.90%  Average Loss: 0.5963
Start test..
Test accuracy for 2000 images: 69.80%

- Adadelta

Validation #10  Accuracy: 49.70%  Average Loss: 0.7168
Start test..
Test accuracy for 2000 images: 53.05%

- RMSProp

Validation #10  Accuracy: 76.50%  Average Loss: 0.4874
Best performance at epoch: 10
Save model in ./saved/SimpleCNN
Start test..
Test accuracy for 2000 images: 74.05%

- Adam

Validation #10  Accuracy: 73.70%  Average Loss: 0.5373
Start test..
Test accuracy for 2000 images: 73.95%

- Nadam

Validation #10  Accuracy: 75.70%  Average Loss: 0.4879
Best performance at epoch: 10
Save model in ./saved/SimpleCNN
Start test..
Test accuracy for 2000 images: 74.25%
