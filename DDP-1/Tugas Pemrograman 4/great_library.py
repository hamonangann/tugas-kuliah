def binser_mod(buku, rak):
  """
  Fungsi binser_mod bertujuan untuk menentukan indeks peletakan objek baru.
  Hal ini dilakukan supaya isi buku dalam rak (pada program utama) terurut
  Fungsi ini adalah modifikasi dari Binary Search (https://www.geeksforgeeks.org/binary-search/)

  Parameter:
  - Buku -> objek yang ingin diletakkan pada array
  - Rak -> array terurut tempat meletak objek

  Fungsi akan mengembalikan sebuah integer, yaitu indeks tempat meletak objek
  """
  # Kasus array kosong
  if len(rak) < 1:
    return 0
  kiri = 0
  kanan = len(rak)-1

  # Kasus objek lebih awal dari elemen terkiri, atau lebih akhir dari elemen terkanan 
  if buku < rak[kiri]:
    return 0
  elif buku > rak[kanan]:
    return len(rak)

  # Kasus objek berada di antara elemen terkiri atau terkanan
  while(kanan - kiri > 1):
    tengah = kiri + ((kanan - kiri)//2)
    if buku < rak[tengah]:
      kanan = tengah
    else:
      kiri = tengah
  return kanan 
  # Indeks tempat meletak objek baru akan berada di antara objek kiri dan kanan
  # Maka objek harus diletakkan di indeks kiri + 1 atau kanan
  

class Book:
    """
    Book adalah kelas untuk menampung objek buku
    Ada 4 parameter yang dijadikan atribut privat yang terdapat di setiap buku:
    - Nama
    - Tahun terbit
    - Penulis
    - Penerbit
    Kelas dilengkapi setter/getter untuk memanggil nilai atribut
    Terdapat metode get_book_description yang mengembalikan string berisi deskripsi
    Ada modifikasi operator yaitu < dan >
    Pada keduanya, yang dibandingkan bukan objek tetapi atribut nama dari objek
    Perbandingan berdasarkan urutan leksikografi
    """
    def __init__(self, nama, tahun, penulis, penerbit):
      self.__nama = nama
      self.__tahun = tahun
      self.__penulis = penulis
      self.__penerbit = penerbit
    
    def get_nama(self):
      return self.__nama

    def get_tahun(self):
      return self.__tahun

    def get_penulis(self):
      return self.__penulis
    
    def get_penerbit(self):
      return self.__penerbit
    
    def get_book_description(self):
      return f"Nama Buku: {self.get_nama()}\nTahun: {self.get_tahun()}\nPenulis: {self.get_penulis()}\nPenerbit: {self.get_penerbit()}\n"

    def __lt__(self,other):
      return self.get_nama() < other.get_nama()

    def __gt__(self,other):
      return self.get_nama() > other.get_nama()
    

class FictionBook(Book):
    """
    FictionBook adalah kelas berisi buku berjenis Fiksi
    Ini adalah subclass dari class Book
    Ada atribut tambahan yaitu __genre berisi genre buku
    Ada overriding pada metode get_book_description() untuk menambahkan genre
    """
    def __init__(self, nama, tahun, penulis, penerbit, genre):
      super().__init__(nama, tahun, penulis, penerbit)
      self.__genre = genre
    
    def get_genre(self):
      return self.__genre

    def get_book_description(self):
      return f"Buku Fiksi\n{super().get_book_description()}Genre: {self.get_genre()}\n"
      
    

class ReferenceBook(Book):
    """
    ReferenceBook adalah kelas berisi buku berjenis Referensi
    Ini adalah subclass dari class Book
    Ada atribut tambahan yaitu __kota berisi kota terbit
    Ada overriding pada metode get_book_description() untuk menambahkan kota
    """
    def __init__(self, nama, tahun, penulis, penerbit, kota):
      super().__init__(nama, tahun, penulis, penerbit)
      self.__kota = kota
    
    def get_kota_terbit(self):
      return self.__kota

    def get_book_description(self):
      return f"Buku Referensi\n{super().get_book_description()}Kota terbit: {self.get_kota_terbit()}\n"
    

class Encyclopedia(Book):
    """
    Encyclopedia adalah kelas berisi buku berjenis Ensiklopedia
    Ini adalah subclass dari class Book
    Ada atribut tambahan yaitu __num berisi nomor revisi
    Ada overriding pada metode get_book_description() untuk menambahkan nomor revisi
    """
    def __init__(self, nama, tahun, penulis, penerbit, num):
      super().__init__(nama, tahun, penulis, penerbit)
      self.__num = num
    
    def get_revisi_num(self):
      return self.__num

    def get_book_description(self):
      return f"Buku Ensiklopedia\n{super().get_book_description()}Nomor Revisi: {self.get_revisi_num()}\n"
    

class Shelf:
    """
    Rak adalah class untuk menampung objek rak
    Terdapat satu parameter yaitu nama rak yang dimasukkan ke atribut __nama
    Pada inisiasi, disediakan sebuah list __kumpulan_buku 
    Gunanya untuk menampung objek buku (sebagaimana fungsi rak semestinya)
    Disediakan setter/getter untuk mengakses atribut privat

    Terdapat metode search_buku yang mengembalikan string apabila buku ditemukan
    String berisi pemberitahuan dan deskripsi buku

    Terdapat juga metode list_buku yang mengembalikan nama rak beserta isinya
    """
    def __init__(self, nama):
      self.__nama = nama
      self.__kumpulan_buku = []
    
    def get_nama(self):
      return self.__nama

    def get_kumpulan_buku(self):
      return self.__kumpulan_buku

    def set_kumpulan_buku(self, buku):
      # Memasukkan objek buku ke __kumpulan_buku dengan urutan leksikografis
      indeks = binser_mod(buku, self.get_kumpulan_buku())
      self.__kumpulan_buku.insert(indeks, buku)
    
    def search_buku(self, buku):
      for i in self.get_kumpulan_buku():
        if buku == i.get_nama():
          return f"Buku ditemukan\n\n{i.get_book_description()}"
      return False

    def list_buku(self):
      s = ""
      for i in self.get_kumpulan_buku():
        s = s + f"- {i.get_nama()}\n"
      
      return s
    

class KnowledgeShelf(Shelf):
    """
    KnowledgeShelf adalah class untuk menampung rak berjenis Pengetahuan
    Tidak ada atribut khusus, semua diturunkan dari superclass yaitu Shelf
    Dapat diisi buku berjenis Referensi dan Ensiklopedia

    Terdapat metode add_buku untuk menambahkan buku ke dalam rak
    """
    def __init__(self, nama):
      super().__init__(nama)
    
    def add_buku(self, buku):
      # Apabila rak tidak boleh diisi karena jenis buku
      if isinstance(buku, FictionBook):
        return "Buku gagal ditambahkan :(\n"

      # Menambahkan buku
      self.set_kumpulan_buku(buku)
      return f"Buku baru berhasil ditambahkan pada rak {self.get_nama()}\n\n{buku.get_book_description()}"
    

class WorldShelf(Shelf):
    """
    WorldShelf adalah class untuk menampung rak berjenis Dunia
    Tidak ada atribut khusus, semua diturunkan dari superclass yaitu Shelf
    Dapat diisi buku berjenis Fiksi dan Ensiklopedia

    Terdapat metode add_buku untuk menambahkan buku ke dalam rak
    """
    def __init__(self, nama):
      super().__init__(nama)
    
    def add_buku(self, buku):
      # Apabila rak tidak boleh diisi karena jenis buku
      if isinstance(buku, ReferenceBook):
        return "Buku gagal ditambahkan :(\n"
      
      # Menambahkan buku
      self.set_kumpulan_buku(buku)
      return f"Buku baru berhasil ditambahkan pada rak {self.get_nama()}\n\n{buku.get_book_description()}"
    

class MysteryShelf(Shelf):
    """
    MysteryShelf adalah class untuk menampung rak berjenis Misteri
    Tidak ada atribut khusus, semua diturunkan dari superclass yaitu Shelf
    Dapat diisi buku berjenis Fiksi dan Referensi

    Terdapat metode add_buku untuk menambahkan buku ke dalam rak
    """
    def __init__(self, nama):
      super().__init__(nama)
    
    def add_buku(self, buku):
      # Apabila rak tidak boleh diisi karena jenis buku
      if isinstance(buku, Encyclopedia):
        return "Buku gagal ditambahkan :(\n"

      # Menambahkan buku
      self.set_kumpulan_buku(buku)
      return f"Buku baru berhasil ditambahkan pada rak {self.get_nama()}\n\n{buku.get_book_description()}"
    

class CompendiumShelf(Shelf):
    """
    MysteryShelf adalah class untuk menampung rak berjenis Misteri
    Tidak ada atribut khusus, semua diturunkan dari superclass yaitu Shelf
    Dapat diisi semua jenis buku

    Terdapat metode add_buku untuk menambahkan buku ke dalam rak
    """
    def __init__(self, nama):
      super().__init__(nama)
    
    def add_buku(self, buku):
      # Menambahkan buku
      self.set_kumpulan_buku(buku)
      return f"Buku baru berhasil ditambahkan pada rak {self.get_nama()}\n\n{buku.get_book_description()}"
    

class Library:
    """
    Library adalah kelas untuk menampung The Great Library itu sendiri
    Terdapat satu atribut privat __kumpulan_rak yaitu list berisi rak-rak
    Terdapat setter/getter untuk mengakses atribut privat

    Terdapat metode add_rak dengan parameter nama dan jenis rak
    Tujuannya adalah menambah rak baru ke dalam __kumpulan_rak

    Terdapat metode add_buku dengan parameter:
    -Nama rak
    -Nama buku
    -Tahun terbit
    -Penulis
    -Penerbit
    -Jenis
    -Atribut khusus
    Tujuannya adalah menentukan rak mana yang akan ditambahkan buku,
    selanjutnya diteruskan dengan metode add_buku rak tersebut

    Terdapat metode search_buku untuk memeriksa semua rak
    Metode ini memanggil metode search_buku semua rak

    Terdapat metode list_buku untuk menampilkan daftar buku
    Metode ini menyatukan semua string kembalian setiap rak dalam satu string

    """
    def __init__(self):
      self.__kumpulan_rak = []

    def get_kumpulan_rak(self):
      return self.__kumpulan_rak
    
    def set_kumpulan_rak(self, new_rak):
      self.__kumpulan_rak = new_rak
    
    def add_rak(self, nama, jenis):
      rak = []

      # Apabila rak bernama sama dengan yang sudah ada
      for i in self.get_kumpulan_rak():
        if nama == i.get_nama():
          return f"Rak dengan nama {nama} sudah ada di dalam sistem\n"
      
      # Membuat objek rak sesuai jenisnya
      if jenis == "Pengetahuan":
        rak.append(KnowledgeShelf(nama))
      elif jenis == "Dunia":
        rak.append(WorldShelf(nama))
      elif jenis == "Misteri":
        rak.append(MysteryShelf(nama))
      elif jenis == "Compendium":
        rak.append(CompendiumShelf(nama))
      else:
        return f"Tidak dapat menambahkan Rak dengan jenis {jenis}"
      
      # Menambahkan rak baru
      self.set_kumpulan_rak(self.get_kumpulan_rak() + rak)
      return f"Rak baru berhasil ditambahkan\n\nNama: {nama}\nJenis: {jenis}\n"

    def add_buku(self, rak, buku, tahun, penulis, penerbit, jenis, atribut):
      # Memeriksa keberadaan rak tempat buku akan diletakkan
      for i in self.get_kumpulan_rak():
        if rak == i.get_nama():
          put = i
          break
      else:
        return "Buku gagal ditambahkan :(\n"

      # Memastikan buku yang dimasukkan unik
      if self.search_buku(buku) != f"Buku dengan nama {buku} tidak ditemukan":
        return f"Buku dengan nama {buku} sudah ada di dalam sistem\n"

      # Membuat objek buku sementara
      if jenis == "Fiksi":
        new_buku = FictionBook(buku, tahun, penulis, penerbit, atribut)
      elif jenis == "Referensi":
        new_buku = ReferenceBook(buku, tahun, penulis, penerbit, atribut)
      elif jenis == "Ensiklopedia":
        new_buku = Encyclopedia(buku, tahun, penulis, penerbit, atribut)
      else: # Apabila jenis buku tidak didukung
        return f"Buku gagal ditambahkan :(\n"
  
      # Memasukkan objek buku ke dalam kumpulan buku di rak
      return put.add_buku(new_buku)
    
    def search_buku(self, buku):
      for i in self.get_kumpulan_rak():
        if i.search_buku(buku): # Apabila ditemukan di salah satu rak
          return i.search_buku(buku)
      return f"Buku dengan nama {buku} tidak ditemukan"

    def list_buku(self):
      s = "\n"
      ada = False # Variabel untuk memastikan keberadaan buku dalam list
      for i in self.get_kumpulan_rak():
        daftar = i.list_buku()
        if daftar:
          ada = True
        s = s + f"{i.get_nama()}\n{daftar}"
      return s if ada else "Belum ada buku di dalam sistem :(\n"
    

def main():
    """
    Melakukan inisiasi The Great Library dengan 4 rak
    Membuat infinite loop yang meminta perintah untuk memodifikasi perpustakaan
    """

    # Inisiasi awal
    lib = Library()
    lib.add_rak("Pengetahuan01", "Pengetahuan")
    lib.add_rak("Dunia01", "Dunia")
    lib.add_rak("Misteri01", "Misteri")
    lib.add_rak("Compendium01", "Compendium")

    # Loop
    while True:
      # Meminta masukan perintah
      print("Selamat datang di The Great Library")
      print("Silakan masukkan perintah!")
      order = input("Perintah Anda: ").split()

      # Apabila perintah ADD RAK valid
      if (len(order) == 4) and (order[0] == "ADD") and (order[1] == "RAK"):
        print(lib.add_rak(order[2], order[3]))
      
      # Apabila perintah ADD BUKU valid
      elif (len(order) == 9) and (order[0] == "ADD") and (order[1] == "BUKU"):
        print(lib.add_buku(order[2], order[3], order[4], order[5], order[6], order[7], order[8]))

      # Apabila perintah SEARCH valid
      elif (len(order) == 2) and (order[0] == "SEARCH"):
        print(lib.search_buku(order[1])) 

      else:
        order = " ".join(order)

        # Apabila diminta daftar buku
        if order == "LIST":
          print(lib.list_buku())

        elif order == "EXIT":
          print("Selesai, Sistem dimatikan\n") 
          break # Keluar dari program
        elif (order[:7] == "ADD RAK") or (order[:8] == "ADD BUKU") or (order[:6] == "SEARCH"):
          print("Perintah tidak valid\n")
        else:
          print("Perintah tidak dikenali\n")

# Menjalankan program
main()