import os

from django.conf import settings
from django.test import TestCase

from parse_large_file.utils import import_customers_from_file


class CustomerImportTestCase(TestCase):
    def test_import_customers_from_file(self):
        from parse_large_file.models import Customer

        assets_path = os.path.join(settings.PROJECT_ROOT, 'parse_large_file', 'tests', 'assets')
        file_path = os.path.join(assets_path, 'customer_import.csv')
        import_customers_from_file(file_path)

        self.assertEqual(Customer.objects.count(), 4)
