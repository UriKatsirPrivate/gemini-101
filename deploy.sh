# https://cloud.google.com/sdk/gcloud/reference/run/deploy
export GOOGLE_CLOUD_PROJECT=landing-zone-demo-341118
gcloud config set project $GOOGLE_CLOUD_PROJECT
export SERVICE_NAME=gemini101
export ARTIFACT_REGISTRY_NAME=gemini101
export REGION=me-west1
export SERVICE_ACCOUNT_EMAIL=gemini-basic@landing-zone-demo-341118.iam.gserviceaccount.com

# Enable APIs
gcloud services enable cloudbuild.googleapis.com --project $GOOGLE_CLOUD_PROJECT
gcloud services enable artifactregistry.googleapis.com --project $GOOGLE_CLOUD_PROJECT
gcloud services enable run.googleapis.com --project $GOOGLE_CLOUD_PROJECT --async
gcloud services enable aiplatform.googleapis.com --project $GOOGLE_CLOUD_PROJECT --async

# Artifact Registry
# gcloud artifacts repositories create $ARTIFACT_REGISTRY_NAME --location=$REGION --repository-format=docker
gcloud builds submit --tag $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest

gcloud run deploy $SERVICE_NAME \
--image $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest \
--platform managed \
--allow-unauthenticated \
--region=$REGION \
--ingress=all \
--min-instances=0 \
--concurrency=20 \
--service-account=$SERVICE_ACCOUNT_EMAIL \
--execution-environment=gen2    \
--cpu-boost \
--cpu=1 \
--memory=1Gi \
# --update-env-vars PROJECT_ID="landing-zone-demo-341118" \

