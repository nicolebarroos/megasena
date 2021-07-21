import time
from selenium import webdriver
from bs4 import BeautifulSoup

def get_results():
    driver = webdriver.Chrome()
    driver.get("http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/")
    time.sleep(15)
    dados = driver.find_element_by_id("ulDezenas")
    dados.click()
    html = dados.get_attribute("innerHTML")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("li")

    results = []
    for i in table:
        results.append(i.get_text('\n'))
    print(results)

    time.sleep(10)

    time.sleep(10)
    driver.close()

    return results
