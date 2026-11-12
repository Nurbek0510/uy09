from database import db, cursor

ruxsat_etilgan_ustunlar = ["nom", "narx", "miqdor"]


def get_products(columns=None):
    if columns:
       
        for ustun in columns:
            if ustun not in ["id"] + ruxsat_etilgan_ustunlar:
                print("Bunday ustun mavjud emas.")
                return []

        ustunlar = ", ".join(columns)
    else:
        ustunlar = "*"

    cursor.execute(f"SELECT {ustunlar} FROM products")
    return cursor.fetchall()


def insert_products(columns, values):
    for ustun in columns:
        if ustun not in ruxsat_etilgan_ustunlar:
            print("Bunday ustunga ma’lumot qo‘shib bo‘lmaydi.")
            return

    ustunlar = ", ".join(columns)
    savollar = ", ".join(["?"] * len(columns))

    cursor.execute(
        f"INSERT INTO products ({ustunlar}) VALUES ({savollar})",
        values
    )
    db.commit()
    print("Mahsulot qo‘shildi.")


def update_products(id, column, value):
    if column not in ruxsat_etilgan_ustunlar:
        print("Ustun nomi noto‘g‘ri.")
        return

    cursor.execute("SELECT id FROM products WHERE id = ?", (id,))
    mahsulot = cursor.fetchone()

    if mahsulot is None:
        print("Bunday ID dagi mahsulot topilmadi.")
        return

    cursor.execute(
        f"UPDATE products SET {column} = ? WHERE id = ?",
        (value, id)
    )
    db.commit()
    print("Mahsulot yangilandi.")


def delete_products(id):
    cursor.execute("SELECT id FROM products WHERE id = ?", (id,))
    mahsulot = cursor.fetchone()

    if mahsulot is None:
        print("Bunday ID dagi mahsulot topilmadi.")
        return

    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    db.commit()
    print("Mahsulot o‘chirildi.")