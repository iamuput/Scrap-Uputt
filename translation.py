class Translation(object):
    START_TEXT = """<b>ππΎππΌπ πππππ di buat untuk Membantu anda Untuk Mengambil APP ID dan API Hash dengan Mudah dan AMAN!
ββββββββββββββββββββββββ
Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.
Contoh : +628xxxxxxx</b>
"""
    AFTER_RECVD_CODE_TEXT = """No HP Diterima!
Silahkan kirimkan kode yang Anda terima dari Telegram!

Kode ini hanya digunakan untuk tujuan mendapatkan ID APP dari my.telegram.org
jika Anda tidak mempercayai dev bot ini, Ngambil Manual aja
"""
    BEFORE_SUCC_LOGIN = "Kode Diterima. Scarpping Web Page..."
    ERRED_PAGE = """Hadeh Error. Coba dengan Cara Manual

Cara Ambil APP ID dan API HASH Secara Manual
1. Buka my.telegram.org/auth
2. Loginkan akun telegram kalian
3. klik menu API Development
4. isi data seperti dibawah ini :
β’ App Title : tgbot
β’ Short Name : tgbot
β’ URL : (kosongin)
β’ Platform : desktop
5. Selesai

Bila Berhasil Ambil Manual Silahkan Coba Lagi di Bot ini"""
    CANCELLED_MESG = "Bye! Silahkan /start kembali untuk mengulang"
    IN_VALID_CODE_PVDED = "Kode OTP yang anda Masukan SALAH"
    IN_VALID_PHNO_PVDED = "No HP yang anda masukan SALAH, Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.\nContoh: +628xxxxxxx"
