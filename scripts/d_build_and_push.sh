# host -> gcr.io/serverless-cfe/serverless-django

docker build -t serverless-django -f Dockerfile .

docker tag serverless-django gcr.io/serverless-cfe/serverless-django

docker push gcr.io/serverless-cfe/serverless-django