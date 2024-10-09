 # Environment (mühit) proqramlaşdırma və sistem inkişafında
# bir proqramın işlədiyi şərtləri və konfiqurasiyanı təsvir edir.

# 1. Nədir Environment?
# Environment, proqramın işlədiyi mühitin konfiqurasiyasını əks etdirir.
# Bu, sistem mühitini, quraşdırılmış kitabxanaları, dəyişənləri və digər sistem resurslarını əhatə edir.

# 2. Niyə Environment-lər Vacibdir?
# - İzolasiya: Müxtəlif layihələr üçün ayrı mühitlər yarada bilərsiniz.
#   Bu, kitabxana versiyalarının bir-birinə təsir etmədən işləməsini təmin edir.
# - Versiya İdarəsi: Hər bir mühitdə fərqli kitabxana versiyalarını istifadə edə bilərsiniz.
#   Bu, layihələrinizi daha asan idarə etməyə kömək edir.
# - Asan İdarəetmə: Layihələrinizi asanlıqla quraşdırmaq, paylaşmaq və mühafizə etmək imkanı verir.

# 3. Conda Environment
# Conda, Python-da mühitlərin yaradılması və idarə olunması üçün geniş istifadə olunan bir paket meneceri və mühit idarəedicisidir.
# Conda ilə fərqli Python versiyaları və kitabxanaları olan mühitlər yarada bilərsiniz.

# 4. Mühitlərin Yaradılması və İdarə Edilməsi
# Aşağıdakı əmrlər Conda mühitlərinin yaradılması və idarə olunması üçün istifadə olunur:

# Yeni bir Conda mühiti yaratmaq:
# !conda create --name myenv python=3.8 -y

# Mühitə girmək:
# !conda activate myenv

# Kitabxana quraşdırmaq:
# !conda install numpy

# Quraşdırılmış kitabxanaların siyahısını göstərmək:
# !conda list

# Mühiti deaktivləşdirmək:
# !conda deactivate

# Mühiti silmək:
# !conda remove --name myenv --all -y

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# SQLite kitabxanası, Python-da istifadə olunan yüngül, diskdə saxlanılan
# bir verilənlər bazası sistemidir. SQLite, tam funksional bir SQL
# verilənlər bazasıdır, lakin ayrı bir serverə ehtiyac duymur.

# 1. Nədir SQLite?
# SQLite, yüngül bir verilənlər bazasıdır, müstəqil bir tətbiq olaraq
# işləyir və sistemin fayl sistemində bir fayl olaraq saxlanılır.
# SQLite, SQL dili vasitəsilə verilənlər bazası əməliyyatlarını yerinə yetirir.

# 2. Niyə SQLite Vacibdir?
# - Yüngül və sadə: Çox az resurs istehlak edir və asanlıqla quraşdırılır.
# - Diskdə saxlanılır: Bütün verilənlər bazası məlumatları tək bir faylda saxlanılır.
# - Daşınabilir: Verilənlər bazası faylını asanlıqla daşıya və paylaşa bilərsiniz.

# 3. SQLite ilə İşləmək
# SQLite ilə işləmək üçün 'sqlite3' modulundan istifadə edirik.
# SQLite kitabxanasında ən çox istifadə olunan funksiyalar:

import sqlite3

# 1. Verilənlər Bazası Bağlantısı
# 'connect' funksiyası ilə verilənlər bazasına bağlantı yaradılır.
connection = sqlite3.connect('mydatabase.db')

# 2. Cursor Yaratmaq
# 'cursor' funksiyası ilə SQL əmrlərini icra etmək üçün bir cursor yaradılır.
cursor = connection.cursor()

# 3. Cədvəl Yaratmaq
# 'CREATE TABLE' əmri ilə yeni cədvəl yaradılır.
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    connection.commit()

# 4. Verilənlər Əlavə Etmək
# 'INSERT INTO' əmri ilə cədvələ yeni verilənlər əlavə edilir.
def add_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    connection.commit()

# 5. Verilənləri Oxumaq
# 'SELECT' əmri ilə cədvəldəki verilənlər oxunur.
def fetch_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# 6. Verilənləri Yeniləmək
# 'UPDATE' əmri ilə mövcud verilənlər yenilənir.
def update_user(user_id, name, age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
    connection.commit()

# 7. Verilənləri Silmək
# 'DELETE' əmri ilə cədvəldən verilənlər silinir.
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connection.commit()

# 8. Cədvəldəki Verilənləri Göstərmək
def display_users():
    users = fetch_users()
    print("İstifadçilər:")
    for user in users:
        print(user)

# 9. Bağlantını Bağlamaq
# 'close' funksiyası ilə verilənlər bazası bağlantısı bağlanır.
def close_connection():
    connection.close()

# Funksiyaları Sınaqdan Keçirmək
create_table()
add_user('Ali', 22)
add_user('Sara', 25)
display_users()
update_user(1, 'Ali', 23)  # ID-si 1 olan istifadəçinin məlumatını yeniləyir
display_users()
delete_user(2)  # ID-si 2 olan istifadəçini silir
display_users()

# Bağlantını bağlayır
close_connection()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
