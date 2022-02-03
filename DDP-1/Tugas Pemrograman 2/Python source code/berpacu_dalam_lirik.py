import os, random

# Fungsi di bawah dimanfaatkan untuk memulai permainan. 
# Mengembalikan tuple (string, string, int, int, list)
#     string pemain - nama pemain yang dijamin sudah valid
#     string mode   - Game Mode yang dipilih pemain
#     int score     - skor awal pemain, mulai dari 0
#     int nyawa     - kesempatan bermain pemain, tergantung Game Mode yang dipilih
#     list lagu     - list berisi semua nama file dalam folder lagu
def start_game():
    print(""" 
  _                                      
 | |__   ___ _ __ _ __   __ _  ___ _   _ 
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝ 
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗ 
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝                             
  """)
    print("~"*50)
    pemain = input("masukkan username     : ")
    mode = ''
    score = 0
    nyawa = 0 
    lagu =  os.listdir("lagu")   

    while pemain == "null" or pemain == "":
        pemain = input("harap gunakan nama yang valid.\nmasukkan username     : ")
    while mode.lower() not in ["normal", "expert"]:
        mode = input("mode (normal/expert)  : ")    

    if mode.lower() == "normal":
        nyawa = 3
    else:
        nyawa = 1

    print("~"*50)
    print("Good Luck & Have Fun :)\n")
    return pemain, mode, score, nyawa, lagu

# Fungsi di bawah membuka file dalam folder sesuai nama file lagu yang terpilih.
# Mengembalikan sebuah list isi file {nama_file}.txt 
def generate_lagu(nama_file): 
    with open(f"lagu/{nama_file}", 'r') as lagu_terpilih:
        lirik = [line.rstrip() for line in lagu_terpilih] # Memodifikasi template supaya list tidak mengandung newline
    return lirik

# Fungsi di bawah memeriksa apakah file highscore.txt sudah ada di directory,
# serta mengembalikan file stream highscore.txt yang telah dibuka
# Parameter:
#     purpose 'read' / 'replace' - tujuan membuka file highscore.txt
# Mengembalikan file stream highscore.txt
def get_highscore_or_create(purpose): 
    hs = os.listdir()
    highscore = None
    # check if doesn't exist, then create default 
    if "highscore.txt" not in hs:
        highscore = open("highscore.txt", 'w')
        a = ["normal null 0\n", "expert null 0\n"]
        highscore.writelines(a)
    else:
        highscore = open("highscore.txt", 'r+')
        if highscore.read(1) == "": # update: checks if file exists, but empty
            a = ["normal null 0\n", "expert null 0\n"]
            highscore.writelines(a)

    # opens highscore.txt in desired mode
    if purpose == 'read': 
        highscore = open("highscore.txt", 'r')
    else: 
        highscore = open("highscore.txt", 'w')
    return highscore

""" 
TODO: 
- Implementasi program tebak-tebakan
- Implementasi perhitungan skor
- Implementasi game over saat kesempatan habis 
- Update highscore.txt saat diperlukan
- Manfaatkan ketiga fungsi yang sudah tersedia dengan sebaik-baiknya 
- Jangan lupa close file highscore.txt yang sudah dibuka!!
"""
name, modes, point, lives, song = start_game() # Memanggil fitur nama pemain dan game mode
round = 1

setlist = set()
while len(setlist) < 5: # Membuat daftar 5 lagu yang berbeda secara acak
    setlist.add(random.choice(song))

for i in setlist:
    print("Round", round)
    print("HP       :", lives)
    print("Score    :", point)
    print("~"*50)
    print("Judul lagu :", i.rsplit(".", 1)[0]) # Memisahkan tanda titik terkanan yang merupakan penanda ekstensi
    lyric = generate_lagu(i)
    k = random.randint(0, len(lyric) - 5) #Mengacak lirik lagu tanpa keluar baris
    for j in range(4):
        print(lyric[k+j]) # Menyediakan 4 baris prompt
    guess = input("Silakan menebak:\n")
    if guess.lower() == lyric[k+4].lower(): # Memeriksa kecocokan jawaban dengan Lirik Misteri
        print("Jawaban BENAR")
        point += len(lyric[k+4]) # Menambah skor karena jawaban benar
    else:
        print("Jawaban SALAH")
        lives -= 1 # Mengurangi nyawa karena jawaban salah
        print("Jawaban :", lyric[k+4]) # Memberitahu jawaban yang benar
    if (lives == 0):
        print("\nGAME OVER")
        print("Sayang sekali " + name +", anda terhenti disini")
        break # Fitur game over, untuk permainan yang berakhir karena nyawa habis
    round += 1
else: # Fitur winning, untuk permainan yang berakhir karena kelima lagu sudah ditebak
    print("\nSELAMAT!")
    print("Anda berhasil menyelesaikan permainan")
        
print("Hasil Akhir:")
print("score    :", point, "\n")

# Fitur High Score
text = get_highscore_or_create("read").readlines()
a = text[0].split()
b = text[1].split()

if modes.lower() == "normal":
    if point > int(a[2]):
        print("NEW HIGH SCORE!!!")
        print("username :", name)
        print("score    :", point)
        text = get_highscore_or_create("replace")
        print("normal", name, point, file=text)
        print(" ".join(b), file=text)
        print("Berhasil meraih highscore mode normal")
        text.close()
else:
    if point > int(b[2]):
        print("NEW HIGH SCORE!!!")
        print("username :", name)
        print("score    :", point)
        text = get_highscore_or_create("replace")
        print(" ".join(a), file=text)
        print("expert", name, point, file=text)
        print("Berhasil meraih highscore mode expert")
        text.close()
        
print(("~"*16) + " Thanks for playing " + ("~"*16))
setlist.clear()
end = input("Press any key to exit :)")