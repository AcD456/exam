import xml.etree.ElementTree as ETree

filename = "person.xml"
try:
    tree = ETree.parse(filename)
    root = tree.getroot()
    data = []
    # Извлечение данных из XML
    person_data = {
        "firstName": root.find("firstName").text,
        "lastName": root.find("lastName").text,
        "address": {
            "streetAddress": root.find(".//streetAddress").text,
            "city": root.find(".//city").text,
            "postalCode": root.find(".//postalCode").text,
        },
        "phoneNumbers": [phone.text for phone in root.findall(".//phoneNumber")]
    }
    print(person_data)
except FileNotFoundError:
    print("Файл не найден")
except ETree.ParseError:
    print(f"Ошибка чтения XML файла {filename}.")
except Exception as e:
    print(f"Ошибка: {e}")
