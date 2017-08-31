# DestinyMilestonesDestinyPublicMilestoneActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_hash** | **int** | The hash identifier of the activity that&#39;s been chosen to be considered the canonical \&quot;conceptual\&quot; activity definition.  This may have many variants, defined herein. | [optional] 
**modifier_hashes** | **list[int]** | The activity may have 0-to-many modifiers: if it does, this will contain the hashesto the DestinyActivityModifierDefinition that defines the modifier being applied. | [optional] 
**variants** | [**list[ComponentsschemasDestinyMilestonesDestinyPublicMilestoneActivityVariant]**](ComponentsschemasDestinyMilestonesDestinyPublicMilestoneActivityVariant.md) | Every relevant variation of this conceptual activity, including the conceptual activity itself,have variants defined here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


