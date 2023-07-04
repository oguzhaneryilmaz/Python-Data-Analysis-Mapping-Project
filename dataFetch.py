import pandas as pd
import matplotlib as plt

depremtweetleri = pd.read_excel("deprem_tweetleri/yardim_isteyen_tweetler_0104_10Subat.xlsx")
depremtweetleri.columns = ['Sıra', 'Tarih', 'İçerik', 'Kullanıcı', 'Tweet Adresi']
depremtweetleri = depremtweetleri.drop(columns=['Sıra']) # excelde ki numaralandırma silindi

print(depremtweetleri['İçerik'])


for i in len(depremtweetleri['İçerik']):
    #Burası tweet içeriğindeki kelimelerin ayıklanacağı kısım.
   i=0
   def text_search(text, regex):
    #doğru regex tanımlamaları ile  text (çekilen tweet) içerisindeki adres verileri alınacak..
    #.. alınan veriler haritalamada kullanılan bir değeri yükseltecek..
    return []


#daha sonra for döngüsünün dışında yükseltilen değer ile haritada ki renklerde değişiklikler olacak