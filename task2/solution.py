import csv
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")  # запуск в фоновом режиме
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')


def get_links(list_of_links: list) -> list:
    """Функция для получения ссылки на каждую букву из таблицы содержание на википедии"""
    for j in range(1, 29):
        for i in range(1, 15):
            xpath_of_link = driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/div/div[2]/ul[{j}]/li[{i}]/a')[0].get_attribute('href')  # получение ссылки через xpath
            list_of_links.append(xpath_of_link)
    return list_of_links


def scrap_animals(beasts_set: set) -> set:
    """Функция для обработки ссылок и получения животных содержащихся на странице"""
    print('Идет обработка ссылок, не завершайте программу')
    for i in links:
        driver.get(i)

        all_cards = driver.find_elements(By.XPATH, '//*[@id="mw-pages"]/div[2]/div/div/ul')  # получение содержащихся животных на странице по ссылке через xpath

        str_of_beasts = ''.join(row.text for row in all_cards)
        beasts = str_of_beasts.split('\n')
        for a in beasts:
            beasts_set.add(a)
    return beasts_set


links = []
get_links(links)

set_of_animals = set()
scrap_animals(set_of_animals)

words = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
animals = {}

for key in words:
    animals[key] = 0

for animal in set_of_animals:
    if animal[0] in words:
        animals[animal[0]] += 1


def save_to_csv(data):
    with open('beasts.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for word, count in data.items():
            writer.writerow([word, count])


save_to_csv(animals)
print('Запись завершена, проверьте файл beasts.csv')
