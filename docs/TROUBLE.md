## 1. DynamoDB Key Schema Mismatch

**Error:** `An error occurred (ValidationException) when calling the GetItem operation: The provided key element does not match the schema`
**Cause:** The key name used in the `GetItem` request (`code_name`) didn't match the expected key defined in DynamoDB. The challenge uses camelCase, so the correct key is `codeName`.
**Fix:** Contacted Eliran, who confirmed all fields use camelCase. Updated the request to use `'codeName': {'S': code_name}` to resolve the issue.

## 2. Travis CI Python 3.12 not supported

**Cause:** Default distro (xenial) did not support Python 3.x.
**Fix:** Downgraded to Python 3.10 and set `dist: jammy`.

## 3. ModuleNotFoundError: 'app' is not a package

**Cause:** Missing `__init__.py` and wrong Docker path.
**Fix:** Added `__init__.py` and used `CMD ["python", "-m", "app.app"]`.
