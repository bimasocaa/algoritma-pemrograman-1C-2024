# program mengonversi bilangan desimal ke biner dalam bentuk segitiga
# Input bilangan desimal dari pengguna
angka_desimal = int(input("Masukkan bilangan desimal: "))

# Konversi bilangan desimal ke biner
biner = ""
n = angka_desimal
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

#program untuk menampilkan bilangan biner
print(f"Bilangan biner dari {angka_desimal} adalah: {biner}")

# program bentuk pola segitiga biner
print("Pola segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])
