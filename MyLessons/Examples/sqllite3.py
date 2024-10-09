import sqlite3 as sql
conn = sql.connect("isciler.db")
cursor = conn.cursor()

def menu():
    button = int(input("isci elave etmek ucun 1\niscilere baxmaq ucun2\niscini guncellemek ucun 3\niscini silmey ucun 4\nduymesini secin\n:"))
    if button==1:
        isci_elaveet()
    elif button == 2:
        isci_listele()
    elif button == 3:
        isci_guncelle()
    elif button == 4:
        isci_sil()
        
def db_yarat():
    cursor.execute('''              
    create table if not exists fehleler(
    id integer primary key autoincrement,
    name text not null,
    surname text not null,
    age integer  not null
                   )
                  ''')
conn.commit()
        
def isci_elaveet():
    name = input("iscinin adin daxil edin\n:")
    surname = input("iscinin soyadin daxil edin\n:")
    age = int(input("iscinin yasin geyd edin\n:"))
    cursor.execute('insert into fehleler(name,surname,age) values (?,?,?)',
                   (name,surname,age))
    conn.commit()
    print("ugurla elave edildi!\n")
     
    
def isci_listele():
    cursor.execute('select * from fehleler')
    isciler = cursor.fetchall()
    for i in isciler:
        print(f"\nid:{i[0]} name: {i[1]} surname: {i[2]} age: {i[3]}\n")
        
def isci_guncelle():
    isci_listele()
    isci_id = int(input("guncellenecek id'ni daxil edin"))
    yeni_ad = input("yeni ad\n:")
    yeni_soyad = input("yeni soyad\n:")
    yeni_yas = int(input("yeni yas\n:"))
    cursor.execute('''update fehleler set name = ?, surname = ?, age = ?
                   where id = ?''',
                   (yeni_ad,yeni_soyad,yeni_yas,isci_id))
    conn.commit()
    print("ugurla guncellendi!\n")
def isci_sil():
    isci_listele()
    isci_id = int(input("silmey istediyiniz iscinin id'sin daxil edin\n:"))
    cursor.execute('''delete from fehleler where id = ?''',(isci_id,))
    conn.commit()
    print("ugurla silindi!\n")

db_yarat()
 
while true:
    menu()
