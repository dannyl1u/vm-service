## Runs newly added .tf files using Pub/Sub notification from Cloud Storage.

1. Setup Cloud Storage Bucket and Pub/Sub

# Replace my-bucket with your bucket name

gcloud pubsub topics create my-topic
gsutil notification create -t my-topic -f json gs://my-bucket

2. Create Cloud Function

# Replace YOUR_PROJECT_ID with your Google Cloud project ID
# Replace YOUR_PROJECT_NUMBER with the project number 

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:YOUR_PROJECT_NUMBER@cloudbuild.gserviceaccount.com" \
  --role="roles/compute.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:YOUR_PROJECT_NUMBER@cloudbuild.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
