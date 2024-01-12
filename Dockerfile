FROM python:3.11.4
RUN pip install -U prefect==2.14.10
RUN useradd -u 1000 docker_user
RUN mkdir /home/docker_user/
RUN chown docker_user:docker_user /home/docker_user
USER docker_user

