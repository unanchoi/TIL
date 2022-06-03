# Generator
- `iterator` 를 생성해주는 함수
- iterator는 클래스 내에 `__iter__` , `__next__` , `__getitem__` 을 구현해야 한다.
- `yield` 를 이용하면, 클래스 내의 메소드 구현 없이 함수를 제너레이터로 만들 수 있다.
- **yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보한다.** 따라서 yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행되도록 만듬.

```python
ALPHABET = ["A", "B", "C"]

def alphabet(string_list : list):
    for l in string_list:
        yield l

for l in alphabet(ALPHABET):
    print(l)

f = alphabet(ALPHABET)
print(f) # <generator object alphabet at 0x0000020047163840>
```

- `dir(generator)`

['**class**', '**del**', '**delattr**', '**dir**', '**doc**', '**eq**', '**format**', '**ge**', '**getattribute**', '**gt**', '**hash**', '**init**', '**init_subclass**', '**iter**', '**le**', '**lt**', '**name**', '**ne**', '**new**', '**next**', '**qualname**', '**reduce**', '**reduce_ex**', '**repr**', '**setattr**', '**sizeof**', '**str**', '**subclasshook**', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']

## Reference

- [https://dojang.io/mod/page/view.php?id=2412](https://dojang.io/mod/page/view.php?id=2412)
