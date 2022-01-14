FROM python:3.8-buster

COPY test_schema.xsd test.py /test/

RUN \
    pip install PyXB-X==1.2.6 python-dateutil==2.8.2 && \
    cd /test && \
    pyxbgen -u ./test_schema.xsd -m protocol --binding-root=generated

WORKDIR /test
CMD ["python", "test.py"]