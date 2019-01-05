FROM joyzoursky/python-chromedriver:2.7-selenium
RUN apt-get update && apt-get -y install cron
RUN pip install configobj && pip install selenium && pip install requests

RUN mkdir /etc/cron.h
ADD crontab /etc/cron.h/passaporto
RUN chmod 0644 /etc/cron.h/passaporto \
    && crontab /etc/cron.h/passaporto

WORKDIR /usr/workspace
VOLUME /usr/workspace

CMD ["sh", "-c", "touch /var/log/cron.log && cron && tail -f /var/log/cron.log"]