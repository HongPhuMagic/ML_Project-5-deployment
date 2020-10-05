FROM continuumio/anaconda3
LABEL maintainer="Aaron Hong <cuong.hong.phu@hotmail.com>" \
    description="Docker image for Solar irradiance prediction model. This container contains\
    predictive model that can be accessed using a REST API (created in Flask)."
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD ["python", "app.py", "--ip='0.0.0.0'"]