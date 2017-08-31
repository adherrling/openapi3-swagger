# DestinyDefinitionsDirectorDestinyActivityGraphDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition.md) | These represent the visual \&quot;nodes\&quot; on the map&#39;s view.  These are the activities youcan click on in the map. | [optional] 
**art_elements** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition.md) | Represents one-off/special UI elements that appear on the map. | [optional] 
**connections** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition.md) | Represents connections between graph nodes.  However, it lacks context that we&#39;d need to make good use of it. | [optional] 
**display_objectives** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.md) | Objectives can display on maps, and this is supposedly metadata for that.  I have not had the time toanalyze the details of what is useful within however: we could be missing important data to make this work.Expect this property to be expanded on later if possible. | [optional] 
**display_progressions** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition.md) | Progressions can also display on maps, but similarly to displayObjectives we appear to lack some requiredinformation and context right now.  We will have to look into it later and add more data if possible. | [optional] 
**linked_graphs** | [**list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphDefinition]**](ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphDefinition.md) | Represents links between this Activity Graph and other ones. | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


