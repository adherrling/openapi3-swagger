# DestinyDefinitionsDestinyClassDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**gendered_class_names** | **dict(str, str)** | A localized string referring to the singular form of the Class&#39;s name when referred to in gendered form.Keyed by the DestinyGender. | [optional] 
**mentor_vendor_hash** | **int** | If the Class has a Mentor (all classes *should*), this will be the hash identifier for that Vendor if you care. | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


