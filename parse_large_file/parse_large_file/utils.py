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


def import_customers_from_file(file_path):
    with open(file_path, 'rb') as fh:
        reader = unicodecsv.reader(fh, delimiter=',', quotechar='"')
        for line in reader:
            save_customer(line)


def batch_import_customers_from_file(file_path, batch_size=1000):
    from parse_large_file.models import Customer

    with open(file_path, 'rb') as fh:
        reader = unicodecsv.reader(fh, delimiter=',', quotechar='"')
        save_objs = []

        for step, line in enumerate(reader):
            if step % batch_size == 0 and step:
                Customer.objects.bulk_create(
                    save_objs, batch_size=batch_size, ignore_conflicts=True
                )
                save_objs = []

            save_objs.append(
                Customer(
                    email=line[0],
                    last_seen=line[1],
                    username=line[2],
                    first_name=line[3],
                    age=line[4],
                )
            )

        Customer.objects.bulk_create(save_objs, batch_size=batch_size, ignore_conflicts=True)
