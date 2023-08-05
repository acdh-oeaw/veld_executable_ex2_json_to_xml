FROM python:3.11.4
RUN useradd -u 1000 docker_user
USER docker_user

