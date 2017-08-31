# DestinyMilestonesDestinyPublicMilestoneQuest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quest_item_hash** | **int** | Quests are defined as Items in content.  As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest.  It will have pointers to all of the stepsin the quest, and display information for the quest (title, description, icon etc)Individual steps will be referred to in the Quest item&#39;s DestinyInventoryItemDefinition.setDataproperty, and themselves are Items with their own renderable data. | [optional] 
**challenges** | [**list[ComponentsschemasDestinyMilestonesDestinyPublicMilestoneChallenge]**](ComponentsschemasDestinyMilestonesDestinyPublicMilestoneChallenge.md) | For the given quest there could be 0-to-Many challenges: mini queststhat you can perform in the course of doing this quest, that may grant you rewards and benefits. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


