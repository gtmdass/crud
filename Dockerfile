FROM python:3.10.11
WORKDIR /home/project
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
CMD python manage.py runserver