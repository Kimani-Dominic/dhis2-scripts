# Importing datavalues to dhis2 instance 

* Step 1: Prepare the JSON/CSV File

 sample of Json file

```json
{
  "dataSet": "pBOMPrpg1QX",
  "completeDate": "2024-07-12",
  "period": "202401",
  "orgUnit": "DiszpKrYNg8",
  "attributeOptionCombo": "HllvX50cXC0",
  "dataValues": [
    {
      "dataElement": "f7n9E0hX8qk",
      "value": "10"
    },
    {
      "dataElement": "Ix2HsbDMLea",
      "value": "20"
    }
  ]
}
```


* Use curl to Import Data Values

```curl
curl -u admin:district -H "Content-Type: application/json" -X POST -d @dataValues.json http://localhost:8070/api/dataValueSets
```

* verify the import through the API
