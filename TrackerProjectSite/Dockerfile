FROM python:latest
WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "TrackerProjectSite/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]