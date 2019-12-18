# egoi-api.AutomationsApi

All URIs are relative to *http://api-v3.egoiapp.max*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automation**](AutomationsApi.md#create_automation) | **POST** /automations | Create new automation
[**delete_automation**](AutomationsApi.md#delete_automation) | **DELETE** /automations/{automation_id} | Remove automation
[**get_all_automations**](AutomationsApi.md#get_all_automations) | **GET** /automations | Get all automations
[**update_automation**](AutomationsApi.md#update_automation) | **PUT** /automations/{automation_id} | Update a specific automation


# **create_automation**
> Automation create_automation(automation)

Create new automation

Create a new automation

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
api_instance = egoi-api.AutomationsApi(egoi-api.ApiClient(configuration))
automation = egoi-api.Automation() # Automation | Parameters for the automation

try:
    # Create new automation
    api_response = api_instance.create_automation(automation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationsApi->create_automation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation** | [**Automation**](Automation.md)| Parameters for the automation | 

### Return type

[**Automation**](Automation.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_automation**
> delete_automation(automation_id)

Remove automation

Remove automation information given its ID

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
api_instance = egoi-api.AutomationsApi(egoi-api.ApiClient(configuration))
automation_id = 56 # int | ID of the Automation

try:
    # Remove automation
    api_instance.delete_automation(automation_id)
except ApiException as e:
    print("Exception when calling AutomationsApi->delete_automation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **int**| ID of the Automation | 

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_automations**
> AutomationCollection get_all_automations(automation_id=automation_id, title=title, created_by=created_by, list_id=list_id, status=status, offset=offset, limit=limit, order=order, order_by=order_by)

Get all automations

Returns all automations

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
api_instance = egoi-api.AutomationsApi(egoi-api.ApiClient(configuration))
automation_id = 56 # int | Reference attribute to automation id (optional)
title = 'title_example' # str | Reference attribute to title (optional)
created_by = 56 # int | Reference attribute to created by (optional)
list_id = 56 # int | ID of the list that owns the automation (optional)
status = 'status_example' # str | Automation status (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'automation_id' # str | Reference attribute to order automations (optional) (default to 'automation_id')

try:
    # Get all automations
    api_response = api_instance.get_all_automations(automation_id=automation_id, title=title, created_by=created_by, list_id=list_id, status=status, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationsApi->get_all_automations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **int**| Reference attribute to automation id | [optional] 
 **title** | **str**| Reference attribute to title | [optional] 
 **created_by** | **int**| Reference attribute to created by | [optional] 
 **list_id** | **int**| ID of the list that owns the automation | [optional] 
 **status** | **str**| Automation status | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order automations | [optional] [default to &#39;automation_id&#39;]

### Return type

[**AutomationCollection**](AutomationCollection.md)

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

# **update_automation**
> Automation update_automation(automation_id, automation)

Update a specific automation

Update an automation

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
api_instance = egoi-api.AutomationsApi(egoi-api.ApiClient(configuration))
automation_id = 56 # int | ID of the Automation
automation = egoi-api.Automation() # Automation | Parameters for the automation

try:
    # Update a specific automation
    api_response = api_instance.update_automation(automation_id, automation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationsApi->update_automation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **int**| ID of the Automation | 
 **automation** | [**Automation**](Automation.md)| Parameters for the automation | 

### Return type

[**Automation**](Automation.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

