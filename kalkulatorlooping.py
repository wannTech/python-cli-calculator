while True:
 x = input("masuk atau keluar : m / k : ")
 if x == "k":
       print("program selesai")
       break
 elif x != "m":
     print("pilihan tidak valid")
     continue

 try:
   angka1 = float(input("masukan angka pertama: "))
   operator = input("masukan operator: +,-,*,/: ")   
   angka2 = float(input("masukan angka kedua: "))

   if operator == "+":
        print(angka1 + angka2)
   elif operator == "-":
        print(angka1 - angka2)
   elif operator == "*":
        print(angka1 * angka2)
   elif operator == "/":
        if angka2 != 0:
            print(angka1 / angka2)
        else:
            print("tidak bisa dibagi 0 ")

    
   else:
       print("angka dan operator yang benar! ")
   print("-------------------")

 except ValueError:
    print("input harus nerupa angka ")