```python
import cv2
from PIL import Image
```

### Image 불러오기

```python
PATH = "이미지 경로"
image = Image.open(PATH) # 이미지 불러오기

print(image.size) # 이미지 사이즈 출력 (가로 , 세로)
print(image.width) # 이미지 가로
print(image.height) # 이미지 세로

image.show() # 이미지 출력
```

## cv2 Image 관련 메소드

- 읽어올 방식에는 여러가지가 있지만, `IMREAD_COLOR` , `IMREAD_GRAYSCALE` 가 계산량이 더 적으므로, 사용 추천
- `image.shape` 는 (height, width, dim) 이 tuple로 return된다.
- `cv2.cvtColor('이미지파일', 색어떻게 바꿀지)`

⇒ option으로, 여러가지가 있다. opencv로 사진을 읽게되면, 기본적으로 BGR로 읽기 때문에,

RGB로 바꿔야 한다.

- `cv2.imshow(”이미지 창 타이틀”, image파일)` 은 이미지를 보여준다.

이 때 원본 이미지 사이즈 그대로 창을 띄워주기 때문에, 만약에 사이즈가 클 경우에 보기 힘들어진다.

⇒ `cv2.namedWindow(”이미지 파일”, cv2.WINDOW_NORMAL)` 후에 imshow로 창을 띄우면 사이즈 조절이 가능해진다. (default는 `cv2.WINDOW_AUTO`)

- `cv2.waitkey(밀리 초)` : 창이 띄워진 상태로 대기
- `cv2.destroyAllWindows`, `cv2.destroyWindows` : 창을 닫는다.
- `cv2.moveWindow("이미지파일", width, height)` : 전체화면 크기를 기준으로 width, height 좌표로 사진이 이동한다. ⇒ 사진을 resize 하거나 띄웠을 때, 화면에서 사라지는 경우가 있다. 이때 사용하면 된다.
- `cv2.resizeWindow(winname=이미지, width, height)` : 이미지 창 사이즈를 바꿔준다.

### 이미지 사이즈 변경

- `cv2.resize(src, dsize, interpolation)` : 이미지의 사이즈를 바꿔준다.
- `cv2.resize(src, (0,0), fx, fy, interpolation`) : 이미지의 사이즈를 상대크기로 바꿔준다.

⇒ fx, fy 는 비율이 들어가면 된다.(가로 세로 크기 1/2 ⇒ fx = 0.5, fy = 0.5)

- interpolation은 어떤 보간법을 사용할 지 정하는 것이고, option마다 전환 속도와 선명도에 tradeoff가 있다.
- 축소 시에는 `cv2.INTER_AREA` 를 많이 사용한다고 한다.
- 확대 시에는 `cv2.INTER_LINEAR` 를 많이 사용한다고 한다.
