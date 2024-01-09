# Replikasi Paper Analisis Sentimen Tweet Pemindahan Ibukota
## Kelompok 3
### Nama Anggota
1. Riky Dermawan - 1313621009
2. Digra Murtaza Izham - 1313621010
3. Rasyaad Maulana Khandiyas - 1313621020
4. Muhammad Ramadhan Putra Pratama - 1313621038
5. Narendra Arkan Putra Darmawan - 1313621043

### Before used this code, please install library
    pip install regex
    pip install sastrawi
    pip install textblob
    pip install clean-text

### File yang digunakan
    Crawling :
    - coding : scraping.bat
    - hasil : txt files/tweets.jsonl

    Scraping :
    - coding : scraping.py
    - hasil : txt files/tweets.txt

    Preprocessing :
    - coding : preproc.py
    - hasil : txt files/preprocessed tweet.txt

    Labelling untuk Data Training :
    - coding : labelling.py
    - hasil : 
    40 Train/traininglist.txt
    60 Train/traininglist.txt
    80 Train/traininglist.txt
    120 Train/traininglist.txt

    Term Frequency :
    coding : termfreq.py
    hasil : tf result.txt

    Pengujian Model 40:80 :
    - coding : trainingtest1.py
    - hasil : For PPT/accurary1.txt

    Pengujian Model 60:60 :
    - coding : trainingtest2.py
    - hasil : For PPT/accurary2.txt

    Pengujian Model 80:40 :
    - coding : trainingtest3.py
    - hasil : For PPT/accurary3.txt