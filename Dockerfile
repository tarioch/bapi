FROM python:3.6

RUN apt-get update \
	&& apt-get install -y openjdk-8-jre-headless \
        && pip install bapi \
        && pip install tabula-py \
        && useradd -d /data -g root appuser -u 911

USER appuser

CMD ["bapi", "--host", "0.0.0.0", "--repo", "/data/repo", "main.beancount"]
