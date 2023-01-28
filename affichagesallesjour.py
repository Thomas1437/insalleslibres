from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv

fichier="sallesbien.csv"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

section = "all_calendars_combined971"
jour = "06"
mois = "02"
annee = "2023"
link = "http://agendas.insa-rouen.fr/2022/day.php?cal="+section+"&getdate="+annee+mois+jour
print(link)

driver.get(link)
newsalles=0
sallesdujour=[]
salleslibresdujour=[]
Du=[]
Ma=[]
Bo=[]
Lh=[]
Da=[]
autresSalles=[]
searchclassps = driver.find_elements("xpath", "//a[@class='ps']")

for el in searchclassps:
    if "Location" in el.get_attribute("nicetitle"):
        txt = el.get_attribute("nicetitle")
        txt = txt[txt.index("Location")+10:]
        txt = txt[:txt.index("\n")]
        #print(txt)
        if len(txt)>=21:
            txts=list(txt.split(","))
            for x in txts:
                if x not in sallesdujour:
                    newsalles+=1
                    sallesdujour.append(x)
        if (txt not in sallesdujour) and (len(txt)<21):
            newsalles+=1
            sallesdujour.append(txt)

print(newsalles,"salles occupees aujourd hui : ",sallesdujour)

with open(fichier, "r") as f:
    reader=csv.reader(f)
    for line in reader:
        if line[0] not in sallesdujour:
            salleslibresdujour.append(line[0])

for x in salleslibresdujour:
    if x.startswith('MA'):
            Ma.append(x)
    elif x.startswith('DU'):
            Du.append(x)
    elif x.startswith('LH'):
            Lh.append(x)
    elif x.startswith('BO'):
            Bo.append(x)
    elif x.startswith('DA'):
            Da.append(x)
    else:
        autresSalles.append(x)


Ma = list(set(Ma))
Du = list(set(Du))
Lh = list(set(Lh))
Bo = list(set(Bo))
Da = list(set(Da))
autresSalles = list(set(autresSalles))

Ma.sort()
Du.sort()
Lh.sort()
Bo.sort()
Da.sort()
autresSalles.sort()

print((len(Ma)+len(Du)+len(Lh)+len(Bo)+len(Da)+len(autresSalles)),'salles libres aujourd hui')

print(len(Ma),"salles libres a Magellan : ", Ma)
print(len(Du),"salles libres a Dumont Durville : ", Du)
print(len(Lh),"salles libres a LH : ", Lh)
print(len(Bo),"salles libres a Bougainville : ", Bo)
print(len(Da),"salles libres a Darwin : ", Da)
print(len(autresSalles),"autres salles libres : ", autresSalles)