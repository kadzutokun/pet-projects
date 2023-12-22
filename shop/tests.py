from string import ascii_letters
from random import choices
from django.test import TestCase
from django.urls import reverse
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


class ProductDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Category = models.Category.objects.create(title = 'работа')
        cls.product = models.Course.objects.create(title = 'TestProduct', price = '100', check_qty = '0', reviews_qty = '0', Category = cls.Category)
        cls.product.save()
        cls.Category.save()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.product.delete()
        
    # def setUp(self) -> None:
    #     self.product = models.Course.objects.create(title = 'TestProduct', price = '100', check_qty = '0', reviews_qty = '0', Category_id = 1)
        
    # def tearDown(self): # Удаление
    #     self.product.delete()
            
    def test_product_detail_view(self):
        response = self.client.get(
            reverse('shop:shop_item', kwargs = {"pk": self.product.pk})
            )
        self.assertEqual(response, self.product.title)

class ProductInfoViewTestCase(TestCase):    
    def test_products(self):
        response = self.client.get(reverse('shop:index'))
        courses = models.Course.objects.filter(archived = False).all()
        course_test = response.context['courses']
        for p,p_test in zip(courses, course_test):
            self.assertEqual(p.pk, p_test.pk)