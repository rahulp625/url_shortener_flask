FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python init_db.py 
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
