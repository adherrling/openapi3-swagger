# ContentContentItemPublicContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **int** |  | [optional] 
**c_type** | **str** |  | [optional] 
**cms_path** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**allow_comments** | **bool** |  | [optional] 
**has_age_gate** | **bool** |  | [optional] 
**minimum_age** | **int** |  | [optional] 
**rating_image_path** | **str** |  | [optional] 
**author** | [**ComponentsschemasUserGeneralUser**](ComponentsschemasUserGeneralUser.md) |  | [optional] 
**auto_english_property_fallback** | **bool** |  | [optional] 
**properties** | **dict(str, object)** | Firehose content is really a collection of metadata and \&quot;properties\&quot;, which arethe potentially-but-not-strictly localizable data that comprises the meat ofwhatever content is being shown.  As Cole Porter would have crooned, \&quot;Anything Goes\&quot; with Firehose properties.They are most often strings, but they can theoretically be anything.  They are JSONencoded, and could be JSON structures, simple strings, numbers etc...  The Content Typeof the item (cType) will describe the properties, and thus how they ought to be deserialized. | [optional] 
**representations** | [**list[ComponentsschemasContentContentRepresentation]**](ComponentsschemasContentContentRepresentation.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**comment_summary** | [**ComponentsschemasContentCommentSummary**](ComponentsschemasContentCommentSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


