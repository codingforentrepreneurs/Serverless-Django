gcloud run deploy serverless-django \
--image gcr.io/serverless-cfe/serverless-django \
--platform managed \
--region us-west1 \
--allow-unauthenticated \
--project serverless-cfe \
--service-account serverless-django@serverless-cfe.iam.gserviceaccount.com