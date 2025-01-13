FROM python:3.9
RUN apt update && apt install -y ruby && rm -rf /root/.cache/apt
RUN gem install lolcat
RUN pip install dinosay && rm -rf /root/.cache/pip
COPY motd2 /etc/motd
CMD ["sh", "-c", "dinosay -r \"$(cat /etc/motd)\" | lolcat"]