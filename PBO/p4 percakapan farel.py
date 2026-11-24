print(" SIMULASI COD HANDPHONE")
print("Kevin : Halo, selamat sore.")
print("Farel : Halo, selamat sore. Ada yang bisa dibantu?")
print("Kevin : Saya melihat iklan HP yang anda jual.")
print("Farel : Oh iya, benar. HP-nya masih tersedia.")
print("Kevin : Perkenalkan, nama saya Kevin.")
print("Farel : Salam kenal, saya Farel.")
print("Kevin : Saya tertarik dengan HP yang anda jual.")
print("Farel : Baik, silakan kalau ada yang ingin ditanyakan.")
print("Kevin : HP yang anda jual merek dan tipe apa?")
print("Farel : Samsung Galaxy A15.")
print("Kevin : RAM dan memorinya berapa?")
print("Farel : RAM 8 GB dan memori internal 128 GB.")
print("Kevin : Kondisinya masih bagus?")
kondisi_hp = "bagus"
if kondisi_hp == "bagus":
    print("Farel : Kondisinya masih bagus dan semua fungsi normal.")
elif kondisi_hp == "rusak":
    print("Farel : Ada beberapa bagian yang mengalami kerusakan.")
else:
    print("Farel : Kondisi HP cukup baik, tetapi ada bekas pemakaian.")
print("Kevin : Apakah layarnya masih original?")
print("Farel : Iya, belum pernah diganti.")
print("Kevin : Kalau baterainya bagaimana?")
print("Farel : Masih normal dan bisa digunakan dengan baik.")
print("Kevin : Kelengkapannya masih lengkap?")
print("Farel : Masih ada kotak, kabel charger, dan SIM ejector.")
print("Kevin : Apakah nota pembelian masih tersedia?")
kelengkapan = "lengkap"
if kelengkapan == "lengkap":
    print("Farel : Iya, semua kelengkapan masih tersedia.")
elif kelengkapan == "sebagian":
    print("Farel : Ada beberapa kelengkapan yang sudah tidak tersedia.")
else:
    print("Farel : Maaf, HP dijual hanya unit saja.")
print("Kevin : Baik, cukup jelas informasinya.")
print("Kevin : Untuk harganya berapa?")
print("Farel : Saya membuka harga Rp1.800.000.")
print("Kevin : Apakah masih bisa nego?")
print("Farel : Bisa, selama penawarannya masih masuk akal.")
print("Kevin : Bagaimana kalau saya tawar Rp1.500.000?")
harga = 1800000
penawaran = 1500000
if penawaran >= 1800000:
    print("Farel : Baik, saya setuju dengan harga tersebut.")
elif penawaran >= 1700000:
    print("Farel : Boleh, saya setuju dengan penawaran anda.")
elif penawaran >= 1600000:
    print("Farel : Bagaimana kalau kita sepakati Rp1.650.000?")
else:
    print("Farel : Maaf, penawarannya masih terlalu rendah.")
print("Farel : Saya bisa memberikan harga Rp1.650.000.")
print("Kevin : Kalau Rp1.650.000 bagaimana?")
print("Farel : Baik, saya setuju.")
print("Kevin : Oke, berarti kita sepakat Rp1.650.000.")
print("Farel : Untuk pembayarannya ingin menggunakan metode apa?")
print("1. COD")
print("2. Transfer")
print()
metode = "COD"
if metode == "COD":
    print("Kevin : Saya memilih COD supaya bisa memeriksa barang langsung.")
    print("Farel : Baik, kita bisa bertemu langsung.")
elif metode == "Transfer":
    print("Kevin : Saya akan melakukan pembayaran melalui transfer.")
    print("Farel : Baik, nanti saya berikan nomor rekening.")
else:
    print("Kevin : Saya masih mempertimbangkan metode pembayaran.")
    print("Farel : Tidak masalah, silakan dipikirkan dahulu.")
print("Kevin : Kalau untuk lokasi COD, anda biasanya di mana?")
print("Farel : Saya biasanya COD di sekitar pusat kota.")
print("Kevin : Bagaimana kalau di minimarket dekat jalan utama?")
lokasi = "setuju"
if lokasi == "setuju":
    print("Farel : Boleh, lokasi tersebut cukup strategis.")
    print("Kevin : Baik, saya akan datang ke sana.")
elif lokasi == "tidak":
    print("Farel : Kalau begitu, kita cari lokasi lain.")
    print("Kevin : Baik, silakan tentukan tempat yang nyaman.")
else:
    print("Farel : Kita bisa membicarakan lokasi yang paling cocok.")
print("Farel : Kapan anda bisa melakukan COD?")
print("Kevin : Besok sore sekitar jam empat.")
waktu = "tersedia"
if waktu == "tersedia":
    print("Farel : Besok jam empat saya bisa.")
    print("Kevin : Baik, sampai bertemu besok.")
elif waktu == "sibuk":
    print("Farel : Maaf, besok saya ada kesibukan.")
    print("Kevin : Kalau begitu, bagaimana kalau lusa?")
else:
    print("Farel : Saya belum bisa memastikan waktunya.")
    print("Kevin : Baik, kabari saya kalau sudah pasti.")
print()
print(" HARI COD")
print("Kevin : Halo Farel, saya sudah sampai di lokasi.")
print("Farel : Baik, saya juga sedang menuju ke sana.")
print("Kevin : Saya memakai jaket hitam.")
print("Farel : Oke, saya sudah melihat anda.")
print("Kevin : Wah, akhirnya bertemu juga.")
print("Farel : Iya, salam kenal secara langsung.")
print("Kevin : Baik, boleh saya melihat HP-nya?")
print("Farel : Tentu, silakan diperiksa terlebih dahulu.")
print("Kevin : Saya mau mengecek kondisi layar, kamera, dan speaker.")
print("Farel : Silakan, tidak perlu terburu-buru.")
print("Kevin : Saya juga ingin mencoba kartu SIM.")
print("Farel : Boleh, semua fitur bisa anda periksa.")
pengecekan = "normal"
if pengecekan == "normal":
    print("Kevin : Setelah saya periksa, semuanya masih normal.")
    print("Farel : Syukurlah kalau kondisinya sesuai.")
    print("Kevin : Iya, HP-nya masih bagus.")
elif pengecekan == "bermasalah":
    print("Kevin : Sepertinya ada masalah pada salah satu bagian.")
    print("Farel : Bagian mana yang bermasalah?")
    print("Kevin : Saya ingin memeriksanya kembali.")
else:
    print("Kevin : Saya masih belum yakin dengan kondisi HP-nya.")
    print("Farel : Tidak masalah, silakan periksa lebih teliti.")
print("Farel : Jadi, apakah anda jadi membeli HP ini?")
keputusan = "jadi"
if keputusan == "jadi":
    print("Kevin : Iya, saya jadi mengambil HP ini.")
    print("Farel : Baik, sesuai kesepakatan harganya Rp1.650.000.")
elif keputusan == "belum":
    print("Kevin : Saya masih ingin mempertimbangkannya.")
    print("Farel : Baik, tidak masalah. Silakan dipikirkan.")
else:
    print("Kevin : Maaf, saya tidak jadi membeli HP ini.")
    print("Farel : Tidak masalah, terima kasih sudah datang.")
print("Kevin : Ini uang pembayaran sesuai kesepakatan.")
print("Farel : Baik, saya hitung terlebih dahulu.")
pembayaran = 1650000
if pembayaran == 1650000:
    print("Farel : Uangnya sudah sesuai, terima kasih.")
    print("Kevin : Sama-sama. HP-nya saya bawa sekarang.")
elif pembayaran > 1650000:
    print("Farel : Sepertinya uangnya lebih, saya kembalikan sisanya.")
    print("Kevin : Baik, terima kasih.")
else:
    print("Farel : Sepertinya uangnya masih kurang.")
    print("Kevin : Baik, saya tambahkan kekurangannya.")
print("Kevin : Terima kasih, Farel. Pelayanannya cukup baik.")
print("Farel : Sama-sama, Kevin. Terima kasih sudah membeli.")
print("Kevin : Semoga nanti bisa bertransaksi lagi.")
print("Farel : Tentu, semoga HP-nya awet dan tidak ada masalah.")
print("Kevin : Amin, saya pamit dulu.")
print("Farel : Baik, hati-hati di jalan.")