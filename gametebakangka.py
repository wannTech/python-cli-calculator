import random

print("    GAME TEBAK ANGKA 1-100")


while True:
    game = input("\nMasuk ke game (m) / Keluar (k): ")
    
    if game == "k":
        print("Terima kasih sudah bermain!")
        print("Game selesai.")
        break
    elif game != "m":
        print("Masukkan huruf yang valid (m/k)")
        continue
    
    # Generate angka rahasia
    generate_angka = random.randint(1, 100)
    kesempatan = 5
    
    print("\n--- Mulai Game ---")
    print(f"Tebak angka antara 1-100")
    print(f"Kamu punya {kesempatan} kesempatan!\n")
    
    # Loop tebak angka
    while kesempatan > 0:
        try:
            tebakan = int(input("masukan tebakan :"))
        except ValueError:
            print("masukan dari 1-100 ")
            continue
        if tebakan == generate_angka:
            print ("tebakan kamu benar")
            print("angka yang kamu masukan :", tebakan, "sama dengan ", generate_angka)
            break
        if tebakan > generate_angka:
            print("angka yang kamu masukan terlalu besar ")
        else :
            print("tebakan kamu terlalu kecil ")

            kesempatan -= 1
            print("sisa kesempatan kamu :", kesempatan)

    if kesempatan == 0:
        print("kesempatan kamu habis, angka yang benar adalah :", generate_angka)



   
            
    




    


