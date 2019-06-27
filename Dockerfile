FROM python:3
 ADD pythontest.py /
 RUN pip install requests
 CMD [ "python3", "./pythontest.py" ]

