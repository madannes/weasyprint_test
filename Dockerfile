FROM python

WORKDIR /usr/src/app

# copy dependency info over and install them all
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy the code last to maximize caching
COPY . .