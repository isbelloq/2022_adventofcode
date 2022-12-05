FROM python:3.10.8
RUN apt update && apt install -y make
WORKDIR /home/aof/2022_adventofcode
ENV HOME=/home/aof
COPY Makefile  .
#Agregar dias
COPY day_01/ day_01/
#Ejecucion
ENTRYPOINT [ "make" ]
CMD [ "day1" ]