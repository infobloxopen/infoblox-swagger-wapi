FROM tutum/apache-php

#RUN apt-get update

MAINTAINER "Vedant Sethia <vsethia@infoblox.com"

RUN apt-get install python3

ADD swagger-ui /var/www/html/swagger-ui
ADD index.php /var/www/html/index.php

#RUN chmod +x /var/www/html/swagger-ui/dist/script.sh
#RUN systemctl restart apache2

EXPOSE 80