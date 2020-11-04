# blackcart-api

### How to run
Once you have this repo cloned, it's very simple to get started.
1. Cd into the root directory
2. Run "pip install -r requirements.txt" (In some cases your pip may have the alias pip3 in which case you must use "pip3" instead of "pip")
3. Run "flask run" (This should start the development server on 127.0.0.1:5000)
If for any reason you have trouble with step 3, you can run "python run.py" while in the root directory instead of "flask run".

### Test endpoint
#### Endpoint: /stores/{store_id}/products
1. Make a GET request to the endpoint above

### How to run test suite
1. Cd into the root directory
2. Run "pytest -v"
- "v" flag is for verbose. It is optional.
- More tests could've been added if more time was given.
- Tests based mostly on the response for that endpoint since it is only one endpoint which was requested and it happens to be a get request.
- Tests I would've added if I had more time would be to test the logic of the helper(private) methods in the controllers such as "_format_product" and "_format_variant" and possibly a couple more to really ensure that the endpoints response output is always consistent.

### Additional Information
- Due to the time constraint, i was not able to include full API documentation however I would normally use something like SwaggerUI for this. (https://swagger.io/tools/swagger-ui/).
- Some other things could possibly be changed if I had more time to work on this but as i was asked to only put in a few hours, I decided to stop here.

### API Documentation
#### Request
Example Request:
```
GET 127.0.0.1:5000/stores/1/products
```

#### Response
Example Response:
```
{
    "data": [
        {
            "id": 921728736,
            "in_stock": true,
            "name": "IPod Touch 8GB",
            "options": [
                {
                    "title": [
                    "Black"
                    ]
                }
            ],
            "variants": [
                {
                    "id": 447654529,
                    "inventory": 13,
                    "prices": [
                        {
                            "amount": "199.00",
                            "code": "USD",
                            "compare": null
                        }
                    ],
                    "weight": {
                        "unit": "lb",
                        "weight": 1.25
                    }
                }
            ]
        }
    ],
    "success": true
}
```