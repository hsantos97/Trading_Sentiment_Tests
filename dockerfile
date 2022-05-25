FROM python:latest
COPY ./ ./
RUN pip install -r requirements.txt
#RUN chmod +x /challange/init.sh
ENTRYPOINT [ "python" ]
CMD [ "./challange/src/main.py" ]