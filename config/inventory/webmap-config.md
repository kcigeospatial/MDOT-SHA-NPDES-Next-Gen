## Config steps on web map

### 1 Add data to map

Add the inventory service

### 2 Rename all Contents

Title-cased layers look better.

- Structures
- BMP Centroid
- Treatment Pipe
- Conveyance
- SWMFAC
- Structure Drainage Area
- SWMFAC Drainage Area
- Structure Issue
- Contract
- Field Screening Site
- Metadata
- Owner


### 3 Set background/non-edit layers

Disable editing and hide the popups for these layers

- Both _Drainage area_ features (SWMFAC and STRUCTURE)
- BMP Centroid

### 4 Enable popups on all related tables

### 5 Set zoom visibility

Layer                     | Don't show beyond |
| :---------------------- | :---------------- |
| Structures              | 1:10,000          |
| BMP Centroid            | 1:24,000          |
| Treatment Pipe          | 1:10,000          |
| Conveyance              | 1:10,000          |
| SWMFAC                  | 1:24,000          |
| Structure Drainage Area | 1:24,000          |
| SWMFAC Drainage Area    | 1:24,000          |

### 6 Add bookmarks

- SHA Hanover
- Any test sites

### 7 Metadata

- Good summary
- Add thumbnail

### 8 Search

Add search in the web map config.

1. Open the web map content page
2. Settings tab
3. At the bottom under _Find Locations_ click _By Layer_
4. Click _Add Layer_ and add the following:

| Layer          | Search Field     | Search Type    |
| :------------- | :--------------- | :------------- |
| SWMFAC         | SWMFAC Number    | Contains       |
| Conveyance     | Conveyance ID    | Contains       |
| Structures     | Structure Number | Contains       |

6. Change the _Hint text_ to "SWFAC No., Conveyance ID, Structure No., or Address"

### Other

- Basemap selection
- Separate offline version if basemap is not supported
