import pyotp
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
secret_base32 = 'thisisoursecretkey'
totp = pyotp.TOTP(secret_base32)


@app.function_name(name="HttpTrigger1")
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    code = req.params.get('code')
    if not code:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            code = req_body.get('code')

    if code:
        is_valid = totp.verify(code)
        return func.HttpResponse(f"Hello, {code}. This HTTP triggered function executed successfully with result {is_valid}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )