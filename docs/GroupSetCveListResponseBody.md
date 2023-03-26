# GroupSetCveListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_ids** | **List[str]** | advisoryIDs of cve | [optional] 
**created_at** | **datetime** | created time | 
**cve_id** | **str** | Cve ID string of cve | 
**cwes** | [**List[CweResponseBody]**](CweResponseBody.md) | cwes of cve | 
**groups** | [**List[GroupResponseBody]**](GroupResponseBody.md) | Groups including this cve | 
**has_exploit** | **bool** | hasExploit of cve | [optional] 
**has_mitigation** | **bool** | hasMitigation of cve | [optional] 
**is_owasp_top_ten2017** | **bool** | isOwaspTopTen2017 of cve | 
**max_v2** | **float** | maxV2 of cve | 
**max_v3** | **float** | maxV3 of cve | 
**score_v2s** | **Dict[str, float]** | cvss v2 scores of cve | 
**score_v3s** | **Dict[str, float]** | cvss v3 scores of cve | 
**title** | **str** | Title of cve | 
**topic_count** | **int** | topicCount of cve | 
**topic_last_updated_at** | **str** | topicLastUpdatedAt of cve (default value is \&quot;\&quot;) | 
**updated_at** | **datetime** | updated time | 
**vector_v2s** | **Dict[str, str]** | cvss v2 vectors of cve | 
**vector_v3s** | **Dict[str, str]** | cvss v3 vectors of cve | 

## Example

```python
from openapiclient.models.group_set_cve_list_response_body import GroupSetCveListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetCveListResponseBody from a JSON string
group_set_cve_list_response_body_instance = GroupSetCveListResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetCveListResponseBody.to_json()

# convert the object into a dict
group_set_cve_list_response_body_dict = group_set_cve_list_response_body_instance.to_dict()
# create an instance of GroupSetCveListResponseBody from a dict
group_set_cve_list_response_body_form_dict = group_set_cve_list_response_body.from_dict(group_set_cve_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


