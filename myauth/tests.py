import json
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse('myauth:cookie-get')) # // Для выполнения GET запроса
        self.assertContains(response, 'Cookie value') # assertContains - вывод



class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse('myauth:foo-bar'))
        self.assertEqual(response.status_code, 200) # Проверка статус кода - 200 (успешно)
        self.assertEqual(
            response.headers['content-type'], 'application/json', # Проверка, что это json

        )
        expected_data = {'foo': 'bar', 'spam' : 'eggs'} # Переменная для проверка ожидаемого результата
        # received_data = json.loads(response.content) # Преобразуем результат в JSON
        # self.assertEqual(received_data, expected_data) 
        
        self.assertJSONEqual(response.content,expected_data) # Сразу преобразует в Json и проверяет