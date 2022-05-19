# nn.Module
- Neural Network의 모든 것을 포괄하는 모든 신경망 모델의 BaseClass
- Condition : nn.Module을 상속한 subclass가 신경망 모델로 사용되기 위해서는 두 메소드를 오버라이딩 해야한다.

```python
1. __init__(self):
# 내가 사용하고 싶은, 내 신경망 모델에 사용될 구성품들을 정의 및 초기화하는 메소드

2. forward(self, x) # specify the connections : init에서 정의된 구성품들을 연결하는 메소드

```
