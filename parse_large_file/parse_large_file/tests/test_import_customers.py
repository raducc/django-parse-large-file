import os

from django.conf import settings
from django.test import TestCase

from parse_large_file.utils import import_customers_from_file, batch_import_customers_from_file


class CustomerImportTestCase(TestCase):
    def setUp(self) -> None:
        assets_path = os.path.join(settings.PROJECT_ROOT, 'parse_large_file', 'tests', 'assets')
        self.csv_file_path = file_path = os.path.join(assets_path, 'customer_import.csv')

    def test_import_customers_from_file(self):
        from parse_large_file.models import Customer

        import_customers_from_file(self.csv_file_path)

        self.assertEqual(Customer.objects.count(), 4)

    def test_batch_import_customers_from_file(self):
        from parse_large_file.models import Customer

        batch_import_customers_from_file(self.csv_file_path)

        self.assertEqual(Customer.objects.count(), 4)
