# IoU (Intersection over Union)

![image](https://user-images.githubusercontent.com/81692211/164349457-8fd5c44e-89ea-40fb-b40d-1275b311a724.png)

- detection model의 성능평가 과정에서 사용되는 공식
- test 진행시에 ground-truth box와 bounding box의 IoU를 구하여, 미리 정해둔 threshold를 넘을 경우에, object detection을 한걸로 판단하여, ground-truth와 같은 Class로 labelling 한다.

```python
def iou(gt_box : tuple , box : tuple):
    gt_box_left = int(gt_box[0])
    gt_box_top = int(gt_box[1])
    gt_box_right = int(gt_box[2])
    gt_box_bottom = int(gt_box[3])

    A_gt = (gt_box_right - gt_box_left) * (gt_box_bottom - gt_box_top)

    pred_box_left = int(box[0])
    pred_box_top = int(box[1])
    pred_box_right = int(box[2])
    pred_box_bottom = int(box[3])

    A_pred = (pred_box_right - pred_box_left) * (pred_box_bottom - pred_box_top)


    # 왼쪽 위 point
    x1 = np.maximum(pred_box_left, gt_box_left)
    y1 = np.maximum(pred_box_top, gt_box_top)

    # 오른쪽 아래 point
    x2 = np.minimum(pred_box_right, gt_box_right)
    y2 = np.minimum(pred_box_bottom, gt_box_bottom)

    # 교차 영역 구하기
    A_intersection = np.maximum(0, x2 - x1) * np.maximum(0, y2 - y1)
    A_union = A_gt + A_pred - A_intersection
    iou = abs(A_intersection / A_union)

    return iou
```
