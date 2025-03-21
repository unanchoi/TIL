### Garbage Collector의 역할

- Heap 영역에 동적으로 할당된 객체 중 `불필요한 객체(garbage)` 를 찾는다.
- 찾아낸 garbage를 처리해서 메모리를 삭제한다.

### 어떤 객체를 Garbage라고 할까?

- 유효한 참조가 존재하는 객체라면, Reachable 상태
- 그렇지 않다면, Unreachable 상태 ⇒ Garbage 즉, GC의 수거 대상.
- Root set과의 관계로 Reachable, Unreachable을 구분한다.
    - Root set과 참조 관계가 있다면 Reachable, 어떠한 관계도 없다면 Unreachable
- Rootset
    - Stack 영역의 지역 변수, 파라미터
    - Method 영역의 정적 변수
    - JNI에 의해 생성된 객체.

### JVM Heap memory 영역

- Young Generation Old Generation으로 나눠져 있다.
    - YG에서 발생하는 GC를 Minor GC
        - Eden, Survivor로 나뉜다.
            - Eden: 새로운 객체가 저장되는 영역.
            - Survivor: 에덴 영역에서 살아남은 객체가 저장되는 영역
    - OG에서 발생하는 GC를 Major GC라고 한다.
    - 영역을 나누어 일부의 메모리 영역만 스캔한다.
    
    ⇒ 효율적으로 처리할 수 있다.
    
    ⇒ 결과적으로 GC 비용을 줄일 수 있다.
    
- 대부분의 할당된 객체는 오랫동안 참조되지 않으며, 금방 Garbage의 대상이 된다.
- 오래된 객체에서 젊은 객체로의 참조는 거의 없다.

### 동작 방식 (Mark and Sweep)

1. Root set에서 참조하는 객체를 찾는다.
2. Reachable 객체에 의해 참조되는 객체를 찾는다.
3. Root set과 어떠한 관계도 없다면, Unreachable Heap 영역에서 제거한다.

Mark : Rootset으로 부터 Heap 영역의 모든 객체를 스캔하여 Reachable한 객체를 찾는다.

Sweep: Unreachable한 객체를 Heap 영역에서 제거한다.

### GC 언제 발생할까?

1. 새로운 객체는 Eden 영역에 할당된다.
2. Eden영역이 가득차면, Minor GC가 발생한다.
3. 살아남은 객체는 비어있는 Survivor의 영역으로 옮겨진다. 옮겨진 객체의 age는 1 증가한다.
4. 과정을 반복하다가 age가 많아지면 OG로 이동 (Promotion)
5. OG 영역이 가득차면 Major GC가 발생한다.

### Reference

- https://www.youtube.com/watch?v=8JrciOSL3Gk
