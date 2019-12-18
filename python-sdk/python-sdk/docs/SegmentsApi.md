# egoi-api.SegmentsApi

All URIs are relative to *http://api-v3.egoiapp.max*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /lists/{list_id}/segments | Create new segment
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /lists/{list_id}/segments/{segment_id} | Remove segment
[**get_all_segments**](SegmentsApi.md#get_all_segments) | **GET** /lists/{list_id}/segments | Get all segments
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /lists/{list_id}/segments/{segment_id} | Get segment


# **create_segment**
> SavedSegment create_segment(list_id, saved_segment)

Create new segment

Create a new segment

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
api_instance = egoi-api.SegmentsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
saved_segment = egoi-api.SavedSegment() # SavedSegment | Parameters for the segment

try:
    # Create new segment
    api_response = api_instance.create_segment(list_id, saved_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **saved_segment** | [**SavedSegment**](SavedSegment.md)| Parameters for the segment | 

### Return type

[**SavedSegment**](SavedSegment.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> delete_segment(segment_id, list_id)

Remove segment

Remove segment information given its ID

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
api_instance = egoi-api.SegmentsApi(egoi-api.ApiClient(configuration))
segment_id = 'segment_id_example' # str | ID of the Segment
list_id = 56 # int | ID of the List

try:
    # Remove segment
    api_instance.delete_segment(segment_id, list_id)
except ApiException as e:
    print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**| ID of the Segment | 
 **list_id** | **int**| ID of the List | 

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

# **get_all_segments**
> SegmentCollection get_all_segments(list_id, type=type, name=name, offset=offset, limit=limit)

Get all segments

Returns all segments

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
api_instance = egoi-api.SegmentsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
type = 'type_example' # str | Type of segment (optional)
name = 'name_example' # str | Segment name (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)

try:
    # Get all segments
    api_response = api_instance.get_all_segments(list_id, type=type, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_all_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **type** | **str**| Type of segment | [optional] 
 **name** | **str**| Segment name | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]

### Return type

[**SegmentCollection**](SegmentCollection.md)

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

# **get_segment**
> Segment get_segment(segment_id, list_id)

Get segment

Returns segment information given its ID

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
api_instance = egoi-api.SegmentsApi(egoi-api.ApiClient(configuration))
segment_id = 'segment_id_example' # str | ID of the Segment
list_id = 56 # int | ID of the List

try:
    # Get segment
    api_response = api_instance.get_segment(segment_id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**| ID of the Segment | 
 **list_id** | **int**| ID of the List | 

### Return type

[**Segment**](Segment.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

