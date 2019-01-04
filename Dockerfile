FROM joyzoursky/python-chromedriver:2.7-selenium
RUN apt-get update && apt-get -y install cron
RUN pip install configobj

RUN mkdir /etc/cron.h
ADD crontab /etc/cron.h/passaporto
RUN chmod 0644 /etc/cron.h/passaporto \
    && crontab /etc/cron.h/passaporto \
    && touch /var/log/cron.log

WORKDIR /usr/workspace
VOLUME /usr/workspace

CMD cron && tail -f /var/log/cron.log