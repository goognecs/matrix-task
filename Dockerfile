FROM python:3.11-slim

WORKDIR /app

COPY minimumPath.py matrix.txt ./

CMD [ "python", "minimumPath.py" ]
