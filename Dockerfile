FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential

# Copy local code to the container image.
ENV APP_HOME /subu
WORKDIR $APP_HOME
COPY . .

RUN pip3 install -r requirements.txt

# Install production dependencies.
RUN pip3 install Flask gunicorn

ENTRYPOINT ["python3"]

#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 audioBook_v3:subu
#CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 audioBook_v3:subu
CMD ["emoji.py"]
