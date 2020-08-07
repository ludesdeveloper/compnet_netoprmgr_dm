FROM python:3.8
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /usr/local/lib/python3.8/site-packages/netoprmgr_dm
WORKDIR /usr/local/lib/python3.8/site-packages/netoprmgr_dm
CMD ["python","__main__.py"]
