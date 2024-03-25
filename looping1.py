#1. Aku cinta Indonesia
#3. Aku cinta Indonesia
#5. Aku cinta Indonesia

lis = 1
for i in range (3) :
    print(f"{lis}.Aku Cinta Indonesia")
    lis += 2
#2 4 7 11 16 22
a = 1
b = 1
for i in range(7) : 
    print(a,end=" ") 
    a += b 
    b += 1
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
print('')
for i in range(1,4) : 
    print("1 x",i,"=", 1 * i ) 
print('')
#7 x 6  = 42
#7 x 7  = 49
#7 x 8  = 56
#7 x 9  = 63
#7 x 10 = 70
for i in range(6,11) : 
    print("7 x",i,"=", 7 * i ) 
print('')
#* * * *
lis = "* * * *"
for i in range (3) :
    print(f"{lis}")
print('')
# + + +
# + + +
# + + +
kolom = 3
baris = 3
for i in range(baris):
    for j in range(kolom):
        print("+" , end =" ")
    print()
print()
#1 1 1 1
#2 2 2 2
#3 3 3 3
for i in range(3,4):
    print(i * "1")
    print(i * "2")
    print(i * "3")
 #1 1 2 3 5 8 13 21 34 55
a, b = 1, 1
length = 8

print(a, b, end=' ')
for i in range(length):
    c = a + b 
    print(c, end=' ')
    a = b
    b = c
print()
