- Setup Git & [Cloud Source Repository](https://console.cloud.google.com/marketplace/details/google-cloud-platform/cloud-source-repositories)

- Create Trigger for Git Pushes to:
    - Build Project's Container Image
    - Deploy Project
    - Add Service Account Permissions for Triggers to do Build/Deploy via Repo

- Create a `cloudbuild.yaml` to:
    - Improve build speed via `caching`

- Setup Django Staticfiles via Google Cloud Storage and `django-storages`

- Map a custom domain to a Cloud Run Service

- Implement Sendgrid to have transactional emails in our project

- Build pre-push (or build) end-to-end tests in Django to ensure valid deploys

- Review the [Django Deployment Checklist](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/)

- Knative on Kubernetes -> Cloud Run <- App Engine

- @justinmitchel @joincfe
