import sqlite3 as sql
conn = sql.connect('private.db')
cursor = conn.cursor()
def menu():
    print("Xosh Geldiniz!")
    button = int(input("Hesaba Daxil Olmaq Ucun 1\nGeydiyyatdan Kecmey Ucun 2\nDuymesini secin\n:"))
    if button==2:
        register()
    elif button == 1:
        login()
    
def db_yarat():
    cursor.execute('''CREATE TABLE IF NOT EXISTS privatedatas(
                   name TEXT NOT NULL,
                   login TEXT NOT NULL,
                   password TEXT NOT NULL)''')
    conn.commit()

def register():
    name = input("Adiniz\n:")
    email = input("Electron Poct\n:")
    password = input("Sifre Teyin Edin\:")
    cursor.execute('''INSERT INTO privatedatas(name,login,password) VALUES (?,?,?) ''',
                   (name,email,password))
    conn.commit()
def login():
    login = input("Login\n:")
    password = input("Sifre:\n")
    cursor.execute('SELECT * FROM privatedatas WHERE login = ? AND password = ?',(login, password))
    datas = cursor.fetchall()
    if datas:
        print("Giris Ugurlu")
    else: print("Ugursuz")
 

db_yarat()
while True:
    menu()