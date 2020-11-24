FROM webdevops/php-nginx
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
COPY ./html /app
RUN  cd /app && \
     composer update
USER www-data
