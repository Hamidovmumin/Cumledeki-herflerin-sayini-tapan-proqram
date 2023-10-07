cumle = input("Cümləni daxil edin: ")

herf_sayisi = 0
for i in cumle:
    if i.isalpha():
        herf_sayisi += 1

print("Cümlədəki hərflərin sayı:", herf_sayisi)

#================================================= isalpha() metodu ===================================================#
## Əgər daxil olunan ifadə hərfdirsə True əks halda False qaytarır
# metin = "12345"
# sonuc = metin.isalpha()
# print(sonuc)  # False

# metin = "abcd"
# sonuc = metin.isalpha()
# print(sonuc)  # True
##=====================================================================================================================#