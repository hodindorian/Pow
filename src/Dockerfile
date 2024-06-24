FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install streamlit matplotlib pandas scikit-learn ydata-profiling

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "home.py", "--server.address=0.0.0.0", "--server.port=8080"]
