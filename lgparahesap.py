import math

# yatırdığınız parayı yazdığınız faiz oranına göre kaç yılda 2 ye katlayabileceğinizi gösterir.
# log(2) değerini hangi değer ile değiştiriseniz paranızı kaça katlayacağını gösterir
x = float(input("degeri giriniz: "))
result = math.log(2) / math.log(1+x)

print(result)
