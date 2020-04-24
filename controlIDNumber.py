
#Turhan ÇETİN(2018123047)#
#İsmail IŞIK(2018123037)#



import re

dosya = open("tckimliknolar.txt")


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8]
tek = 0
cift = 0
toplam = 0
gecerliSayac = 0

def ilkBasamakKontrol(list):#ilk basamağın 0 olmaması gerektiği için txtden aldığımız tclerin ilk basamağını burda karşılaştırdık#
    if list[0] != 0:
        return True
    else:
        return False

def controlLength(list):#burada array(liste) özelliği kullanarak len metodu ile uzunluğunu karşılaştırdık#
    if len(list) == 11:
        return True
    else:
        return False


def controlIDNum(list, tek, cift,toplam):#burayı ana baseimiz gibi düşüne biliriz şartları kontrol etmemizi sağlayan fonksiyonların birbirleri ile çalışıp bütün şartları sağlaması sonucunda true çeviren bir fonksiyon oluşturduk#
    if ilkBasamakKontrol(list) == True:
        if controlLength(list) == True:
            for eleman in liste:
                if eleman % 2 == 0:
                    tek = tek + list[eleman]
                else:
                    cift = cift + list[eleman]
            if basamakOnKontrol(list, tek, cift, toplam) == True:
                if basamakOnbirKontrol(list, toplam) == True:
                    return True
        else:
            print("Gecersiz TC Kimlik Numarası (TC Kimlik No 11 haneli olmalıdır.)")
            return False
    else:
        print("Gecersiz TC Kimlik Numarası  (İlk basamak sifir olamaz)")
        return False


def basamakOnKontrol(list, tek, cift,toplam):# burada tek basamakların ve çift basamakların arasındaki algoritmanın verilen txtde dosyasındaki tclerin karışılayıp karşılamadığına baktık#
    sonuc = ((tek * 7) - cift) % 10
    if sonuc == list[9]:
        return True
    else:
        print("Geçersiz TC Kimlik Numarası (Onuncu basamak şartı sağlamıyor)")
        return False

def basamakOnbirKontrol(list,toplam):#burada ilk 10 basamağın 10a bölümünden kalannın tcnin 10. basamağa eşit olup olmadığına baktık#
    for x in range(0, 10):
        toplam = toplam + list[x]
    if toplam % 10 == list[10]:
        print("Geçerli TC Kimlik Numarası")
        return True
    else:
        print("Gecersiz TC Kimlik Numarası (Onbirinci basamak sarti saglamiyor)")
        return False


for line in dosya:#burada ise aldığımız tclerin array(liste) haline getirdiğimiz kodlar ve burda direk 11 elemanlı olan syaıları düzenli ifadelerle alarak 10 basamaklılar tcye uymadığı için almadık verilen txtde geçerli olnalrın sayısı isteniyordu#
    line = re.findall("(\d{11})", line)
    for word in line:
        if word != []:
            number = str(word)
            tcNo = list(number)
            map_object = map(int, tcNo)
            tcNo = list(map_object)
            print(word)
            if controlIDNum(tcNo, tek, cift, toplam) == True:
                gecerliSayac += 1
print("gecerli tc no sayisi : ", gecerliSayac)





