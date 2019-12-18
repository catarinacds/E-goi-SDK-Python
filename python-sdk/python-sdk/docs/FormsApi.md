# egoi-api.FormsApi

All URIs are relative to *http://api-v3.egoiapp.max*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_forms**](FormsApi.md#get_all_forms) | **GET** /forms | Get all forms


# **get_all_forms**
> FormCollection get_all_forms(offset=offset, limit=limit, order=order, order_by=order_by, language=language, list_id=list_id, owner=owner, status=status, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max)

Get all forms

Returns all forms

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi-api
from egoi-api.rest import ApiException
from pprint import pprint
configuration = egoi-api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to http://api-v3.egoiapp.max
configuration.host = "http://api-v3.egoiapp.max"
# Create an instance of the API class
api_instance = egoi-api.FormsApi(egoi-api.ApiClient(configuration))
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'form_id' # str | Reference attribute to order forms (optional) (default to 'form_id')
language = 'language_example' # str | Language of the form (optional)
list_id = 56 # int | ID of the list that owns the form (optional)
owner = 56 # int | User ID of the form owner (optional)
status = 'status_example' # str | Status filter (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
updated_min = '2013-10-20T19:20:30+01:00' # datetime | Updated initial (optional)
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Updated finish (optional)

try:
    # Get all forms
    api_response = api_instance.get_all_forms(offset=offset, limit=limit, order=order, order_by=order_by, language=language, list_id=list_id, owner=owner, status=status, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->get_all_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order forms | [optional] [default to &#39;form_id&#39;]
 **language** | **str**| Language of the form | [optional] 
 **list_id** | **int**| ID of the list that owns the form | [optional] 
 **owner** | **int**| User ID of the form owner | [optional] 
 **status** | **str**| Status filter | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **updated_min** | **datetime**| Updated initial | [optional] 
 **updated_max** | **datetime**| Updated finish | [optional] 

### Return type

[**FormCollection**](FormCollection.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

