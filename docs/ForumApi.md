# swagger_client.ForumApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forum_approve_fireteam_thread**](ForumApi.md#forum_approve_fireteam_thread) | **POST** /Forum/Recruit/Approve/{topicId}/ | 
[**forum_get_core_topics_paged**](ForumApi.md#forum_get_core_topics_paged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ | 
[**forum_get_forum_tag_suggestions**](ForumApi.md#forum_get_forum_tag_suggestions) | **GET** /Forum/GetForumTagSuggestions/ | 
[**forum_get_poll**](ForumApi.md#forum_get_poll) | **GET** /Forum/Poll/{topicId}/ | 
[**forum_get_post_and_parent**](ForumApi.md#forum_get_post_and_parent) | **GET** /Forum/GetPostAndParent/{childPostId}/ | 
[**forum_get_post_and_parent_awaiting_approval**](ForumApi.md#forum_get_post_and_parent_awaiting_approval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ | 
[**forum_get_posts_threaded_paged**](ForumApi.md#forum_get_posts_threaded_paged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ | 
[**forum_get_posts_threaded_paged_from_child**](ForumApi.md#forum_get_posts_threaded_paged_from_child) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ | 
[**forum_get_recruitment_thread_summaries**](ForumApi.md#forum_get_recruitment_thread_summaries) | **POST** /Forum/Recruit/Summaries/ | 
[**forum_get_topic_for_content**](ForumApi.md#forum_get_topic_for_content) | **GET** /Forum/GetTopicForContent/{contentId}/ | 
[**forum_get_topics_paged**](ForumApi.md#forum_get_topics_paged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ | 
[**forum_join_fireteam_thread**](ForumApi.md#forum_join_fireteam_thread) | **POST** /Forum/Recruit/Join/{topicId}/ | 
[**forum_kick_ban_fireteam_applicant**](ForumApi.md#forum_kick_ban_fireteam_applicant) | **POST** /Forum/Recruit/KickBan/{topicId}/{targetMembershipId}/ | 
[**forum_leave_fireteam_thread**](ForumApi.md#forum_leave_fireteam_thread) | **POST** /Forum/Recruit/Leave/{topicId}/ | 


# **forum_approve_fireteam_thread**
> forum_approve_fireteam_thread(topic_id)



Allows the owner of a fireteam thread to approve all joined members and start a private message conversation with them.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 'topic_id_example' # str | The post id of the recruitment topic to approve.

try: 
    api_instance.forum_approve_fireteam_thread(topic_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_approve_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **str**| The post id of the recruitment topic to approve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_core_topics_paged**
> forum_get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)



Gets a listing of all topics marked as part of the core group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
category_filter = 'category_filter_example' # str | The category filter.
page = 'page_example' # str | Zero base page
quick_date = 'quick_date_example' # str | The date filter.
sort = 'sort_example' # str | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)

try: 
    api_instance.forum_get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_core_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **str**| The category filter. | 
 **page** | **str**| Zero base page | 
 **quick_date** | **str**| The date filter. | 
 **sort** | **str**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_forum_tag_suggestions**
> forum_get_forum_tag_suggestions(partialtag=partialtag)



Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
partialtag = 'partialtag_example' # str | The partial tag input to generate suggestions from. (optional)

try: 
    api_instance.forum_get_forum_tag_suggestions(partialtag=partialtag)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_forum_tag_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partialtag** | **str**| The partial tag input to generate suggestions from. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_poll**
> forum_get_poll(topic_id)



Gets the specified forum poll.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 'topic_id_example' # str | The post id of the topic that has the poll.

try: 
    api_instance.forum_get_poll(topic_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **str**| The post id of the topic that has the poll. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_post_and_parent**
> forum_get_post_and_parent(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 'child_post_id_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_instance.forum_get_post_and_parent(child_post_id, showbanned=showbanned)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_post_and_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_post_and_parent_awaiting_approval**
> forum_get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent of posts that are awaiting approval.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 'child_post_id_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_instance.forum_get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_post_and_parent_awaiting_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_posts_threaded_paged**
> forum_get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
get_parent_post = 'get_parent_post_example' # str | 
page = 'page_example' # str | 
page_size = 'page_size_example' # str | 
parent_post_id = 'parent_post_id_example' # str | 
reply_size = 'reply_size_example' # str | 
root_thread_mode = 'root_thread_mode_example' # str | 
sort_mode = 'sort_mode_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_instance.forum_get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_posts_threaded_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_parent_post** | **str**|  | 
 **page** | **str**|  | 
 **page_size** | **str**|  | 
 **parent_post_id** | **str**|  | 
 **reply_size** | **str**|  | 
 **root_thread_mode** | **str**|  | 
 **sort_mode** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_posts_threaded_paged_from_child**
> forum_get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 'child_post_id_example' # str | 
page = 'page_example' # str | 
page_size = 'page_size_example' # str | 
reply_size = 'reply_size_example' # str | 
root_thread_mode = 'root_thread_mode_example' # str | 
sort_mode = 'sort_mode_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_instance.forum_get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_posts_threaded_paged_from_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **str**|  | 
 **page** | **str**|  | 
 **page_size** | **str**|  | 
 **reply_size** | **str**|  | 
 **root_thread_mode** | **str**|  | 
 **sort_mode** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_recruitment_thread_summaries**
> forum_get_recruitment_thread_summaries()



Allows the caller to get a list of to 25 recruitment thread summary information objects.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()

try: 
    api_instance.forum_get_recruitment_thread_summaries()
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_recruitment_thread_summaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_topic_for_content**
> forum_get_topic_for_content(content_id)



Gets the post Id for the given content item's comments, if it exists.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
content_id = 'content_id_example' # str | 

try: 
    api_instance.forum_get_topic_for_content(content_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_topic_for_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_topics_paged**
> forum_get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)



Get topics from any forum.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
category_filter = 'category_filter_example' # str | A category filter
group = 'group_example' # str | The group, if any.
page = 'page_example' # str | Zero paged page number
page_size = 'page_size_example' # str | Unused
quick_date = 'quick_date_example' # str | A date filter.
sort = 'sort_example' # str | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)
tagstring = 'tagstring_example' # str | The tags to search, if any. (optional)

try: 
    api_instance.forum_get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **str**| A category filter | 
 **group** | **str**| The group, if any. | 
 **page** | **str**| Zero paged page number | 
 **page_size** | **str**| Unused | 
 **quick_date** | **str**| A date filter. | 
 **sort** | **str**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 
 **tagstring** | **str**| The tags to search, if any. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_join_fireteam_thread**
> forum_join_fireteam_thread(topic_id)



Allows a user to slot themselves into a recuritment thread fireteam slot. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 'topic_id_example' # str | The post id of the recruitment topic you wish to join.

try: 
    api_instance.forum_join_fireteam_thread(topic_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_join_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **str**| The post id of the recruitment topic you wish to join. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_kick_ban_fireteam_applicant**
> forum_kick_ban_fireteam_applicant(target_membership_id, topic_id)



Allows a recruitment thread owner to kick a join user from the fireteam. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
target_membership_id = 'target_membership_id_example' # str | The id of the user you wish to kick.
topic_id = 'topic_id_example' # str | The post id of the recruitment topic you wish to join.

try: 
    api_instance.forum_kick_ban_fireteam_applicant(target_membership_id, topic_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_kick_ban_fireteam_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_membership_id** | **str**| The id of the user you wish to kick. | 
 **topic_id** | **str**| The post id of the recruitment topic you wish to join. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_leave_fireteam_thread**
> forum_leave_fireteam_thread(topic_id)



Allows a user to remove themselves from a recuritment thread fireteam slot. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 'topic_id_example' # str | The post id of the recruitment topic you wish to leave.

try: 
    api_instance.forum_leave_fireteam_thread(topic_id)
except ApiException as e:
    print("Exception when calling ForumApi->forum_leave_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **str**| The post id of the recruitment topic you wish to leave. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

