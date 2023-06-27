
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://playwright.dev/")
    elemento = pagina.locator('xpath=//span[@class="DocSearch-Button-Placeholder"]')
    elemento.click()
    
    if elemento.is_visible():
        print("O elemento está presente na página.")
    else:
        print("O elemento não está presente na página.")
    
    time.sleep(5)
