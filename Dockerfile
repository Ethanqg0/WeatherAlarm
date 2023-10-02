FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN python -m venv /venv && \
    /venv/bin/pip install -r requirements.txt

# For macOS/Linux
ENV PATH="/venv/bin:$PATH"
# For Windows
ENV PATH="/venv/Scripts:$PATH"

CMD python ./app.py
