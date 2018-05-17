// First set the fields as variables
// Then set a flag to true if the field is not null
// then return flags

var etl_issue_field = $feature["FLD_ETL_ISSUES"]
var etl_spatial_field = $feature["FLD_ETL_SPATIAL_ISSUES"]

var etl_issue_flag = IIf(IsEmpty(etl_issue_field), false, true)
var etl_spatial_flag = IIf(IsEmpty(etl_spatial_field), false, true)

When(etl_issue_flag, 'etl_issue', etl_spatial_flag, 'etl_spatial', 'no_flag')
