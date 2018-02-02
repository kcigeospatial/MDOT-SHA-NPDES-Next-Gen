# Inventory Notes
via email by BR dated 30 Jan 2018

## Feature Classes and Tables for Inventory

### Feature Class

* STRUCTURES
* CONVEYANCE
* SWMFAC
* BMP_CENTROID

### Table
* CONTRACT
* DITCH
* END_HEADWALL
* INLET
* MANHOLE_CON
* METADATA_INFO
* PIPES
* PUMPSTN
* STRUCTURE_ISSUE
* SWMRISER
* WEIR

## Editing
The only fields that **cannot** be edited for inventory are:

* Any foreign or primary GUID keys (ie, _ID)
* SWMFAC.DESIGNATION
* SWMFAC.DESIGN_SUB
* SWMFAC.PLANDATE
* SWMFAC.FEAT_STATUS
* SWMFAC.OWNER_ID

## Backend update possible
Field that can be populated on the back end using overlay source GIS include:

* MD_WSHED
* MD_MSHOP
* MD_DISTRICT
* PLAN_IMP_AREA
* PLAN_DRAN_AREA
* LEGISLATIVE_DISTRICT
* CONGRESSIONAL_DISTRICT
* WATERSHED_8DIGIT

## IDDE Specific Tables
Some of these are under review for update. See the [idde](https://github.com/kcigeospatial/MDOT-SHA-NPDES-Next-Gen/issues?q=is%3Aissue+is%3Aopen+label%3Aidde) label in this repo.

* FLDSC_SITE
* INSPECTION
* FLOW_CHAR
* FILE_ATTACH_STR
