# 아이템 37. ordinal 인덱싱 대신 EnumMap을 사용하라.

이따금 배열이나 리스트에서 원소를 꺼낼 때 ordinal 메서

```Java
class Plant {
  enum LifeCycle {
   ANNUAL, PERENNIAL, BIENNIAL
  }

  final String name;
  final LifeCycle lifeCycle;

  Plant(String name, LifeCycle lifeCycle) {
    this.name = name;
  }

  @Override public String toString() {
    return name;
  }
}
```


#### 안 좋은 예시
```Java
Set<Plant>[] plantsByLifeCycle = (Set<Plant>[]) new Set[Plant.LifeCycle.values().length];

for (int i = 0; i < plantsByLifeCycle.length; i++) {
  plantsByLifeCycle[i] = new HashSet<>();
}

for (Plant p : garden) {
  plantsByLifeCycle[p.lifeCycle.ordinam()].add(p);

  // 결과 출력
   for (int i = 0; i < plantsByLifeCycle.length; i++) {
     System.out.printf("%s: %s%n", Plant.lifeCycle.values()[i],
      plantsByLifeCycle[i]);
   }
}
```
- 배열은 제네릭과 호환되지 않으니 비검사 형변환을 수행해야하고 깔끔하게 컴파일 되지 않음.
- 배열은 각 인덱스의 의미를 모르니 출력 결과에 직접 레이블을 달아야함.
- 정확한 정숫값을 사용한다는 것을 직접 보증해야함.
	-  정수는 열거 타입과 달리 타입 안전하지 않기 때문이다. (ArrayIndexOutOfBoundsException 발생 가능)

#### 해결 방법
열거 타입을 키로 사용할 수 있도록 설계한 Map 구현체 : EnumMap

```Java
Map<Plant.LifeCycle, Set<Plant>> plantsByLifeCycle = new EnumMap<>(Plant.LifeCycle.class);


for (Plant.LifeCycle lc : Plant.LifeCycle.values()) {
  plantsByLifeCycle.put(lc, new HashSet<>());


for (Plant p: garden) {
 plantsByLifeCycle.get(p.lifeCycle).add(p);
 System.out.println(plantsByLifeCycle);
}
}
```

안전하지 않은 형변환 사용 X, 성능 비슷.
EnumMap의 생성자가 받는 Class 객체는 한정적 타입 토큰으로, 런타임 제네릭 타입 정보를 제공한다.(아이템 33)

스트림을 사용해 Map을 관리하면 코드를 더 줄일 수 있다.
다음은 앞 예의 동작을 거의 그대로 모방한 가장 단순한 형태의 스트림 기반 코드이다.

```Java
System.out.println(Arrays.stream(garden))
  .collect(groupingBy((p -> p.lifeCycle)));
```

이 코드는 EnumMap이 아닌 고유한 Map 구현체를 사용했기 때문에 EnumMap을 써서 얻은 공간과 성능 이점이 사라진다는 문제가 있다.

스트림을 사용한 코드2
```Java
System.out.println(Arrays.stream(garden)
				  .collect(groupingBy(p -> p.lifeCycle, ()
				  -> new EnumMap<>(LifeCycle.class), toSet()));
```



EnumMap 버전에서는 상태 목록에 PLASMA를 추가하고, 전이 목록에 IONIZE(GAS, PLASMA)와 DEIONICZE(PLASMA, GAS)만 추가하면 끝이다.

EnumMap 버전에 새로운 상태 추가하기.
```Java

public enum Phase {

  SOLID, LIQUID, GAS, PLASMA;

  public enum Transition {
    MELT(SOLID, LIQUID),
    FREEZE(LIQUID, SOLID),
    BOIL(LIQUID, GAS),
    CONDENSE(GAS, LIQUID),
    SUBLIME(SOLID, GAS),
    DEPOSIT(GAS, SOLID),
    IONIZE(GAS, PLASMA ),
    DEIONIZE(PLASMA, GAS);

   ...
  }
}
```

### 핵심 정리
배열의 인덱스를 얻기 위해 ordinal을 쓰는 것은 일반적으로 좋지 않으니, 대신 EnumMap을 사용하라.
다차원 관계는 EnumMap<..., EnumMap<...>>으로 표현하라.

"애플리케이션 프로그래머는 Enum.ordinal을 웬만해서는 사용하지 말아야한다"는 일반원칙의 특수사례
