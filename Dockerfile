FROM python:3.10.8
RUN apt update && apt install -y make
WORKDIR /home/aof/2022_adventofcode
ENV HOME=/home/aof
COPY Makefile  .
#Agregar dias
COPY day_01/ day_01/
COPY day_02/ day_02/
COPY day_03/ day_03/
COPY day_04/ day_04/
COPY day_05/ day_05/
COPY day_06/ day_06/
#Ejecucion
ENTRYPOINT [ "make" ]
CMD [ "day1" ]