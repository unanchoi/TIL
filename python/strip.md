### strip

- strip()은 공백만 지워주는 method로 알고 있었는데, 공백이 아닌 문자열도 지울 수 있는 method 였다.
- 양쪽 끝의 문자열도 삭제할 수 있는 매우 유용한 함수 였는데, 공백만 지워준다고 생각하여,,, 매우 기능이 제한적이어서 유용하지 않은 함수라고 생각했었다.
- lstrip(), rstrip()은 각각 문자열 왼쪽, 오른쪽에 있는 문자를 지워준다.


```python
string = "hello world"
x = string.strip("hello ")
print(x) 
# "world"

y = string.strip("h""d")
print(y)
# "ello worl"

z = string.lstrip("h""e")
print(z)
# llo world

```

