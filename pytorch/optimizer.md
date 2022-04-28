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
