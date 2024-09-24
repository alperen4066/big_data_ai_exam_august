# CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info", "app.main:app"]
exec uvicorn --host 0.0.0.0 --port "${API_PORT:-8000}" --log-level info app.main:app