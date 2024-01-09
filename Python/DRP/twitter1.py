with open("datacrawl.txt", "r", encoding = "utf-8") as text_file:
    read_file = text_file.read().casefold()

splitter = read_file.split("\n")

netral_plus = 0
negatif_plus = 0
positif_plus = 0
takkut_plus = 0
berani_plus = 0

negatif = ["tidak", "bukan", "jangan", "belum", "nggak", "tanpa", "kurang", "tidaklah", "tak"]
positif = ["kabar baik", "kabar gembira", "alhamdulillah", "bagus", "gembira", "aman"]
takut = ["depresi", "takut", "ngeri", "aduh"]
berani = ["tenang", "santai", "ngapain takut"]
netral = ["resesi", "krisis ekonomi 2023", "resesi 2023"]

for index in splitter:
    positive_bool = any(word in index for word in positif)
    negation_bool = any(word in index for word in negatif)
    scared_bool = any(word in index for word in takut)
    brave_bool = any(word in index for word in berani)
    neutral_bool = any(word in index for word in netral)

    if (positive_bool == True):
        positif_plus += 1
    if (negation_bool == True):
        negatif_plus += 1
    if (scared_bool == True):
        takkut_plus += 1
    if (brave_bool == True):
        berani_plus += 1
    elif (neutral_bool == True):
        netral_plus += 1

print("Tidak Setuju =",negatif_plus)
print("Setuju =",positif_plus)
print("Berani =",berani_plus)
print("Takut =",takkut_plus)
print("Netral =",netral_plus)