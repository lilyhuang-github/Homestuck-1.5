FROM python:3.13

WORKDIR /homestuckNgram

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backEnd.py .
COPY conversions.py .
COPY /ngram .
COPY setup.py .

EXPOSE 80

CMD ["fastapi", "run", "backEnd.py", "--port", "80"]
# CMD ["uvicorn", "backEnd.py:app", "--host", "0.0.0.0", "--port", "80"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD ["fastapi", "dev", "backEnd.py"]
#test