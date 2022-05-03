- python은 변수 혹은 parameter 선언시에, 따로 타입지정을 하지 않는다.
- `typing`이라는 library와 python의 타입 명시 기능을 통해, 명시적으로 타입을 지정할 수 있다.
- 실제 compile 과정에서 에러가 발생하지는 않는다.

```python
def hello(a:int,b:int) -> int:
    return a+b
  
number_list :list[int] = [1, 2, 3, 4, 5]
number_list_2 :list[int, str] = [1, "이"]
```

- 새로 type을 명시적으로 사용할 수도 있다.

```python
from typing import NewType

user = NewType("human", str)

someone = user("player1")
print(type(someone)) # str
```
