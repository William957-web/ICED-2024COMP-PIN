FROM python:3.9
RUN pip3 install --upgrade pip
RUN pip3 install flask
WORKDIR /app
COPY . /app
RUN rm /app/Dockerfile
ENTRYPOINT [ "python3" ]
CMD ["render.py" ]
