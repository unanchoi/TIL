## Scheduler

- Learning rate(학습율)을 epoch 또는 iteration에 따라 학습률을 조정 시키는 framework
- learning rate가 높은 경우 loss값을 빠르게 내릴수는 있지만, 최적의 학습을 하기 어렵다. 낮은 경우는 최적의 학습이 가능하지만 단계가 오래 걸린다.
- learning rate decay : 처음에는 학습율을 크게 설정한 후, 시간에 다라서 감소시키는 방법
- 일반적으로 처음에는 학습율을 크게 했다가, 최적값에 가까워질수록 학습율을 작게하는 것이 효과적이라고 한다.
- step decay : 각 epoch마다 일정한 비율로 학습을 감소시키는 방법

```python
from torch.optime.lr_scheduler import StepLR, MultiStepLR,CosineAnnealingLR

scheduler = MultiStepLR(optimizer, milestones , gamma, last_epoch)
scheduler =  StepLR(optimizer, step_size, gamma, last_epoch, verbose=False)

scheduler = CosineAnnealingLR(optimizer, T_max, eta_min=0, last_epoch=-1, verbose=False)
```
