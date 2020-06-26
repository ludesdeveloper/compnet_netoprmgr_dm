FROM python:3.8
ADD . /usr/local/lib/python3.8/site-packages/netoprmgr_dm
ADD __main__.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD ["python","__main__.py"]
