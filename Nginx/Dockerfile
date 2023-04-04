FROM nginx
RUN mkdir /etc/nginx/ssl/
COPY ./ecoprop.test.crt /etc/nginx/ssl/
COPY ./ecoprop.test.key /etc/nginx/ssl/
RUN rm /etc/nginx/conf.d/*
COPY ./my_default.conf /etc/nginx/conf.d/my_default.conf
