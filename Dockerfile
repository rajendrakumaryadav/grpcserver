FROM python:slim
LABEL MAINTAINER "Rajendra Kumar R Yadav"
WORKDIR /app
COPY requirements.txt .
RUN /bin/bash -c "pip install -r requirements.txt"
COPY messages.proto .
COPY proto-compile.py .
RUN /bin/bash -c "python proto-compile.py"
COPY . .
#EXPOSE 5000
RUN /bin/bash -c "chmod u+x ./entrypoint.sh"
ENTRYPOINT ["./entrypoint.sh"]