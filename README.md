#analisis 1
Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris
hero1 = Hero...? Coba lakukan print(hero1.hp).

setelah diubah tidak ada perubahan signifikan

#analisis 2
Perhatikan parameter lawan pada method serang. Parameter tersebut
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
penting?

hal ini penting karena jika suatu objek mau berinteraksi dengan objek lain maka dengan memakai objek utuhlah cara paling efektif

#analisis 3
• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian
jalankan programnya.

akan muncul error "AttributeError: 'Mage' object has no attribute 'name'"

• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat
pembuatan objek?

Parameter "Eudora" hanya melewati __init__ sebagai variabel lokal. Tanpa super(), tidak ada yang memerintahkan self.name = name untuk dieksekusi

• Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke
class Induk!

jika dijelaskan dengan analogi sederhana maka 
Tanpa super():
Kamu mengisi formulir tambahan (mana = 100)
tapi formulir induk (nama, hp, power) dibiarkan kosong
Saat ditanya "siapa namamu?" → error kolom nama kosong

Dengan super():
Kamu mengisi formulir induk dulu (nama, hp, power)
lalu mengisi formulir tambahan (mana)
Semua data lengkap

Tugas Analisis 4:
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling
bawah (luar class):
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan
temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman
yang baik.

Mencoba akses paksa: 100
0
tidak error nilai HP muncul

2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya
hanya self.__hp = nilai_baru.
Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method
Setter sangat penting untuk menjaga integritas data dalam game!

HP Hero = -100
hero1.diserang(50)                     
sisa_hp = -100 - 50 = -150            
set_hp(-150) → self.__hp = -150

validasi di setter adalah penjaga terakhir integritas data.
Tanpa setter yang benar → data bisa jadi sampah
→ game bug → pemain marah → game gagal

Tugas Analisis 5:
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh
blok method def serang(self, target):. Jalankan programnya.
Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
pesan error Can't instantiate abstract class Hero with abstract
method...?
=TypeError: Can't instantiate abstract class Hero with abstract method serang.Tidak bisa membuat objek dari class Hero karena Hero belum menyelesaikan kewajibannya method serang masih belum dibuat

Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di
Interface?

akan terjadi error saat tengah memainkan game yang bisa perpotensi menghilangkan progres pemain

2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit().
Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

gameUnit bukan karakter nyata.
gameUnit adalah cetakan / blueprint
untuk memastikan semua karakter yang dibuat sudah lengkap dan siap dimainkan

Tugas Analisis 6:
1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf
pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class
baru bernama Healer(Hero).
Isi method serang milik Healer dengan: print(f"{self.name} tidak
menyerang, tapi menyembuhkan teman!").
Masukkan objek Healer ke dalam list pasukan.
o Pertanyaan: Apakah program berjalan lancar?
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
ketika harus mengupdate game dengan karakter baru di masa depan?

Program berjalan lancar tanpa mengubah satu huruf pun pada loop
dengan polimorfisme jika ingin menambah sesuatu tidak perlu menambah banyak hal tinggal menambah class baru

2. Konsistensi Penamaan: Ubah nama method serang pada class Archer
menjadi tembak_panah. Jalankan program.
Pertanyaan: Apa yang terjadi?
Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
berbagai Child Class harus persis sama?

--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Hero menyerang dengan tangan kosong.<-- output miya berubah
Zilong (Fighter) memukul dengan pedang! Slash!
Gord (Mage) menembakkan Bola Api! Boom!
Rafaela tidak menyerang, tapi menyembuhkan teman!
python malah menjalankan serang() milik Parent class hero

karena jika tidak sama maka output antara akan tidak ada sama sekali ataupakai default