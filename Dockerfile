FROM gboeing/osmnx
COPY requirements.txt /home/src/voila/requirements.txt
WORKDIR /home/src
RUN pip install -r voila/requirements.txt