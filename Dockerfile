FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv pip install --system --no-deps -r <(uv pip compile --no-emit-index-url --no-emit-find-links pyproject.toml)

COPY . .

RUN python src/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000"] 