# TK2 - Path Calculator

### Tujuan

Program ini dapat memperkirakan path (jejak) gerakan suatu objek dengan informasi titik-titik lokasi yang objek tersebut lalui.

### Requirements

IDE untuk Octave. Bisa diunduh di octave.org

### Petunjuk

1. Daftarkan titik-titik lokasi yang diketahui dilewati suatu objek pada bidang datar

2. Simpan koordinat x setiap lokasi pada list X. Contoh: untuk titik (2,4), (3,-5) maka X=[2,3]

3. Simpan koordinat y setiap lokasi pada list Y. Contoh: untuk titik (2,4), (3,-5) maka Y=[4,-5]

4. Tentukan dot (kehalusan) dari gerak objek. Apabila objek bergerak patah-patah, gunakan nilai dot yang kecil. Apabila objek bergerak secara luwes, gunakan nilai dot yang besar. Nilai dot berupa integer positif

5. Panggil fungsi pathcalculator.m dengan parameter X,Y,dots yang sudah disiapkan. Anda akan mendapat plot perkiraan gerak objek yang Anda inginkan.

### Kontributor

Dev: Nito (https://github.com/hamonangann)

Test: Nahda (https://github.com/amalianahda), Dinda (http://github.com/dindasrg)