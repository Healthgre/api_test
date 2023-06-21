import requests


class TestNewJoke():
    """Создание новой шутки."""

    def __init__(self):
        None

    def test_create_new_random_joke(self):
        """Создание случчайной шутки."""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        print("Успех. Получили новую шутку.")

        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна.")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        assert name in check_info_value
        print("Угадал.")

    def test_create_new_random_categories_joke(self):
        """Создание случчайной шутки по определённую тему."""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        # print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        # print("Успех. Получили новую шутку.")
        #
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        # print(check_info)
        assert check_info ==["sport"]
        print("Категория верна.")
        check_info_value = check.get("value")
        print(check_info_value)
        # name = "Chuck"
        # assert name in check_info_value
        # print("Угадал.")


# random_joke = TestNewJoke()
# random_joke.test_create_new_random_joke()

sport_joke = TestNewJoke()
sport_joke.test_create_new_random_categories_joke()
