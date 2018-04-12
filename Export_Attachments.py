#############################################
# Export Attachments python script
# By: @dobrochtaKCI
#############################################

## Summary
#  There are no geoprocessing tools that allow users to export and save all
#      attachments locally. The instructions provided below describe a possible solution.
#  The following script iterates through the entire attachment table of a single
#      feature class and copies all of the attachments (saved as BLOBs, or binary large
#      objects) to file.

import arcpy
from arcpy import da
import os

# Base code and instructions for use come from https://support.esri.com/en/technical-article/000011912
# This script will need to be added to an ArcGIS toolbox to work properly
#     it requires the first parameter to be a table and the second parameter to be a folder


# Input Attachment Table 
inTable = arcpy.GetParameterAsText(0)
# Location folder of output attachments
fileLocation = arcpy.GetParameterAsText(1)


## Add a meaningful name to the attachments
#  1. Add a new field to Attachement table, in this scenario I called the field 'Label'
#  2. join related table and or features back to the attachment table (Start with attachments and move backwards)
#      especially if using a 1:M feature to attachment relationship
#  3. field calculate a label used for each picture using a unique ID or a combination of fields, which will provide the
#      primary label for each picture

# The fields `Label`, `ATTACHMENTID`, and `ATT_NAME` are used to build the final picture filename

# fields DATA, ATTACHMENTID, and ATT_NAME are native to Attachment tables in ArcGIS
with da.SearchCursor(inTable, ['DATA', 'Label','ATTACHMENTID', 'ATT_NAME']) as cursor:
    for item in cursor:
        attachment = item[0]
        filenum = str(item[1]) + "_" +str(item[2])+"_"
        filename = filenum + str(item[3])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment
