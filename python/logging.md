# logging

`import logging`

### log 수준

`logging.debug` : 상세한 정보, 문제 진단 시에 사용

`logging.info` : 예상대로 작동하는 지 확인

`logging.warning` : 예상치 못한 일이 발생했거나, 가까운 미래에 발생할 문제 

`logging.error` :  문제 발생

`logging.critical` : 가장 높은 수준의 문제 발생

### 파일에 로깅 하기

```jsx
import logging
import datetime.datetime.now

logging.basicConfig(filename="logging.log", encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger(now())
logger.info("Hello World!")
```

### 파일과 console창에 로그 남기기

```python
import logging
from datetime import datetime

logging.basicConfig(filename="logging.log", level=logging.DEBUG)
created_at = str(datetime.now())

logger = logging.getLogger(created_at)

streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('./logging.log')

formatter = logging.Formatter(" %(asctime)s %(levelname)s %(message)s")
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

logger.setLevel(level=logging.DEBUG)

logger.info("hello world!")
```

## Reference

- [https://inma.tistory.com/136](https://inma.tistory.com/136)
- [https://docs.python.org/ko/3/howto/logging.html](https://docs.python.org/ko/3/howto/logging.html)
