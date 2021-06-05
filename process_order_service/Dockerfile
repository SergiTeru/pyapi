FROM python:rc as builder

WORKDIR /starshit
COPY ./requirements.txt ./requirements
RUN pip install --user -r requirements && rm requirements


FROM python:rc-alpine as deploy

WORKDIR /starshit
ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local
COPY ./main.py ./main.py

CMD [ "sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080" ]