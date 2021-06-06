FROM python:rc as builder

WORKDIR /starshit
COPY ./requirements.txt ./requirements
RUN pip install --user -r requirements && rm requirements


FROM python:rc-alpine as deploy

WORKDIR /process_order
ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local
COPY process_order.py ./

CMD [ "sh", "-c", "python process_order.py" ]