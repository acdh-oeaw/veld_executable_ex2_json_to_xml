FROM python:3.10
RUN useradd -u 1000 docker_user
USER docker_user

