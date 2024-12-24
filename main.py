# try:
#     son =int(input("son kiriting: "))
#     print(son)
# except:
#     print("san son kiritmading!")

# from fung import summa, ayir

# a = int(input("1-sonni kiriitng: "))
# b = int(input("2-sonni kiriitng: "))
# amal = input('Matimatik amal kiriting: ')

# if amal == '+':
#     print(summa(a, b))

# elif amal == '-':
#     print(ayir(a, b))

# 10-dars
# 1-vazifa

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# print(toliq_ism_yasa("Ibrohim", 'Asdulayev'))

# 2-vazifa

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {}
#     avto['kompania'] = kompaniya
#     avto['model'] = model
#     avto['rangi'] = rangi
#     avto['korobka'] = korobka
#     avto['yili'] = yili
#     avto['narxi'] = narhi=None
#     return avto

# avtom = input("Avtomobilni kompaniyasini kiriting: ")
# avtom1 = input("Avtomobilni modelini kiriting: ")
# avtom2 = input("Avtomobilni rangi kiriting: ")
# avtom3 = input("Avtomobilni korobkasi kiriting: ")
# avtom4 = input("Avtomobilni yili kiriting: ")

# print(avto_info(avtom, avtom1, avtom2, avtom3, avtom4))


# def sum_bolinuvchilar(son: int) -> int:
#     sonlar = []
#     for i in range(1, son+1):
#         if son % i == 0:
#             sonlar.append(i)
#     return sum(sonlar)


# user_son = int(input("Son kiring: "))
# print(sum_bolinuvchilar(user_son))


# def sum_boluvchilar(son: int) -> int:
#     sonlar = []
#     for i in range(1, son+1):
#         if son % i == 0:
#             sonlar.append(i)
#     return len(sonlar)


# user_son = int(input("Son kiring: "))
# print(sum_boluvchilar(user_son))

# def find_max_min(*sonlar):
#     mx = max(sonlar)
#     mn = min(sonlar)
#     return f"Eng kattasi {mx}, eng kichigi {mn}"

# print(find_max_min(10, 20, 15, 24646531, 9))

# 4-dars

# 1
# user_input = input("Sonlarni kiriting: ")
# def max_min():
#     My_list = []
#     for i in user_input.split(', '):
#         My_list.append(int(i))
#     return f"Eng kattasi: {max(My_list)}, Eng kichkinasi {min(My_list)}"

# print(max_min())

# 5-dars
# 1-vazifa. Lambda funksiyasi yordamida berilgan ikkita sonning yig'indisini qaytaring.
# Input: 3, 7 Natija: 10
# yigindi = lambda a,b: a + b
# natija = yigindi(3, 7) 
# print(natija)

# 2-vazifa. Lambda funksiyasi yordamida berilgan ro'yxatdagi eng katta sonni qaytaring.
# Input: [1, 5, 3, 9, 2] Natija: 9

# numbers = [1, 5, 3, 9, 2]

# max_number = max(numbers, key=lambda x: x)

# print(max_number)

# 3-vazifa. Lambda funksiyasi yordamida ikkita stringni birlashtiring.
# Input: 'hello', 'world' Natija: 'helloworld'
# Ikkita stringni birlashtirish uchun lambda funksiyasi

# stringlar = lambda a, b: a + b

# javob = stringlar('hello', 'world')

# print(javob)

# 4-vazifa. Lambda funksiyasi yordamida berilgan matn a harfi bilan boshlanadimi yoki yo'qligini aniqlang
# Input: 'apple' Natija: True
# Input: 'banana' Natija: False"

# a_harfini_bel = lambda s: s.startswith('a')

# javob = a_harfini_bel('apple')
# savol = a_harfini_bel('banana')

# print(javob)
# print(savol)

# 6-dars
# 1-vazifa

# import calendar
# import datetime

# today = datetime.datetime.today()
# print(f'Bugun: {today}', end='\n\n')

# print(calendar.month(today.year, today.month))
# user_oy = int(input("Oy nomeri: "))
# print(calendar.month(2011, user_oy))


# # 2-vazifa
# import calendar
# from datetime import datetime

# oy = int(input("Oy raqamini kiriting (1-12): "))

# yiling = datetime.now().year

# kalendar = calendar.month(yiling, oy)
# print(kalendar)

# # 3-vazifa
# from datetime import datetime

# birth_date = input("Tug'ilgan kuningizni kiriting (YYYY-MM-DD): ")
# kun = datetime.strptime(birth_date, "%Y-%m-%d")

# now = datetime.now()

# xozi_vaqt = now - birth_date

# xozi = xozi_vaqt.total_seconds() / 3600

# print(f"Siz {xozi:.0f} soat yashadingiz.")

#  7-dars
# 2-vazifa

# Fayllar bilan ishlash

# "r" – (read) faqat o'qish uchun ochish (standart rejim).
# "w" – (write) yozish uchun ochish (agar fayl mavjud bo'lsa, ma'lumot o'chiriladi, 
#               aks holda yangi fayl yaratiladi).
# "a" – (append) mavjud fayl oxiriga yozish uchun ochish.
# "b" – (bianry) ikkilik rejim (binary files, masalan, rasm va videolar uchun).
# "r+" – o'qish va yozish uchun ochish.

# fayl = open("qolda.txt", 'r')
# print(fayl.read())
# fayl.close()

# new = open('qolda.txt', 'w')
# new.write("Barca kuchli")
# new.close()

# fayl = open('abubakr.txt', 'a')
# fayl.write('Abubakr yaxshi bola\n')
# fayl = open('abubakr.txt', 'r')
# print(fayl.read())


# fael = "oquvchi.txt"

# def add_student(name):
#     with open(fael, "a") as file:
#         file.write(name + "\n")

# def read_students():
#     with open(fael, "r") as file:
#         return file.readlines()

# while True:
#     oquvchi_name = input("Ismingizni kiriting (to'xtatish uchun 0 ni kiriting): ")
    
#     if oquvchi_name == "0":
#         print("\nFayldagi barcha ismlar:")
#         students = read_students()
#         for student in students:
#             print(student.strip())
#         break
#     else:
#         add_student(oquvchi_name)
#         print(f"{oquvchi_name} ismli talaba faylga qo'shildi.")

# 8-dars

# "Students.txt nomli yangi fayl yaratilsin.

# add_students() nomi yangi funksiya yaratilsin va u chaqirilganda har safar foydalanuvchidan student ism familiyasi so'ralsin va kiritilgan har bir ism-familiyani Students.txt fayliga qo'shilsin. Toki stop so'zi kiritilganda student qo'shish jarayoni tugasin.
# Input: Cristiano Ronaldo Karim Benzema Klian Mbappe stop

# Natija: Yuqorida kiritilgan ism-familiyalar Students.txt ga qo'shilgan bo'lishi kerak

# get_students() nomli funksiya yaratilsin va u funksiya chaqirilganda Students.txt faylidagi barcha studentslarning ism-familiyalari yangi qatordan chiqarilsin
# Input: yo'q Natija: Cristiano Ronaldo Karim Benzema Klian Mbappe"'

# def add_students():
#    while True:
#     oquvchi_name = input("Ismingizni kiriting (to'xtatish uchun 0 ni kiriting): ")
    
#     if oquvchi_name == "0":
#         break
#     else:
#         file = open('students.txt', 'a')
#         file.write(f'{oquvchi_name}\n')
#         file.close()
#         print(f"{oquvchi_name} ismli talaba faylga qo'shildi.")

# add_students()

# def get_students():
#     try:
#         with open('Students.txt', 'r') as file:
#             students = file.readlines()

#         for student in students:
#             print(student.strip())

#     except FileNotFoundError:
#         print("Students.txt fayli topilmadi.")

# get_students()


# 1-ooep
# import random

# l = []
# a = random.randint(1,10)
# l.append(a)

# def sonlar ():
#     try:
#         with open('toq.txt', 'r') as file:
#             sonlar = file.readlines

#         with open('juft.txt', 'r') as file:
#             sonlar = file.readlines

#     for sonlar in range(1,11):
#         print(sonlar.strip)

# print(l)
# sonlar()

# Amaliy dars
# - OOP da o'tilgan barcha mavzularni birlashtirgan xolda Vending machine loyihasini amalga oshirish

# - Bunda, SavdoAvtomati va Haridor nomli klasslar bo'ladi. Maxsulotlar alohida faylda products nomli dict ichida saqlangan bo'ladi

# - SavdoAvtomati klassida (id, address, products, cash_balance) kabi atributlari bo'ladi. products atributi products.py ni ichida saqlangan products nomli dictga teng bo'ladi, cash_balance esa odatiy xolatda 0ga teng bo'ladi

# Ushbu klassda add_product(product), get_products(), get_cash_balance(), set_cash_balance(balance) kabi metodlari bo'ladi

# - Haridor klassida esa (card_number, card_balance, card_password, cash_balance) nomli atirbutlari bo'ladi, cash_balance bu haridorning cho'ntagidagi naqd bul balansi hisoblanadi

# Ushbu klassda get_card_balance(), get_cash_balance(), set_cash_balance(balance), set_card_balance(balance), get_password() kabi metodlari bo'ladi

# Loyihani ishga tushirish jarayoni While True bilan amalga oshiriladi, dastur ishga tushganda foydalanuvchidan qaysi usulda mahsulot sotib olish so'raladi va tanlovga qarab dastur ishga tushishi kerak
