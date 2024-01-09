# Digra Murtaza Izham
# 1313621010
from dataclasses import replace
from itertools import count

with open("C:/VSCode/Python/Belajar Python/data raya/Tugas 2/text.txt", "r", encoding='utf-8') as text:
    read = text.read().casefold()
    read = read.replace('?', '.').replace('!', '.').replace("\n", " ")
    pisah = read.split(".")

counter = 0

with open("C:/VSCode/Python/Belajar Python/data raya/Tugas 2/negatif.txt", encoding='utf-8') as text1:
    baca1 = text1.read()
    negasi = baca1.split("-")

kalimat = []
with open("C:/VSCode/Python/Belajar Python/data raya/Tugas 2/output.txt", "w", encoding='utf-8') as output:
    for i in pisah:
        negation_bool = any(word in i for word in negasi)
        if (negation_bool == True):
            counter += 1
            kalimat.append(i)
    
    print("Jumlah kalimat negatif dalam teks tersebut berjumlah", counter, "kalimat\n", file = output, end="\n")

    for i in kalimat:
        print("[", i, "]", file = output, end="\n")        
    print()