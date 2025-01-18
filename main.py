import xml.etree.ElementTree as ETree

filename = "person.xml"

try:
    # Парсинг XML файла
    tree = ETree.parse(filename)
    root = tree.getroot()

    # Извлечение данных из атрибутов и элементов XML
    person_data = {
        "firstName": root.attrib.get("firstName", "Не указано"),  # Получение атрибутов
        "lastName": root.attrib.get("lastName", "Не указано"),
        "address": {
            "streetAddress": root.find(".//address").attrib.get("streetAddress", "Не указано"),
            "city": root.find(".//address").attrib.get("city", "Не указано"),
            "postalCode": root.find(".//address").attrib.get("postalCode", "Не указано"),
        },
        "phoneNumbers": [phone.text.strip() for phone in root.findall(".//phoneNumber") if phone.text]
    }

    # Вывод данных
    print("------------------")
    print("Имя:", person_data["firstName"])
    print("Фамилия:", person_data["lastName"])
    print("Адрес:")
    print("---Улица:", person_data["address"]["streetAddress"])
    print("---Город:", person_data["address"]["city"])
    print("---Почтовый индекс:", person_data["address"]["postalCode"])
    print("Телефоны:")
    for phone in person_data["phoneNumbers"]:
        print("  -", phone)
    print("------------------")

except FileNotFoundError:
    print("Файл не найден.")
except ETree.ParseError:
    print(f"Ошибка чтения XML файла {filename}. Убедитесь, что файл имеет корректный формат XML.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Завершение работы программы")