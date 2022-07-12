### Clone this repo
```bash
git clone https://github.com/kaiongit/gt-tap-meteor-hw.git
```
### Install Google's Functions Framework
```bash
pip install functions-framework
```
### Install the app's requirements
```bash
pip install --requirement requirements.txt
```
### In the file ```GlobalConstants.py```, change the variable ```GCLOUD_PROJECT_NAME``` to your own Firestore enabled Google Cloud project's name
### Run the app with Functions Framework
```bash
functions-framework --target gov_grant_disb
```
Note the ``address:port`` that Flask deployed to
### Curl the ```address:port``` that the Flask deployed to