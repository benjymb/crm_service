from django.test import TestCase, SimpleTestCase
from crm_app.serializers import CustomerSerializer
from crm_app.models import Customer
from crm_app.exceptions import InvalidParameters, NotFound, ImageHandlingError
from model_bakery.recipe import Recipe
from datetime import date, datetime
import uuid
from .constants import TEST_IMAGE
from crm_app.image_handling import process_image
from django.core.files.base import ContentFile

class ImageHandlingTestCase(SimpleTestCase):

    def test_that_an_image_gets_handled_correctly(self):
        b64_image = TEST_IMAGE
        image = process_image(b64_image, 'file1')
        self.assertEqual(type(image), ContentFile)

    def test_that_an_exception_is_raised_when_image_is_corrupted(self):
        with self.assertRaises(ImageHandlingError):
            b64_image = 'erds' + TEST_IMAGE + 'ef3ss$ED'
            process_image(b64_image, 'file1')
