import re
import plotly.express as px
import pandas as pd
from collections import Counter



sehir_listesi = ['kahramanmaraş','hatay', 'gaziantep', 'malatya',
                 'diyarbakır', 'kilis', 'şanlıurfa', 'adıyaman', 
                 'osmaniye', 'adana','elazığ','maraş']
for i in range (len(sehir_listesi)):
    sehir_listesi[i] = sehir_listesi[i].capitalize()
    
boyut = ((len(sehir_listesi))-1, 4) 
sehir_verileri = [[""] * boyut[1] for _ in range(boyut[0])]
tweet_verileri = []

def sehir_sayilarini_bul(tweetler, sehir_listesi):
    birlestirilmis_metin = (' '.join(tweetler)).lower()
    sehirler = re.findall(
        r'\b(?:{})\b'
        .format('|'
                .join(sehir_listesi)
                ), birlestirilmis_metin, 
        flags=re.IGNORECASE)
    sehir_sayilari = Counter(sehirler)
    
    tweet_verileri = Counter(sehirler)
    
    for i in range (len(sehir_listesi)-1):
            if(sehir_listesi[i] == 'maraş'):
                sehir_verileri[0][0] = sehir_listesi[0]
                sehir_verileri[0][1] = tweet_verileri[sehir_listesi[i].lower()]
            sehir_verileri[i][0] = sehir_listesi[i]
            sehir_verileri[i][1] = tweet_verileri[sehir_listesi[i].lower()]
    
    print(sehir_verileri)
    
    return sehir_sayilari


depremtweetleri = pd.read_excel("deprem_tweetleri/yardim_isteyen_tweetler_0104_10Subat.xlsx")
depremtweetleri.columns = ['Sıra', 'Tarih', 'İçerik', 'Kullanıcı', 'Tweet Adresi']
depremtweetleri = depremtweetleri.drop(columns=['Sıra']) # excelde ki numaralandırma silindi

veri_excel = pd.read_excel("enlem_boylam.xlsx")
veri_excel.columns = ['Sıra', 'İl_Adı', 'Enlem', 'Boylam']
veri_excel = veri_excel.drop(columns=['Sıra']) # excelde ki numaralandırma silindi



# for i in range(len(veri_excel)):
#     if(veri_excel['İl_Adı'][i] in sehir_listesi):
#         sehir_verileri[i][3] = veri_excel['Enlem'][i]
#         sehir_verileri[i][4] = veri_excel['Boylam'][i]


sehir_verileri[0][2] = 37.58
sehir_verileri[0][3] = 36.93
sehir_verileri[1][2] = 36.40
sehir_verileri[1][3] = 36.34
sehir_verileri[2][2] = 37.06
sehir_verileri[2][3] = 37.38
sehir_verileri[3][2] = 38.35
sehir_verileri[3][3] = 38.30
sehir_verileri[4][2] = 37.91
sehir_verileri[4][3] = 40.23
sehir_verileri[5][2] = 36.71
sehir_verileri[5][3] = 37.12
sehir_verileri[6][2] = 37.15
sehir_verileri[6][3] = 38.79
sehir_verileri[7][2] = 37.76
sehir_verileri[7][3] = 38.27
sehir_verileri[8][2] = 37.21
sehir_verileri[8][3] = 36.17
sehir_verileri[9][2] = 37
sehir_verileri[9][3] = 35.32
sehir_verileri[10][2] = 38.68
sehir_verileri[10][3] = 39.22


fetchedTweets = []

for i in range (len(depremtweetleri['İçerik'])):
    fetchedTweets.append(depremtweetleri['İçerik'].astype('str')[i])



sehir_sayilari = sehir_sayilarini_bul(fetchedTweets, sehir_listesi)


for sehir, sayi in sehir_sayilari.items():
    print(f"{sehir}: {sayi}")

sehir_verileri_dataframe = pd.DataFrame(sehir_verileri, columns=["İl_Adı","Tweet_Sayısı","Enlem","Boylam"])

# HARİTA YANSITMA KISMI

print('getting data')
df = sehir_verileri_dataframe

fig = px.scatter_mapbox(df,
                        lon = df['Boylam'],
                        lat = df['Enlem'],
                        zoom = 8,
                        color = df['Tweet_Sayısı'],
                        width = 900,
                        height = 600,
                        title = 'Tweet_Map')

fig.update_layout(mapbox_style = "open-street-map")
fig.update_layout(margin = {"r":0,"t":50, "l":0,"b":10})
fig.show()

print('plot complete.')
