from string import ascii_letters
from random import choices
from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from . import utils
from . import models
# Create your tests here.
class AddTwoNumbersTestCase(TestCase):
    def test_add_two_number(self):
        result = utils.add_two_number(2,5)
        self.assertEquals(result,7)


class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.title = "".join(choices(ascii_letters, k = 7))
        models.Course.objects.filter(title = self.title).delete()
    def test_create_product(self):
        response = self.client.post(reverse('shop:shopCreate'), {
            'title' : self.title,
            'price': '75000',
            'check_qty': '0',
            'reviews_qty': '0',
            'Category': 'Курсовая работа'
        })
        self.assertRedirects = (response , reverse('shop:index'))
        self.assertTrue = (
            models.Category.objects.filter(title = self.title).exists()
        )
        # self.assertEqual = (response.status_code, 20)


# class ProductDetailViewTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.Category = models.Category.objects.create(title = 'работа')
#         cls.product = models.Course.objects.create(title = 'TestProduct', price = '100', check_qty = '0', reviews_qty = '0', Category = cls.Category)
#         cls.product.save()
#         cls.Category.save()
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.product.delete()
        
#     def setUp(self) -> None:
#         self.product = models.Course.objects.create(title = 'TestProduct', price = '100', check_qty = '0', reviews_qty = '0', Category_id = 1)
        
#     def tearDown(self): # Удаление
#         self.product.delete()
            
#     def test_product_detail_view(self):
#         response = self.client.get(
#             reverse('shop:shop_item', kwargs = {"pk": self.product.pk})
#             )
#         self.assertEqual(response, self.product.title)

class ProductInfoViewTestCase(TestCase):
    fixtures = [
        'course-fixtures.json',
        'Category-fixtures.json'
    ]

    def test_products(self):
        response = self.client.get(reverse('shop:index'))
        courses = models.Course.objects.filter(archived = False).all()
        course_test = response.context['courses']
        self.assertQuerySetEqual(
            qs =  models.Course.objects.filter(archived = False).all(), 
            values= (p.pk for p in response.context['courses']),
            transform= lambda p: p.pk
        )

class OrderViewTestCase(TestCase):
    fixtures = [
        'order-fixtures.json',
        'course-fixtures.json',
        'Category-fixtures.json',
        'user-fixtures.json',
        'group-fixtures.json'
    ]
    # @classmethod
    # def setUpClass(cls) -> None:
    #     #cls.dict = dict(username='TestUser', password = 'TestUser17')
    #     #cls.user = User.objects.create_user(**cls.dict)
    #     cls.user = User.objects.create_user(username = 'TestUser', password = 'TestUser17')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.user.delete
    # def setUp(self) -> None:
    #     #self.client.login(**self.dict)
    #     self.client.force_login(self.user)
    def test_detail(self):
        self.client.logout()
        order = models.Order.objects.filter(status = 'accepted').all()
        response = self.client.get(reverse('shop:order', kwargs= {'pk': 4}))
        last_path = response.request['PATH_INFO']
        print(last_path)
        self.assertEqual(response.status_code, 200)
        #print(response['location'])

class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'Category-fixtures.json',
        'course-fixtures.json'
    ]

    def test_get_product_view(self):
        response = self.client.get(
            reverse('shop:product_export'),
            )
        self.assertEqual(response.status_code, 200)

        course = models.Course.objects.order_by('pk').all()
        expected_data = [
            {
                "pk": courses.pk,
                "title": courses.title,
                "price" : courses.price
            }
            for courses in course
        ]
        products_data = response.json()
        self.assertEqual(
            products_data['products'], expected_data 
        )