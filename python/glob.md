`glob.glob()` : 원하는 디렉토리의 파일을 디렉토리로 반환

- 하위 경로의 파일이나 특정 확장자를 가진 파일들을 복사, 이동 등의 작업을 할 때 활용하자!

```python
import glob

image_files = glob.glob("경로/*.jpg")
```
