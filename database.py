import sqlite3

db = sqlite3.connect("mahsulotlar.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    narx INTEGER,
    miqdor INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM products")
mahsulotlar_soni = cursor.fetchone()[0]

if mahsulotlar_soni == 0:
    mahsulotlar = [
        ("Olma", 12000, 20),
        ("Banan", 18000, 15),
        ("Nok", 14000, 12),
        ("Uzum", 25000, 10),
        ("Apelsin", 22000, 18),
        ("Anor", 20000, 9),
        ("Shaftoli", 16000, 14),
        ("O‘rik", 17000, 11),
        ("Qovun", 30000, 6),
        ("Tarvuz", 35000, 5),
        ("Non", 4000, 30),
        ("Sut", 12000, 16),
        ("Tuxum", 18000, 25),
        ("Guruch", 22000, 20),
        ("Makaron", 9000, 17),
        ("Shakar", 13000, 13),
        ("Un", 8000, 22),
        ("Yog‘", 19000, 12),
        ("Choy", 15000, 10),
        ("Qahva", 45000, 7),
        ("Daftar", 7000, 40),
        ("Ruchka", 3000, 50),
        ("Qalam", 2500, 35),
        ("O‘chirg‘ich", 2000, 28),
        ("Chizg‘ich", 5000, 19),
        ("Quloqchin", 150000, 5),
        ("Sichqoncha", 90000, 8),
        ("Klaviatura", 250000, 4),
        ("Fleshka", 80000, 12),
        ("Telefon g‘ilofi", 50000, 10)
    ]

    cursor.executemany("""
    INSERT INTO products (nom, narx, miqdor)
    VALUES (?, ?, ?)
    """, mahsulotlar)

    db.commit()
    print("30 ta mahsulot qo‘shildi.")
else:
    print(f"Bazada allaqachon {mahsulotlar_soni} ta mahsulot bor.")

db.close()