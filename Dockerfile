FROM python:3.8-buster
ENV pyver="3.8"

COPY test_schema.xsd /test/

RUN \
    pip install PyXB-X==1.2.6 python-dateutil==2.8.2 && \
    cd /test && \
    pyxbgen -u ./test_schema.xsd -m protocol --binding-root=generated

# Comment out to get the original crash. This copies in the patched file.
COPY fixed-datatypes.py "/usr/local/lib/python${pyver}/site-packages/pyxb/binding/datatypes.py"

COPY test.py /test/
WORKDIR /test
CMD ["python", "test.py"]
