from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

fichier="sallesbien.csv"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

link = "https://cocktail.insa-rouen.fr/ics/liste_flux_ics.php#salle"
driver.get(link)

felbytag = driver.find_elements(By.TAG_NAME,'td')

for x in felbytag:
    elt=x.get_attribute('outerHTML')
    if (('MA' in elt) or ('DU' in elt) or ('LH' in elt) or ('BO' in elt) or ('DA' in elt)) and ('href' not in elt):
        salle=elt[4:-5]
        print(salle)
        with open(fichier, "a",newline='') as f:
            csv_writer=csv.writer(f)
            csv_writer.writerow(salle)


