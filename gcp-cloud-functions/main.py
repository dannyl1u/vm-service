## First Gen Cloud Function

import base64
import json
from google.cloud.devtools import cloudbuild_v1


def trigger_cloud_build(event, context):
    try:
        # Decode and parse the Pub/Sub message
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        message = json.loads(pubsub_message)
        file_path = message['name']  # The file path in the GCS bucket

        # Create a Cloud Build client instance
        client = cloudbuild_v1.services.cloud_build.CloudBuildClient()

        # Set the project ID (ensure you have the correct project ID)
        project_id = 'YOUR_PROJECT_ID'  # Replace with your actual project ID

        # Build configuration with dynamic file path
        build_config = {
            'steps': [
                {
                    'name': 'gcr.io/cloud-builders/gsutil',
                    'args': ['cp', f'gs://BUCKET_NAME/{file_path}', '.'] # Replace with your bucket name
                },
                {
                    'name': 'hashicorp/terraform',
                    'args': ['init']
                },
                {
                    'name': 'hashicorp/terraform',
                    'args': ['apply', '-auto-approve']
                }
            ],
            'timeout': '1200s'  # Adjust timeout as needed
        }

        operation = client.create_build(project_id=project_id, build=build_config)
        print("Build triggered:", operation.metadata.build.id)
    except Exception as e:
        print(f"An error occurred: {e}")  # Log any errors

