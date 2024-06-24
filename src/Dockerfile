FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install streamlit matplotlib pandas scikit-learn

EXPOSE 80

ENTRYPOINT ["streamlit", "run", "home.py", "--server.port=80"]
