FROM python:3.6.6

RUN apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        gdb; \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache ipython numpy ptvsd