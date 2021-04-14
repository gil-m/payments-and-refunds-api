# Payments API
http://localhost:1111/api

## GET "/api/payments"

Retrieves the complete list of payments respecting query parameters whitout the additional parameters. Optional parameters:

* ```payment_id``` (```string```): matches an exact ```payment_id```
* ```payment_method``` (```string```): choices are ```'credit_card'``` or ```'mbway'```
* ```status``` (```string```): choices are ```'success'```, ```'error'``` or ```'settled'```
* ```amount_gte``` (```float```): will retrieve all entries that have an amount greater or equal to this parameter.
* ```amount_lte``` (```float```): will retrieve all entries that have an amount lesser or equal to this parameter.
* ```created_at_gte``` (```datetime```): will retrieve all entries that have been created after or equal to this parameter.
* ```created_at_lte``` (```datetime```): will retrieve all entries that have been created before or equal to this parameter.
* ```settled_at_gte``` (```datetime```): will retrieve all entries that have been settled after or equal to this parameter.
* ```settled_at_lte``` (```datetime```): will retrieve all entries that have been settled before or equal to this parameter.

* Request url:
```
http://localhost:1111/api/payments?payment_id=TEST&payment_method=credit_card&status=settled&amount_gte=50.0&amount_lte=500.0&created_at_gte=2020-01-01T00:00:00&created_at_lte=2021-01-01T00:00:00&settled_at_gte=2020-01-01T00:00:00&settled_at_lte=2021-01-01T00:00:00
```

* Curl example:
```
curl -X GET "http://localhost:1111/api/payments?payment_id=TEST&payment_method=credit_card&status=settled&amount_gte=50.0&amount_lte=500.0&created_at_gte=2020-01-01T00:00:00&created_at_lte=2021-01-01T00:00:00&settled_at_gte=2020-01-01T00:00:00&settled_at_lte=2021-01-01T00:00:00" -H "accept: application/json"
```

* Example response:
```
[
    {
        "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50.0,
        "payment_method": "credit_card",
        "status": "settled",
        "settled_at": "2020-04-07T15:01:07.000",
        "settled_amount": 50
    }
]
```

## GET "/api/payments/{id}"

Retrieves a single payment with the additional parameters or an empty result if none are found.

* Request url:
```
http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM
```

* Curl example:
```
curl -X GET "http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM" -H "accept: application/json"
```

* Example response:
```
{
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 50.0,
    "payment_method": "credit_card",
    "status": "settled",
    "settled_at": null,
    "settled_amount": null,
    "additional_params": {
        "payment": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

## POST "/api/payments"

Creates a new payment and returns it.

* Request url:
```
http://localhost:1111/api/payments
```

* Curl example:
```
curl -X POST "http://localhost:1111/api/payments" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"amount\":50.0,\"payment_method\":\"credit_card\",\"additional_params\":{\"amount\":50,\"method\":\"credit_card\",\"number\":\"1234567890123456\",\"name\":\"John john\",\"expiration_month\":\"05\",\"expiration_year\":\"2028\",\"cvv\":\"321\"}}"
```

* Request body:
```
{
    "amount": 50.0,
    "payment_method": "credit_card",
    "additional_params": {
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

* Example response:
```
{
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 50.0,
    "payment_method": "credit_card",
    "status": "success",
    "settled_at": null,
    "settled_amount": null,
    "additional_params": {
        "payment": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

## PUT "/api/payments/{id}"

Updates an existing payment using its id as search parameter and returns it. If the query matches no objects, an empty response is returned.

* Request url:
```
http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM
```

* Curl example:
```
curl -X PUT "http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"amount\":50.0,\"payment_method\":\"credit_card\",\"additional_params\":{\"payment\":\"SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM\",\"amount\":50,\"method\":\"credit_card\",\"number\":\"1234567890123456\",\"name\":\"John john\",\"expiration_month\":\"05\",\"expiration_year\":\"2028\",\"cvv\":\"321\"}}"
```

* Request body:
```
{
    "amount": 50.0,
    "payment_method": "credit_card",
    "additional_params": {
        "payment": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

* Example response:
```
{
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 50.0,
    "payment_method": "credit_card",
    "status": "success",
    "settled_at": null,
    "settled_amount": null,
    "additional_params": {
        "payment": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

## DELETE "/api/payments/{id}"

Deletes an existing payment using its id as search parameter and returns it. If the query matches no objects, an empty response is returned.

* Request url: 
```
http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM
```

* Curl example:
```
curl -X DELETE "http://localhost:1111/api/payments/SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM" -H "accept: application/json"
```

* Example response:
```
{
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 50.0,
    "payment_method": "credit_card",
    "status": "success",
    "settled_at": null,
    "settled_amount": null,
    "additional_params": {
        "payment": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 50,
        "method": "credit_card",
        "number": "1234567890123456",
        "name": "John john",
        "expiration_month": "05",
        "expiration_year": "2028",
        "cvv": "321"
    }
}
```

# Refunds API
http://localhost:2222/api

## GET "/api/refunds"

Retrieves the complete list of payments respecting query parameters. Optional parameters:

* ```payment_id``` (```string```): matches an exact ```payment_id```
* ```refund_id``` (```string```): matches an exact ```refund_id```
* Request url:
```
http://localhost:2222/api/payments?payment_id=TEST&refund_id=SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM
```

* Curl example:
```
curl -X GET "http://localhost:2222/api/payments?payment_id=TEST&refund_id=SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM" -H "accept: application/json"
```

* Example response:
```
[
    {
        "refund_id": "6KwjOmYUdGuotNglvwfsvWzcMARa9ipIHzJXSmqaLqN68jykZtmNKQxVE1IGYEnT0Pmu6q3NAxztlOd8yGKbhQ3Su1eW0UGt9CryE1MYYiyLw3FGx8CcOx9EzN2GvRfggZUzw4EeVpX1C0SkD3kUKL1ULudMcJ8GU1d2QG454hgXckoYBKo9Jn8eSAgjXbK5hVIIrrQX",
        "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 20.0
    },
    {
        "refund_id": "pW30g8efRUrbR3ly6ZxW5KkQVWuCzyhdfsDEePLCJaAquXFDqNGc29iM59UtbakCL1UuURpPyZlcDIuOuE9m40B5n3XqTWh1FHfTZLT6CGCFfikANe6yo09I9CI4UFwiT393rV8MBI7Xh3oVj4LaCK52ITqY7AipZnOOG0sgfPKV0oRmia0yPgn51SFsNIf3VxSl0UxB",
        "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
        "amount": 20.0
    }
]
```

## GET "/api/refunds/{id}"

Retrieves a single payment or an empty result if none are found.

* Request url:
```
http://localhost:1111/api/refunds/pW30g8efRUrbR3ly6ZxW5KkQVWuCzyhdfsDEePLCJaAquXFDqNGc29iM59UtbakCL1UuURpPyZlcDIuOuE9m40B5n3XqTWh1FHfTZLT6CGCFfikANe6yo09I9CI4UFwiT393rV8MBI7Xh3oVj4LaCK52ITqY7AipZnOOG0sgfPKV0oRmia0yPgn51SFsNIf3VxSl0UxB
```

* Curl example:
```
curl -X GET "http://localhost:1111/api/refunds/pW30g8efRUrbR3ly6ZxW5KkQVWuCzyhdfsDEePLCJaAquXFDqNGc29iM59UtbakCL1UuURpPyZlcDIuOuE9m40B5n3XqTWh1FHfTZLT6CGCFfikANe6yo09I9CI4UFwiT393rV8MBI7Xh3oVj4LaCK52ITqY7AipZnOOG0sgfPKV0oRmia0yPgn51SFsNIf3VxSl0UxB" -H "accept: application/json"
```

* Example response:
```
{
    "refund_id": "pW30g8efRUrbR3ly6ZxW5KkQVWuCzyhdfsDEePLCJaAquXFDqNGc29iM59UtbakCL1UuURpPyZlcDIuOuE9m40B5n3XqTWh1FHfTZLT6CGCFfikANe6yo09I9CI4UFwiT393rV8MBI7Xh3oVj4LaCK52ITqY7AipZnOOG0sgfPKV0oRmia0yPgn51SFsNIf3VxSl0UxB",
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 20.0
}
```

## POST "/api/refunds"

Creates a new refund and returns it.

* Request url:
```
http://localhost:1111/api/refunds
```

* Curl example:
```
curl -X POST "http://localhost:1111/api/refunds" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"amount\":20.0,\"payment_id\":\"SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM\"}"
```

* Request body:
```
{
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 20.0
}
```

* Example response:
```
{
    "refund_id": "pW30g8efRUrbR3ly6ZxW5KkQVWuCzyhdfsDEePLCJaAquXFDqNGc29iM59UtbakCL1UuURpPyZlcDIuOuE9m40B5n3XqTWh1FHfTZLT6CGCFfikANe6yo09I9CI4UFwiT393rV8MBI7Xh3oVj4LaCK52ITqY7AipZnOOG0sgfPKV0oRmia0yPgn51SFsNIf3VxSl0UxB",
    "payment_id": "SSUARQXWKPDJSTTGEPVRTEONTPDBQSUXOVRJTBGXWNCTGBBBJLEUKDUPNCZDPELHRUISCDEMMWRQNXBEKPQJCFWWASQOMCYALVAHFPFCVDTOJXODEMDLJRDDECVDAUZEMDVLLNJYJPSAYXRBLCTSYGLBWKUAEOWKWOANLLAJWMIBPXTHVPWZAETCEBPSEZZYLVQTSTSM",
    "amount": 20.0
}
```