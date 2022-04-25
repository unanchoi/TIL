## shutil

- folder 혹은 file을 이동, 복사하는 python 내장 라이브러리

```python
import shutil
```

`shutil.rmtree(path)` : path 디렉토리 or 파일 삭제 (하위 디렉토리와 파일 모두 삭제)_

`shutil.copytree(src,dest)` : src 디렉토리를 dest 디렉토리로 복사

- 파일을 복사하는 함수

⇒ copyfile < copy < copy2

`shutil.copyfile(src, dest)` 

`shutil.copy(src, dest)`  : 파일과 파일의 권한까지 복사

`shutil.copy2(src, dest)` : 파일과 파일의 메타데이터까지 복사

- `shutil.move(src, dest)` : 파일 또는 디렉토리 이동
```python
import shutil

src = "./input/hello.txt"
dest = "./output/hello.txt"
shutil.move(src, dest,copy_function=copy2)

```
