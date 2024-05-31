a = 8
b = 5

print('Перше завдання: Оператор and')
print(a > b and b < a)  
print(a != b and b < a)  
print(a < b and b > a) 
print(a == b and b < a)  
print('Друге завдання: Оператор or')
print(a > b or b > a)  
print(a == 8 or b == 5) 
print(a < b or b > a)  
print(a == 0 or b == 0) 

s1 = "Tsuki"
s2 = "Akane"

print('Третє завдання: Змінні рядкового типу')
print(len(s1) == 5 and s1 != s2) 
print(s1 >= s2 and len(s2) == 5)  
print(s1 == s2 and len(s1) == 4)  
print(s1 > s2 and len(s2) != 5)  

print('Четверте завдання: Виведення повідомлення при значенні змінної більше 0')
x = -7  

if x > 0:
    print("Змінна більше 0")
else:
    print("Змінна менше або дорівнює 0")

print('Четверте завдання: Вдосконалений код з гілкою else')
y = 5 

if y > 0:
    print(1)
else:
    print(-1)


print('Пяте завдання: Програма за описом')
d = 10
e = 15

if d > e:
    c = d - e
elif d < e:
    c = d + e
else:
    c = d

print(f"Значення третьої змінної: {c}")
