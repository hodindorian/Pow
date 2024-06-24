FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install streamlit matplotlib pandas scikit-learn

EXPOSE 4200

ENTRYPOINT ["streamlit", "run", "home.py", "--server.address=0.0.0.0"]
