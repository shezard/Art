FROM python:3.9-slim
# RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/root
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "app.py" ]
CMD [""]