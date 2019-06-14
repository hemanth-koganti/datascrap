# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3

# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
#WORKDIR /home/hemanth/Downloads/indeed

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt

#VOLUME ~/Downloads/indeed/vol

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

# Run the crawler when the container launches.

ENTRYPOINT ["python3","./go-spider.py"]
#CMD [ "python3", "./go-spider.py" ]
#CMD "python3 ./go-spider.py"
#CMD python3 ./go-spider.py -t $ENV1

