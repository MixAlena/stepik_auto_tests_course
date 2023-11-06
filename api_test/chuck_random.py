import requests

class Test_new_joke():
    '''Создание новой шутки'''

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        '''Создание случайной шутки'''
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Yay, here your joke are")
        else:
            print("Wrong request")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Chuck отсутствует")
        check_info_create_data = check.get("created_at")
        print(check_info_create_data)
        create_year = "2020"
        if create_year in check_info_create_data:
            print("Шутка 2020 года")
        else:
            print("Новая шутка")

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()
