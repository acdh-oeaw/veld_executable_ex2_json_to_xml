FROM python:3.6.15
RUN useradd -u 1000 docker_user
USER docker_user

