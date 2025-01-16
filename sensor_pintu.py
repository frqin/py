# Program Sensor Pintu Otomatis

while True:
    # Input jarak dari sensor (dalam meter)
    jarak = float(input("Masukkan jarak orang dari pintu (dalam meter): "))
    
    # Kondisi pintu berdasarkan jarak
    if jarak <= 4 and jarak >= 2:
        print("Pintu terbuka.")
    elif jarak > 4 or jarak < 2:
        print("Pintu tertutup.")
    else:
        print("Tidak ada perubahan pada pintu.")
    
    # Tanya apakah ingin melanjutkan
    lanjut = input("Apakah ingin melanjutkan simulasi? (y/t): ").lower()
    if lanjut != "ya":
        print("Simulasi selesai.")
        break
