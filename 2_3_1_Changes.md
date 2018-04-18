UG Changes

##Found in Prod schema

These appear to have been updated by Kerry recently

    INSPECTION TYPE
    COM_RESPONSE
    FIRM_NAME
    SURFACE_CONDITION
    OCCUPAT_HAZARD_COM
    PLAN_MATCH_COMMENT
    OTHER_INSP_TYPE_DESC
    STRUCTURE_ACCESS_CONDITION


## Alter

Made the following alterations

Old Field Name | New Field Name | New Field Length
-- | -- | --
UNDERGROUND_YN | FO_UNDERGROUND_YN |  
OT_OTHER_DESCRIPTION | OTHER_INSP_TYPE_DESC | 50
PLAN_MATCH_COMM | PLAN_MATCH_COMMENT |  
OC_HAZ_COM | OCCUPAT_HAZARD_COM |  
COM_RESPON | COM_RESPONSE |  
FIRM | FIRM_NAME | 50

## Remove

Removed the following fields and tables

- BMP_Inspect_ID
- Issue tracker table
- all UG fields


## Add

Beta test: add the EXIF fields to the overall BMP photos.
