FROM python:rc as builder

WORKDIR /starshit
COPY ./requirements.txt ./requirements
RUN pip install --user -r requirements && rm requirements


FROM python:rc-alpine as deploy

WORKDIR /post_order
ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local
COPY post_order.py .

CMD [ "sh", "-c", "uvicorn post_order:app --host 0.0.0.0 --port 5000" ]