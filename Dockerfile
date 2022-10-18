FROM python:3.10.8 AS development_build


RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install poetry==1.2.2

# set work directory
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Install dependencies:
RUN poetry config virtualenvs.create false
RUN poetry run pip install -U pip && \
    poetry install --no-root --no-interaction

# copy project
COPY parse_large_file/ .