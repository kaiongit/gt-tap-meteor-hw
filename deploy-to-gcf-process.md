### Install the gCloud CLI
https://cloud.google.com/sdk/docs/install

### Run the deployment command
```
gcloud functions deploy gov-grant-disb --allow-unauthenticated --region=asia-southeast2 --entry-point=gov_grant_disb --runtime=python38 --max-instances=5 --trigger-http
```