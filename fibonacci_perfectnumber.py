'''İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturun. Örnek: [ 1, 1, 2, 3, 5, 8, 13, 21, 34..... ]
Fibonacci Serisi : Serideki her bir sayı kendisinden önceki iki sayının toplamına eşittir.

'''
Number = 20 #ilk yirmi eleman
my_List=[1,1]
# birinci ve ikinci sayıların değeri 1
i = 0
First_Value = 1
Second_Value = 1
           
# sonraki elemanı oluştur
while(i < Number):
    if(i <= 1):
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
        my_List.append(Next)
    #print(my_List)
    i = i + 1
print(my_List)


###########################################
#Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. Örnek: 1 + 2 + 3 = 6
#Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 
#############################################
sayi=int(input("Lütfen bir sayi giriniz"))
carpantoplam=0
for j in range(1,sayi):
    if sayi%j==0:
        carpantoplam+=j
if carpantoplam==sayi:
    print(f"sayi mükemmel sayıdır:{sayi}") 
else:
    print(f"sayi mükemmel değildir:{sayi}")
