from django.test import TestCase
from crm_app.serializers import CompleteUserSerializer as UserSerializer
from crm_app.models import Customer, CustomUser
from crm_app.exceptions import InvalidParameters, NotFound, PermissionDenied
from model_bakery.recipe import Recipe
from .constants import TEST_IMAGE
from django.contrib.auth.models import Group

class UserSerializerTestCase(TestCase):

    maxDiff = None

    def setUp(self):
        self.regular_user = Recipe(
            CustomUser,
            first_name='Daenerys',
            last_name='Targeryen',
            username='dtargeryen'
        ).make()

        self.admin_groups = Group.objects.filter(name='admin_group')

        self.admin_user = Recipe(
            CustomUser,
            first_name='Jon',
            last_name='Snow',
            username='jsnow',
            groups=self.admin_groups
        ).make()

    def test_that_users_are_retrieved(self):
        expected = [
            {
                'id': str(self.regular_user.pk),
                'username': self.regular_user.username,
                'first_name': self.regular_user.first_name, 'last_name': self.regular_user.last_name, 
                'groups': []

            },
            {
                'id': str(self.admin_user.pk),
                'username': self.admin_user.username,
                'first_name': self.admin_user.first_name, 'last_name': self.admin_user.last_name, 
                'groups': [
                    {
                        'name': self.admin_groups[0].name
                    }
                ]

            }
        ]
        self.assertEqual(
            UserSerializer.get_users(self.admin_user), expected
        )

        with self.assertRaises(PermissionDenied):
            UserSerializer.get_users(self.regular_user)



    def test_that_users_are_created(self):
        user_information = [
            {
                'id': str(self.regular_user.pk),
                'username': self.regular_user.username,
                'first_name': self.regular_user.first_name, 'last_name': self.regular_user.last_name, 
                'groups': []

            },
            {
                'id': str(self.admin_user.pk),
                'username': self.admin_user.username,
                'first_name': self.admin_user.first_name, 'last_name': self.admin_user.last_name, 
                'groups': [
                    {
                        'name': self.admin_groups[0].name
                    }
                ]

            }
        ]
        self.assertEqual(
            UserSerializer.create_user(user_information, self.admin_user)
        )

        with self.assertRaises(PermissionDenied):
            UserSerializer.get_users(self.regular_user)