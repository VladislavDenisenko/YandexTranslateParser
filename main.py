from selenium import webdriver
from bs4 import BeautifulSoup
import time



#открываем на чтение/запись файлы
print("Открываю на чтение/запись файлы")
file_input = open(r"C:\Users\vladi\PycharmProjects\YandexTranslate\vhod.txt", encoding='utf-8')
file_output = open(r"C:\Users\vladi\PycharmProjects\YandexTranslate\vihod.txt", 'w', encoding='utf-8')
print("Файлы успешно открыты")


try:
    # options
    options = webdriver.ChromeOptions()
    #отключаем web
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path=r"C:\Users\vladi\PycharmProjects\YandexTranslate\chromedriver.exe",
        options=options
    )
    print("Перехожу на сайт Яндекс.Переводчика")
    driver.get("https://translate.yandex.ru/")
    print("Успешно")
    time.sleep(2)
    counter = 1

    while True:
        #
        line = file_input.readline()

        if not line:
            print("\n"+"Все строки файла успешно переведены"+"\n"+"До новых встреч!")
            break

        if line == '\n':
            file_output.write('\n')
            continue

        # закидываем строку в переводчик
        print("_______Считываю строку № ", counter, " из файла______")
        counter += 1
        print("Отправляю строку в переводчик")
        line_input = driver.find_element_by_id("fakeArea")
        line_input.clear()
        line_input.send_keys(line)
        time.sleep(2)
        # забираем страницу
        print("Забираю html страницы")
        with open("index.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)
        #
        with open("index.html", encoding='utf-8') as file:
            src =file.read()

        # берем переведенный текст
        print("Загружаю переведенную строку в новый файл")

        soup = BeautifulSoup(src, "lxml")
        stroka = soup.find("div", class_= "translation-container").get_text()
        file_output.write(stroka+'\n')
        print("Успешно")

except Exception as ex:
    print(ex)
finally:
    file_output.close()
    file_input.close()
    driver.close()
    driver.quit()






