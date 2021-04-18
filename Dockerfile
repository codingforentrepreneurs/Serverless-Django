FROM python:3.8.2-slim

ENV APP_HOME /app
WORKDIR ${APP_HOME}

COPY . ./

# Uncomment to use pipenv
# RUN pip install pip pipenv --upgrade
# RUN pipenv install --skip-lock --system --dev

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

CMD ["./scripts/entrypoint.sh"]