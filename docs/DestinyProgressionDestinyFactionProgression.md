# DestinyProgressionDestinyFactionProgression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction_hash** | **int** | The hash identifier of the Faction related to this progression.  Use it to look up the DestinyFactionDefinitionfor more rendering info. | [optional] 
**progression_hash** | **int** | The hash identifier of the Progression in question.  Use it to look up the DestinyProgressionDefinition in static data. | [optional] 
**daily_progress** | **int** | The amount of progress earned today for this progression. | [optional] 
**daily_limit** | **int** | If this progression has a daily limit, this is that limit. | [optional] 
**weekly_progress** | **int** | The amount of progress earned toward this progression in the current week. | [optional] 
**weekly_limit** | **int** | If this progression has a weekly limit, this is that limit. | [optional] 
**current_progress** | **int** | This is the total amount of progress obtained overall for thisprogression (for instance, the total amount of Character Level experience earned) | [optional] 
**level** | **int** | This is the level of the progression (for instance, the Character Level). | [optional] 
**level_cap** | **int** | This is the maximum possible level you can achieve for this progression (for example, the maximumcharacter level obtainable) | [optional] 
**step_index** | **int** | Progressions define their levels in \&quot;steps\&quot;.  Since the last step may be repeatable, the user maybe at a higher level than the actual Step achieved in the progression.  Not necessarily useful, butpotentially interesting for those cruising the API.  Relate this to the \&quot;steps\&quot; property of the DestinyProgressionto see which step the user is on, if you care about that.  (Note that this is Content Version dependent sinceit refers to indexes.) | [optional] 
**progress_to_next_level** | **int** | The amount of progression (i.e. \&quot;Experience\&quot;) needed to reach the next level of this Progression.Jeez, progression is such an overloaded word. | [optional] 
**next_level_at** | **int** | The total amount of progression (i.e. \&quot;Experience\&quot;) needed in order to reach the next level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


