# Government Grant Disbursement API
> Made for GovTech METEOR's technical assessment.

Try the API at [https://asia-southeast2-nomadic-thinker-355706.cloudfunctions.net/gov-grant-disb](https://asia-southeast2-nomadic-thinker-355706.cloudfunctions.net/gov-grant-disb)

### Outlined objectives and what was achieved
- [x] Create endpoint for creating household
- [x] Create endpoint for adding members to household
- [x] Create endpoint for listing all households
- [x] Create endpoint for searching for a specific household
- [x] Create endpoint for listing household eligible for specific grants
- [x] Deploy the API onto a cloud provider
- [ ] Containerize the application
- [ ] Add unit tests where applicable

### Overall system architecture
The API is designed cloud first to be deployed onto Google's Cloud Functions. The underlying datastore for the application is in Firestore. 

---

### API endpoints

### Create a Household
**Endpoint:** ```POST /create_hh```

#### Arguments
Argument | Description
--- | ---
```housing_type```  *(Required)* | A string of values of any of the following ```landed``` ```condo``` ```hdb``` ```others```

#### Returns
Property | Description
--- | ---
```hh_id``` | The string document ID of the newly created household document

---

### Add member to a Household
**Endpoint:** ```POST /add_mb```

#### Arguments
Argument | Description
--- | ---
```hh_id``` *(Required)* | A string document ID of a household
```name``` *(Required)* | An arbitrary string of the member's name
```gender``` *(Required)* | A string of values of any of the following ```male``` ```female``` ```others```
```marital_status``` *(Required)* | A string of values of any of the following ```single``` ```married``` ```divorced``` ```widowed```
```spouse``` | An arbitrary string of the member's spouse's name. Must be empty if ```marital_status``` is not ```married```. Must be given if ```marital_status``` is ```married```.
```occupation_type``` *(Required)* | A string of values of any of the following ```student``` ```unemployed``` ```employed```
```annual_income``` | An arbitrary float of the member's annual income. Can be omitted if ```occupation_type``` is not ```employed```.
```dob``` *(Required)* | An arbitrary integer of the member's date of birth in the format *YYYYMMDD*

**Returns:** Nothing

---

### Search a Household
**Endpoint:** ```GET /search_hh```

#### Arguments
Argument | Description
--- | ---
```hh_id``` | A string document ID of a household. If omitted, returns all households.

#### Returns
A list of any number of the following object:
Property | Description
--- | ---
```hh_id``` | A string document ID of a household 
```housing_type``` | The housing type of the household
```members``` | A list of any number of the following object: <table> <thead> <tr> <th>Property</th> <th>Description</th> </tr> </thead> <tbody> <tr><td>```pers_id```</td><td>A string document ID of the member</td><tr> <tr><td>```name```</td><td>A string of the name of the member</td><tr> <tr><td>```gender```</td><td>A string of the gender of the member</td><tr> <tr><td>```marital_status```</td><td>A string of the marital status of the member</td><tr> <tr><td>```spouse```</td><td>A string of the name of the member's spouse</td><tr> <tr><td>```occupation_type```</td><td>A string of the occupation type of the member</td><tr> <tr><td>```annual_income```</td><td>A float of the annual income of the member</td><tr> <tr><td>```dob```</td><td>An integer of the date of birth of the member</td><tr> </tbody> </table>

---

### List households eligible for a grant
**Endpoint:** ```GET /list_grants```

#### Arguments
Argument | Description
--- | ---
```grant_name``` *(Required)* | A string of value of any of the following ```seb``` ```mgs``` ```elb``` ```bsg``` ```ygg```
#### Returns
A list of any number of the following object:
Property | Description
--- | ---
```hh_id``` | A string document ID of a household 
```housing_type``` | The housing type of the household
```members``` | A list of any number of the following object: <table> <thead> <tr> <th>Property</th> <th>Description</th> </tr> </thead> <tbody> <tr><td>```pers_id```</td><td>A string document ID of the member</td><tr> <tr><td>```name```</td><td>A string of the name of the member</td><tr> <tr><td>```gender```</td><td>A string of the gender of the member</td><tr> <tr><td>```marital_status```</td><td>A string of the marital status of the member</td><tr> <tr><td>```spouse```</td><td>A string of the name of the member's spouse</td><tr> <tr><td>```occupation_type```</td><td>A string of the occupation type of the member</td><tr> <tr><td>```annual_income```</td><td>A float of the annual income of the member</td><tr> <tr><td>```dob```</td><td>An integer of the date of birth of the member</td><tr> </tbody> </table>

---

### Libraries used
- [Flask](https://pypi.org/project/Flask/)
- [google-cloud-firestore](https://pypi.org/project/google-cloud-firestore/)

Made with :purple_heart: and :coffee: in Singapore.