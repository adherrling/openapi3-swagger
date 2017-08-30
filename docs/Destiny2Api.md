# swagger_client.Destiny2Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destiny2_activate_talent_node**](Destiny2Api.md#destiny2_activate_talent_node) | **POST** /Destiny2/Actions/Items/ActivateTalentNode/ | 
[**destiny2_equip_item**](Destiny2Api.md#destiny2_equip_item) | **POST** /Destiny2/Actions/Items/EquipItem/ | 
[**destiny2_equip_items**](Destiny2Api.md#destiny2_equip_items) | **POST** /Destiny2/Actions/Items/EquipItems/ | 
[**destiny2_get_activity_history**](Destiny2Api.md#destiny2_get_activity_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
[**destiny2_get_character**](Destiny2Api.md#destiny2_get_character) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/ | 
[**destiny2_get_clan_aggregate_stats**](Destiny2Api.md#destiny2_get_clan_aggregate_stats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
[**destiny2_get_clan_leaderboards**](Destiny2Api.md#destiny2_get_clan_leaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
[**destiny2_get_clan_weekly_reward_state**](Destiny2Api.md#destiny2_get_clan_weekly_reward_state) | **GET** /Destiny2/Clan/{groupId}/WeeklyRewardState/ | 
[**destiny2_get_destiny_aggregate_activity_stats**](Destiny2Api.md#destiny2_get_destiny_aggregate_activity_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
[**destiny2_get_destiny_manifest**](Destiny2Api.md#destiny2_get_destiny_manifest) | **GET** /Destiny2/Manifest/ | 
[**destiny2_get_historical_stats**](Destiny2Api.md#destiny2_get_historical_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
[**destiny2_get_historical_stats_definition**](Destiny2Api.md#destiny2_get_historical_stats_definition) | **GET** /Destiny2/Stats/Definition/ | 
[**destiny2_get_historical_stats_for_account**](Destiny2Api.md#destiny2_get_historical_stats_for_account) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
[**destiny2_get_item**](Destiny2Api.md#destiny2_get_item) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/ | 
[**destiny2_get_leaderboards**](Destiny2Api.md#destiny2_get_leaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
[**destiny2_get_leaderboards_for_character**](Destiny2Api.md#destiny2_get_leaderboards_for_character) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**destiny2_get_post_game_carnage_report**](Destiny2Api.md#destiny2_get_post_game_carnage_report) | **GET** /Destiny2/Stats/PostGameCarnageReport/{activityId}/ | 
[**destiny2_get_profile**](Destiny2Api.md#destiny2_get_profile) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/ | 
[**destiny2_get_public_milestone_content**](Destiny2Api.md#destiny2_get_public_milestone_content) | **GET** /Destiny2/Milestones/{milestoneHash}/Content/ | 
[**destiny2_get_public_milestones**](Destiny2Api.md#destiny2_get_public_milestones) | **GET** /Destiny2/Milestones/ | 
[**destiny2_get_unique_weapon_history**](Destiny2Api.md#destiny2_get_unique_weapon_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
[**destiny2_get_vendor**](Destiny2Api.md#destiny2_get_vendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
[**destiny2_get_vendors**](Destiny2Api.md#destiny2_get_vendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
[**destiny2_insert_socket_plug**](Destiny2Api.md#destiny2_insert_socket_plug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
[**destiny2_search_destiny_entities**](Destiny2Api.md#destiny2_search_destiny_entities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 
[**destiny2_search_destiny_player**](Destiny2Api.md#destiny2_search_destiny_player) | **GET** /Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/ | 
[**destiny2_set_item_lock_state**](Destiny2Api.md#destiny2_set_item_lock_state) | **POST** /Destiny2/Actions/Items/SetLockState/ | 
[**destiny2_transfer_item**](Destiny2Api.md#destiny2_transfer_item) | **POST** /Destiny2/Actions/Items/TransferItem/ | 


# **destiny2_activate_talent_node**
> destiny2_activate_talent_node()



Activate a Talent Node.  Chill out, everyone: we haven't decided yet whether this will be able to activate nodes with costs, but if we do it will require special scope permission for an application attempting to do so.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.  PREVIEW: This service is not actually implemented yet, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_activate_talent_node()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_activate_talent_node: %s\n" % e)
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

# **destiny2_equip_item**
> destiny2_equip_item()



Equip an item.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_equip_item()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_equip_item: %s\n" % e)
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

# **destiny2_equip_items**
> destiny2_equip_items()



Equip a list of items by itemInstanceIds.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.  Any items not found on your character will be ignored.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_equip_items()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_equip_items: %s\n" % e)
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

# **destiny2_get_activity_history**
> destiny2_get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)



Gets activity history stats for indicated character.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The id of the character to retrieve.
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
count = 'count_example' # str | Number of rows to return (optional)
mode = 'mode_example' # str | A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. (optional)
page = 'page_example' # str | Page number to return, starting with 0. (optional)

try: 
    api_instance.destiny2_get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_activity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The id of the character to retrieve. | 
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **count** | **str**| Number of rows to return | [optional] 
 **mode** | **str**| A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. | [optional] 
 **page** | **str**| Page number to return, starting with 0. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_character**
> destiny2_get_character(character_id, destiny_membership_id, membership_type, components=components)



Returns character information for the supplied character.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 789 # int | ID of the character.
destiny_membership_id = 'destiny_membership_id_example' # str | Destiny membership ID.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
components = 'components_example' # str | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_instance.destiny2_get_character(character_id, destiny_membership_id, membership_type, components=components)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| ID of the character. | 
 **destiny_membership_id** | **str**| Destiny membership ID. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **components** | **str**| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_clan_aggregate_stats**
> destiny2_get_clan_aggregate_stats(group_id, modes=modes)



Gets aggregated stats for a clan using the same categories as the clan leaderboards.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
group_id = 'group_id_example' # str | Group ID of the clan whose leaderboards you wish to fetch.
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)

try: 
    api_instance.destiny2_get_clan_aggregate_stats(group_id, modes=modes)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_clan_aggregate_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_clan_leaderboards**
> destiny2_get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
group_id = 'group_id_example' # str | Group ID of the clan whose leaderboards you wish to fetch.
maxtop = 'maxtop_example' # str | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_instance.destiny2_get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_clan_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **maxtop** | **str**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_clan_weekly_reward_state**
> destiny2_get_clan_weekly_reward_state(group_id)



Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
group_id = 'group_id_example' # str | A valid group id of clan.

try: 
    api_instance.destiny2_get_clan_weekly_reward_state(group_id)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_clan_weekly_reward_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A valid group id of clan. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_destiny_aggregate_activity_stats**
> destiny2_get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)



Gets all activities the character has participated in together with aggregate statistics for those activities.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The specific character whose activities should be returned.
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.

try: 
    api_instance.destiny2_get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_destiny_aggregate_activity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The specific character whose activities should be returned. | 
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_destiny_manifest**
> destiny2_get_destiny_manifest()



Returns the current version of the manifest as a json object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_get_destiny_manifest()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_destiny_manifest: %s\n" % e)
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

# **destiny2_get_historical_stats**
> destiny2_get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)



Gets historical stats for indicated character.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
dayend = 'dayend_example' # str | Last day to return when daily stats are requested.  Use the format YYYY-MM-DD. (optional)
daystart = 'daystart_example' # str | First day to return when daily stats are requested. Use the format YYYY-MM-DD (optional)
groups = 'groups_example' # str | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals (optional)
modes = 'modes_example' # str | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
period_type = 'period_type_example' # str | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity (optional)

try: 
    api_instance.destiny2_get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_historical_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. | 
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **dayend** | **str**| Last day to return when daily stats are requested.  Use the format YYYY-MM-DD. | [optional] 
 **daystart** | **str**| First day to return when daily stats are requested. Use the format YYYY-MM-DD | [optional] 
 **groups** | **str**| Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals | [optional] 
 **modes** | **str**| Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **period_type** | **str**| Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_historical_stats_definition**
> destiny2_get_historical_stats_definition()



Gets historical stats definitions.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_get_historical_stats_definition()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_historical_stats_definition: %s\n" % e)
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

# **destiny2_get_historical_stats_for_account**
> destiny2_get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)



Gets aggregate historical stats organized around each character for a given account.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
groups = 'groups_example' # str | Groups of stats to include, otherwise only general stats are returned.  Comma separated list is allowed. Values: General, Weapons, Medals. (optional)

try: 
    api_instance.destiny2_get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_historical_stats_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **groups** | **str**| Groups of stats to include, otherwise only general stats are returned.  Comma separated list is allowed. Values: General, Weapons, Medals. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_item**
> destiny2_get_item(destiny_membership_id, item_instance_id, membership_type, components=components)



Retrieve the details of an instanced Destiny Item.  An instanced Destiny item is one with an ItemInstanceId.  Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
destiny_membership_id = 'destiny_membership_id_example' # str | The membership ID of the destiny profile.
item_instance_id = 'item_instance_id_example' # str | The Instance ID of the destiny item.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
components = 'components_example' # str | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_instance.destiny2_get_item(destiny_membership_id, item_instance_id, membership_type, components=components)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **str**| The membership ID of the destiny profile. | 
 **item_instance_id** | **str**| The Instance ID of the destiny item. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **components** | **str**| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_leaderboards**
> destiny2_get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint has not yet been implemented.  It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
maxtop = 'maxtop_example' # str | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_instance.destiny2_get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **maxtop** | **str**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_leaderboards_for_character**
> destiny2_get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The specific character to build the leaderboard around for the provided Destiny Membership.
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
maxtop = 'maxtop_example' # str | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_instance.destiny2_get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_leaderboards_for_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The specific character to build the leaderboard around for the provided Destiny Membership. | 
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **maxtop** | **str**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_post_game_carnage_report**
> destiny2_get_post_game_carnage_report(activity_id)



Gets the available post game carnage report for the activity ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
activity_id = 'activity_id_example' # str | The ID of the activity whose PGCR is requested.

try: 
    api_instance.destiny2_get_post_game_carnage_report(activity_id)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_post_game_carnage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| The ID of the activity whose PGCR is requested. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_profile**
> destiny2_get_profile(destiny_membership_id, membership_type, components=components)



Returns Destiny Profile information for the supplied membership.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
destiny_membership_id = 'destiny_membership_id_example' # str | Destiny membership ID.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
components = 'components_example' # str | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_instance.destiny2_get_profile(destiny_membership_id, membership_type, components=components)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **str**| Destiny membership ID. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **components** | **str**| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_public_milestone_content**
> destiny2_get_public_milestone_content(milestone_hash)



Gets custom localized content for the milestone of the given hash, if it exists.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
milestone_hash = 'milestone_hash_example' # str | The identifier for the milestone to be returned.

try: 
    api_instance.destiny2_get_public_milestone_content(milestone_hash)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_public_milestone_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_hash** | **str**| The identifier for the milestone to be returned. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_public_milestones**
> destiny2_get_public_milestones()



Gets public information about currently available Milestones.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_get_public_milestones()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_public_milestones: %s\n" % e)
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

# **destiny2_get_unique_weapon_history**
> destiny2_get_unique_weapon_history(character_id, destiny_membership_id, membership_type)



Gets details about unique weapon usage, including all exotic weapons.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The id of the character to retrieve.
destiny_membership_id = 'destiny_membership_id_example' # str | The Destiny membershipId of the user to retrieve.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.

try: 
    api_instance.destiny2_get_unique_weapon_history(character_id, destiny_membership_id, membership_type)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_unique_weapon_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The id of the character to retrieve. | 
 **destiny_membership_id** | **str**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_vendor**
> destiny2_get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)



Get the details of a specific Vendor.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 'destiny_membership_id_example' # str | Destiny membership ID of another user. You may be denied.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
vendor_hash = 'vendor_hash_example' # str | The Hash identifier of the Vendor to be returned.
components = 'components_example' # str | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_instance.destiny2_get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **str**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **vendor_hash** | **str**| The Hash identifier of the Vendor to be returned. | 
 **components** | **str**| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_vendors**
> destiny2_get_vendors(character_id, destiny_membership_id, membership_type, components=components)



Get currently available vendors.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
character_id = 'character_id_example' # str | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 'destiny_membership_id_example' # str | Destiny membership ID of another user. You may be denied.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type.
components = 'components_example' # str | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_instance.destiny2_get_vendors(character_id, destiny_membership_id, membership_type, components=components)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **str**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **str**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **str**| A valid non-BungieNet membership type. | 
 **components** | **str**| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_insert_socket_plug**
> destiny2_insert_socket_plug()



Insert a plug into a socketed item.  I know how it sounds, but I assure you it's much more G-rated than you might be guessing.  We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_insert_socket_plug()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_insert_socket_plug: %s\n" % e)
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

# **destiny2_search_destiny_entities**
> destiny2_search_destiny_entities(search_term, type, page=page)



Gets a page list of Destiny items.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
search_term = 'search_term_example' # str | The string to use when searching for Destiny entities.
type = 'type_example' # str | The type of entity for whom you would like results.  These correspond to the entity's definition contract name.  For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
page = 'page_example' # str | Page number to return, starting with 0. (optional)

try: 
    api_instance.destiny2_search_destiny_entities(search_term, type, page=page)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_search_destiny_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The string to use when searching for Destiny entities. | 
 **type** | **str**| The type of entity for whom you would like results.  These correspond to the entity&#39;s definition contract name.  For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is tentatively in final form, but there may be bugs that prevent desirable operation. | 
 **page** | **str**| Page number to return, starting with 0. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_search_destiny_player**
> destiny2_search_destiny_player(display_name, membership_type)



Returns a list of Destiny memberships given a full Gamertag or PSN ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()
display_name = 'display_name_example' # str | The full gamertag or PSN id of the player. Spaces and case are ignored.
membership_type = 'membership_type_example' # str | A valid non-BungieNet membership type, or All.

try: 
    api_instance.destiny2_search_destiny_player(display_name, membership_type)
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_search_destiny_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| The full gamertag or PSN id of the player. Spaces and case are ignored. | 
 **membership_type** | **str**| A valid non-BungieNet membership type, or All. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_set_item_lock_state**
> destiny2_set_item_lock_state()



Set the Lock State for an instanced item.  You must have a valid Destiny Account.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_set_item_lock_state()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_set_item_lock_state: %s\n" % e)
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

# **destiny2_transfer_item**
> destiny2_transfer_item()



Transfer an item to/from your vault.  You must have a valid Destiny account.  You must also pass BOTH a reference AND an instance ID if it's an instanced item.  itshappening.gif

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Destiny2Api()

try: 
    api_instance.destiny2_transfer_item()
except ApiException as e:
    print("Exception when calling Destiny2Api->destiny2_transfer_item: %s\n" % e)
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

