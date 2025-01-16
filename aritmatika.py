#Operasi aritmatika

a = 10
b = 5

hasil = a + b
data = input ("Hasil penjumlahan =")
print(a,'+',b,'=',hasil)

hasil = a - b
data = input ("Hasil pengurangan =")
print(a,'-',b,'=',hasil)

hasil = a * b
data = input ("Hasil perkalian =")
print(a,'+*',b,'=',hasil)

hasil = a / b
data = input ("Hasil pembagian =")
print(a,'/',b,'=',hasil)

hasil = a ** b   # eksponen(pangkat)
data = input ("Hasil eksponen =")
print(a,'**',b,'=',hasil)

hasil = a % b    # modulus(sisa pembagian)
data = input ("Hasil modulus =")
print(a,'%',b,'=',hasil)

hasil = a // b   # floor division
data = input ("Hasil Floor division =")
print(a,'//',b,'=',hasil)

print("----------------------------------")

v = 4
w = 2    # prioritas operasi, 1.(), eksponen **, perkalian * 
x = 3                         

hasil = v ** w * x - w + x / w // v % x
print(v,'**',w,'*',x,'-',w,'+',x,'/',w,'//',v,'%',x,'=',hasil)



