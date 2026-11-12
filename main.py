from funksiyalar import (
    get_products,
    insert_products,
    update_products,
    delete_products
)
from database import db


def mahsulotlarni_korsat():
    mahsulotlar = get_products()

    if not mahsulotlar:
        print("Mahsulotlar ro‘yxati bo‘sh.")
        return

    print("\nID | Nomi | Narxi | Miqdori")
    print("-" * 35)

    for mahsulot in mahsulotlar:
        print(f"{mahsulot[0]} | {mahsulot[1]} | {mahsulot[2]} so‘m | {mahsulot[3]} ta")


def mahsulot_qoshish():
    nom = input("Mahsulot nomi: ")

    try:
        narx = int(input("Mahsulot narxi: "))
        miqdor = int(input("Mahsulot miqdori: "))
    except ValueError:
        print("Narx va miqdorni butun son bilan kiriting.")
        return

    insert_products(
        ["nom", "narx", "miqdor"],
        (nom, narx, miqdor)
    )


def mahsulotni_yangilash():
    try:
        id = int(input("Yangilanadigan mahsulot ID si: "))
    except ValueError:
        print("ID ni butun son bilan kiriting.")
        return

    print("O‘zgartiriladigan ustun: nom, narx yoki miqdor")
    ustun = input("Ustun nomi: ").strip().lower()
    qiymat = input("Yangi qiymat: ")

    if ustun in ["narx", "miqdor"]:
        try:
            qiymat = int(qiymat)
        except ValueError:
            print("Narx va miqdor butun son bo‘lishi kerak.")
            return

    update_products(id, ustun, qiymat)


def mahsulotni_ochirish():
    try:
        id = int(input("O‘chiriladigan mahsulot ID si: "))
    except ValueError:
        print("ID ni butun son bilan kiriting.")
        return

    delete_products(id)


while True:
    print("\n========== MAHSULOTLAR ==========")
    print("1. Mahsulotlarni ko‘rish")
    print("2. Mahsulot qo‘shish")
    print("3. Mahsulotni yangilash")
    print("4. Mahsulotni o‘chirish")
    print("5. Dasturni yopish")
    print("=================================")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        mahsulotlarni_korsat()
    elif tanlov == "2":
        mahsulot_qoshish()
    elif tanlov == "3":
        mahsulotni_yangilash()
    elif tanlov == "4":
        mahsulotni_ochirish()
    elif tanlov == "5":
        print("Dastur yopildi.")
        db.close()
        break
    else:
        print("Noto‘g‘ri tanlov. 1 dan 5 gacha son kiriting.")