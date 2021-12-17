FROM ubuntu:16.04
COPY ./a.out /opt/a.out
COPY ./flag.txt /opt/flag.txt
WORKDIR /opt
RUN apt update&&apt install -y socat&&chown root:root a.out&&chmod 775 a.out&&chown root:root flag.txt&&chmod 664 flag.txt && useradd -s /bin/bash user 
USER user
CMD socat tcp-listen:9090,fork,reuseaddr exec:/opt/a.out 
