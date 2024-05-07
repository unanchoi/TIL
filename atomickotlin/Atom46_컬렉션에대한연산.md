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

`filter()` 주어진 술어와 일치하는 모든 원소가 들어있는 새 리스트 ( 반대 : `filterNot()`)
`any()` 원소 중 어느 하나에 대해 술어가 true를 반환하면 true
`all()`은 모든 원소가 술어와 일치하는지 검사한다.
`none()`은 술어와 일치하는 원소가 하나도 없는지 검사한다.
`find()`와 `firstOrNull()`은 모두 술어와 일치하는 첫 번째 원소를 반환한다. 원소가 없을 때 find()는 예외를 던지고, findOrNull()은 null을 반환한다.
`lastOrNull()`은 술어와 일치하는 마지막 원소를 반환, 일치하는 원소가 없으면 null을 반환한다.
`count()`는 술어와 일치하는 원소의 개수를 반환한다.

```Kotlin
val (pos, neg) = list.partition {it > 0 }  
pos eq "[5, 7, 10]"  
neg eq "[-3, -1]"
```


sumOf()
```kotlin
data class Product(  
    val name: String  
    val price: Double  
) {  
  
}  
  
  
val products = listOf(  
    Product("Apple", 1.0),  
    Product("Banana", 2.0),  
    Product("Orange", 3.0)  
)  
  
products.sumOf { it.price } eq 6.0}
```


`take()` , `drop()` 은 각각 첫 번째 원소를 취하고, 첫 번쨰 원소를 제거한다. `takeLast()`와 `dropLast()` 는 각각 마지막 원소를 취하거나 제거한다.

```kotlin
val list = listOf('a', 'b', 'c', 'X', 'Z')  
list.takeLast(3) eq "[c, X, Z]"  
list.takeLastWhile { it.isUpperCase() } eq "[X, Z]"  
list.drop(1) eq "[b, c, X, Z]"  
list.dropWhile { it.isLowerCase() } eq "[X, Z]"
```

Set에서도 적용할 수 있음. -> Set에 적용하면 결과는 List
```kotlin
val set = setOf("a", "ab", "ac")  
set.maxByOrNull { it.length }?.length eq 2  
    set.filter {  
        it.contains("b")  
    } eq listOf("ab")  
  
    set.map { it.length } eq listOf(1, 2, 2)
```
