import unicodecsv


def save_customer(entry):
    from parse_large_file.models import Customer

    Customer.objects.get_or_create(
        email=entry[0],
        defaults={
            'last_seen': entry[1],
            'username': entry[2],
            'first_name': entry[3],
            'age': entry[4],
        },
    )


def import_customers_from_file(filename):
    with open(filename, 'rb') as fh:
        reader = unicodecsv.reader(fh, delimiter=',', quotechar='"')
        for line in reader:
            save_customer(line)
