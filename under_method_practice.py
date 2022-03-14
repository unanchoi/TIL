
class Animal:
    
    def __str__(self):
        return '나는 동물이다.'

    def __repr__(self):
        return '나는 동물 객체이다.'


dog = Animal()

dog # dog 객체를 호출하면, 나는 동물 객체이다. 를 출력
str(dog) # '나는 동물이다'

print(dog) # 나는 동물이다
print(str(dog)) # 나는 동물이다.
