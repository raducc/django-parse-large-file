from .celery import app


@app.task
def import_file():
    from parse_large_file.utils import import_customers_from_file

    import_customers_from_file('large_file.csv')
