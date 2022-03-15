import csv
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=capa)
driver1 = webdriver.Chrome(desired_capabilities=capa)
wait = WebDriverWait(driver, 20)
wait1 = WebDriverWait(driver1, 20)


# aller sur la page d'accueil
# Step 02
base_url = "https://shop.palaceskateboards.com/"
driver.get(base_url)
# Step 02

# attendre le chargement
try:
    wait.until(EC.visibility_of_all_elements_located(
        (By.ID, "product-loop"))
    )
except (TimeoutException):
    sys.exit("Error message - loading page")

# ouvrir csv
with open('palace_items.csv', 'w') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=' ',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # ouvrir toutes les pages produits
    # Step 03
    products = driver.find_elements(
        By.CLASS_NAME, "product-grid-item clearfix")
    # Step 03
    i = 1
    for product in products:

        # creer tableau
        csv_row = []

        # aller sur la page produit
        url_product = product.find_element(By.CSS_SELECTOR,
                                           "a").get_attribute('href')
        csv_row.append(url_product)
        print(i)
        print(url_product)
        i = i + 1

        driver1.get(url_product)
        wait1.until(EC.visibility_of_all_elements_located(
            (By.ID, "content"))
        )

        # PRENDRE LES INFORMATIONS

        # disponibilite
        try:
            # step 04
            driver1.find_element(By.CSS_SELECTOR,
                                 "add cart-btn clearfix")
            # step 04

            print("Product " + url_product + " is available")
            product_availability = "Available"
            csv_row.append(product_availability)

        except(NoSuchElementException):
            print("Product " + url_product + " is sold out")
            product_availability = "Sold out"
            csv_row.append(product_availability)

        # nom
        try:
            # step 05
            product_name = driver1.find_element(By.CSS_SELECTOR,
                                                "title").text
            # step 05
            csv_row.append(product_name)
        except (NoSuchElementException):
            print("Element from " + url_product + " has no name")
        finally:
            pass

        # prix
        try:
            # step 06
            product_price = driver1.find_element(By.CSS_SELECTOR,
                                                 "prod-price").text
            # step 06
            csv_row.append(product_price)
        except (NoSuchElementException):
            print("Element from " + url_product + " has no price")
        finally:
            pass

        # image
        try:
            # step 07
            product_picture = driver1.find_element(By.CSS_SELECTOR,
                                                   "img is-selected").get_attribute('src')
            # step 07
            csv_row.append(product_picture)
        except (NoSuchElementException):
            print("Element from " + url_product + " has no picture")
        finally:
            pass

        # copier dans le csv
        try:
            cwriter.writerow(csv_row)
            print("Row written")

        except(WebDriverException):
            print("Error message - csv")

        finally:
            pass

# fermer les navigateurs
print("Tout est bien la, chef !")
driver.close()
driver1.close()
