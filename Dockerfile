FROM python:3.9

WORKDIR .

COPY requires.txt .
RUN pip3 install -U -r requires.txt

COPY . .

CMD [ 'python' , 'bot.py']