def SearchWord(file):
    ctr1 =0
    ctr2 =0
    ctr3 =0

    for i in pisah:
        if (i == "Dan" or i == "dan" or i == "&"):
            ctr1+=1

        elif (i == "guna" or i == "guna." or i == "Guna"):
            ctr2+=1
        
        elif (i == "salah" or i == "Salah" or i=="salah."):
            ctr3+=1

    print ("Jumlah kata \"dan\" yang ada di dalam file adalah: %i" % ctr1)
    print ("Jumlah kata \"guna\" yang ada di dalam file adalah: %i" % ctr2)
    print ("Jumlah kata \"salah\" yang ada di dalam file adalah: %i" % ctr3)

def NegativeWord(file):
    ctr = 0
    t = open("negatif.txt", "r")
    baca1 = t.read()
    pisah1 = baca1.split()
    for i in pisah1:
        for j in pisah:
            if (j == i):
                ctr+=1
    
    print("Jumlah gabungan kata negatif yang ada di dalam file adalah: %i" %ctr)

f = open("text.txt", "r")
baca = f.read()
pisah = baca.split()
SearchWord(f)
NegativeWord(f)