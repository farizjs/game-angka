import random

def tebak_angka():
    angka_rahasia = random.randint(1, 10)
    tebakan = None

    print("Tebak angka antara 1 dan 10")

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            if tebakan < angka_rahasia:
                print("Tebakan Anda terlalu rendah!")
            elif tebakan > angka_rahasia:
                print("Tebakan Anda terlalu tinggi!")
            else:
                print("Selamat! Anda benar!")
        except ValueError:
            print("Tolong masukkan angka yang valid.")

if __name__ == "__main__":
    tebak_angka()
