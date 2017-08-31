# DestinyDestinyTalentNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_index** | **int** | The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]).CONTENT VERSION DEPENDENT. | [optional] 
**node_hash** | **int** | The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes).Deceptively CONTENT VERSION DEPENDENT.  We have no guarantee of the hash&#39;s immutability between content versions. | [optional] 
**is_activated** | **bool** | If true, the node is activated: it&#39;s current step then provides its benefits. | [optional] 
**step_index** | **int** | The currently relevant Step for the node.  It is this step that has rendering data for the nodeand the benefits that are provided if the node is activated.  (the actual rules for benefits providedare extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don&#39;t have to worryabout a lot of those old Destiny 1 rules.)  This is an index into:DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex] | [optional] 
**materials_to_upgrade** | [**list[ComponentsschemasDestinyDefinitionsDestinyMaterialRequirement]**](ComponentsschemasDestinyDefinitionsDestinyMaterialRequirement.md) | If the node has material requirements to be activated, this is the list of those requirements. | [optional] 
**activation_grid_level** | **int** | The progression level required on the Talent Grid in order to be able to activate this talent node.Talent Grids have their own Progression - similar to Character Level, but in this case it is experiencerelated to the item itself. | [optional] 
**progress_percent** | **float** | If you want to show a progress bar or circle for how close this talent node is to being activate-able, thisis the percentage to show.  It follows the node&#39;s underlying rules about when the progress bar should firstshow up, and when it should be filled. | [optional] 
**hidden** | **bool** | Whether or not the talent node is actually visible in the game&#39;s UI.  Whether you want to show it in your ownUI is up to you!  I&#39;m not gonna tell you who to sock it to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


