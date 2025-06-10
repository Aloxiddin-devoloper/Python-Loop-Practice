#Dastur foydalanuvchidan “O‘zbekiston poytaxti nima?” deb so‘raydi. 
# “Toshkent” deb to‘g‘ri javob berguncha so‘rashda davom etadi.

answer = "Toshkent"

#for i in range(5):
    #option = input("O'zbekiston poytaxti nima :")
    #if option.capitalize() == answer:
        #print("Siz to'g'ri topdinggiz.")
        #break
#else:
    #print("siz topa olmadinggiz! Urinishlar soni ko'p!")
        
        
        
while True:
    option = input("O'zbekiston poytaxti nima? :")
    if option.capitalize() == answer:
        print("Siz tog'ri topdinggiz")
        break
    else:
        print("Siz to'g'ri topa olmadinggiz qaytadan urining!")
        
        
# har doim ishlaydigan whilega shart berdim siz kiritgan narsa answerga teng bo'lsa 
#if shart ishlab kod tugaydi bo'lmasa else ishlab boshqattan urinib ko'ring yozuv chiqaradi