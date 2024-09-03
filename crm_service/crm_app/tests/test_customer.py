from django.test import TestCase
from crm_app.serializers import CustomerSerializer
from crm_app.models import Customer, CustomUser
from crm_app.exceptions import InvalidParameters, NotFound
from model_bakery.recipe import Recipe
from .constants import TEST_IMAGE

class CustomerSerializerTestCase(TestCase):

    maxDiff = None

    def setUp(self):

        self.user = Recipe(
            CustomUser,
            first_name='Daenerys',
            last_name='Targeryen',
            username='dtargeryen'
        ).make()

        self.customer = Recipe(
            Customer,
            name='John',
            surname='Snow',
            created_by=self.user
        ).make()




    def test_that_customers_are_retrieved(self):
        expected = [
            {
                'id': str(self.customer.id),
                'name': self.customer.name,
                'surname': self.customer.surname,
                'updated_by': None,
                'photo': None,
                'created_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            }
            }
        ]
        self.assertEqual(
            CustomerSerializer.get_customers(), expected
        )


    def test_that_a_customer_is_retrieved(self):
        expected = {
                'id': str(self.customer.id),
                'name': self.customer.name,
                'surname': self.customer.surname,
                'updated_by': None,
                'photo': None,
                'created_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            }
            }
        self.assertEqual(
            CustomerSerializer.get_customer(self.customer.pk), expected
        )

    def test_that_an_exception_is_raised_when_trying_to_get_a_customer(self):
        with self.assertRaises(NotFound) as cm:
            CustomerSerializer.get_customer('c' + str(self.customer.pk)[1:])

        with self.assertRaises(InvalidParameters) as cm:
            CustomerSerializer.get_customer('z' + str(self.customer.pk)[1:])

    def test_that_a_customer_is_created_correctly(self):
        new_customer_data = {
                'name': 'Arya',
                'surname': 'Stark',
            }
        new_customer = CustomerSerializer.create_customer(
            new_customer_data, self.user
        )
        db_customer = Customer.objects.get(pk=new_customer['id'])
        self.assertEqual(new_customer, {
            'id': str(db_customer.pk),
            'name': db_customer.name,
            'surname': db_customer.surname,
            'photo': None,
            'updated_by': None,
            'created_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            }
        })

    def test_that_an_image_is_correctly_saved_and_retrived(self):
        new_customer_data = {
            'name': 'Arya',
            'surname': 'Stark',
            'photo': TEST_IMAGE
        }
        new_customer = CustomerSerializer.create_customer(
            new_customer_data, self.user
        )
        db_customer = Customer.objects.get(pk=new_customer['id'])
        self.assertEqual(new_customer, {
            'id': str(db_customer.pk),
            'name': db_customer.name,
            'surname': db_customer.surname,
            'photo': db_customer.photo.url,
            'updated_by': None,
            'created_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            }
        })

    def test_that_a_customer_is_updated_correctly(self):
        customer_data = {
                'name': 'Arya',
                'surname': 'Stark',
            }
        new_customer = CustomerSerializer.update_customer(
            customer_data, self.customer.id, self.user
        )
        db_customer = Customer.objects.get(pk=new_customer['id'])
        self.assertEqual(new_customer, {
            'id': str(db_customer.pk),
            'name': db_customer.name,
            'surname': db_customer.surname,
            'photo': None,
            'updated_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            },
            'created_by': {
                'id': str(self.user.pk),
                'username': self.user.username
            }
        })


    def test_that_a_customer_is_deleted_correctly(self):
        CustomerSerializer.delete_customer(
            self.customer.id
        )
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(pk=self.customer.id)
