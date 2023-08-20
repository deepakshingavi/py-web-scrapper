FROM --platform=linux/amd64  python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

# install google chrome
#ARG CHROME_VERSION="114.0.5735.90-1"
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
#RUN apt-get update -qqy --no-install-recommends && apt-get install -qqy --no-install-recommends google-chrome-stable=114.0.5735.90
# Check available versions here: https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable
ARG CHROME_VERSION="114.0.5735.90-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt-get update -qqy --no-install-recommends && apt-get install -qqy --no-install-recommends  -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

#RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
#  && apt install -y /tmp/chrome.deb \
#  && rm /tmp/chrome.deb

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget --no-check-certificate https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN dpkg -i google-chrome-stable_${CHROME_VERSION}_amd64.deb || apt -y -f install
RUN rm google-chrome-stable_${CHROME_VERSION}_amd64.deb;

# set display port to avoid crash
ENV DISPLAY=:99

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt
