# DestinyDefinitionsSocketsDestinySocketTypeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plug_whitelist** | [**list[ComponentsschemasDestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition]**](ComponentsschemasDestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.md) | A list of Plug \&quot;Categories\&quot; that are allowed to be plugged into sockets of this type.  These should be compared against a given plug item&#39;s DestinyInventoryItemDefinition.plug.plugCategoryHash,which indicates the plug item&#39;s category.  If the plug&#39;s category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted. | [optional] 
**socket_category_hash** | **int** |  | [optional] 
**visibility** | [**ComponentsschemasDestinyDestinySocketVisibility**](ComponentsschemasDestinyDestinySocketVisibility.md) |  | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


