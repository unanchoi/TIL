46. 컬렉션에 대한 연산

```kotlin

val list1 = List(10) { it }

val list2 = List(10) { 0 }
val list3 = List(10) { 'a' + it }
val list4 = List(10) { list3[it & 3] }
```

이 List 생성자에는 인자가 2개가 있다.
생성할 List의 크기, 각 원소를 초기화하는 람다.


```kotlin

fun main() {
	val mutableList1 = MutableList(5, {10 * (it + 1 )})
	val mutableList2 = MutableList(5) { 10 * (it + 1)}
}
```

`List(), MutableList()` 는 생성자가 아니라 함수이다. 
다양한 컬렉션 함수가 술어를 받아서 컬렉션 원소를 검사함.

`filter()` 주어진 술어와 일치하는 모든 원소가 들어있는 새 리스트
`any()` 원소 중 어느 하나에 대해 술어가 true를 반환하면 true


