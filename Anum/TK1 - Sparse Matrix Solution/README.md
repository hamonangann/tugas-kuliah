Program TK1 ini menghitung solusi sistem persamaan linear yang direpresentasikan sparse matrix
Meskipun demikian matriks biasa juga bisa dihitung dengan ini

- Extract sparse: membuat informasi tambahan untuk matriks sparse (gunakan ini sebagai input)

- Factorization: melakukan LU factorization (gunakan output dari extract sparse sebagai input)

- Forward: algoritma forward elimination untuk menyelesaikan hitungan

- Backward: algoritma backward substitution untuk menyelesaikan hitungan
