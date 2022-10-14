import datetime
import random
import string

import progressbar as progressbar
import unicodecsv as unicodecsv

from django.core.files.storage import default_storage
from django.core.management import BaseCommand


def pbar(iterable, **kwargs):
    widgets = [
        progressbar.Bar('>'),
        ' ',
        progressbar.SimpleProgress(),
        ' - ',
        progressbar.Percentage(),
        ' - ',
        progressbar.ETA(),
        ' / Rate: ',
        progressbar.FileTransferSpeed(unit=' items'),
        ' ',
        progressbar.ReverseBar('<'),
    ]
    progress_bar = progressbar.ProgressBar(widgets=widgets, **kwargs)

    return progress_bar(iterable)


class RandomGenerator:
    @classmethod
    def get_email(cls):
        alphabet = string.ascii_lowercase + string.digits
        length = random.randint(4, 20)
        base_email = cls.get_random_text(alphabet, length)
        return f"{base_email}@gmail.com"

    def get_username(self):
        pass

    @staticmethod
    def get_date():
        base_date = datetime.date(2020, 1, 1)
        add_days = random.randint(0, 500)
        return base_date + datetime.timedelta(days=add_days)

    @staticmethod
    def get_random_text(alphabet, length):
        return "".join(random.choice(alphabet) for _ in range(length))


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--lines", default=1000000, type=int)

    def handle(self, *args, **options):
        csv_file = default_storage.open('large_file.csv', 'wb')
        csv_file_writer = unicodecsv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_ALL
        )
        for _ in pbar(range(options['lines'])):
            csv_file_writer.writerow([RandomGenerator.get_date(), RandomGenerator.get_email()])

        csv_file.close()
