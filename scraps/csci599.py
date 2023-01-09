# -------------------------------------------------------------------------------------------------
#   To run this program the following libraries are required:
#   download the source code from https://github.com/vgrem/Office365-REST-Python-Client.git
#   open command prompt
#   type 'pip install Office365-REST-Python-Client', press enter
#   after that install finishes, type 'pip install requests', press enter
#   after that install finishes, type 'pip install pandas', press enter
#   next, 'pip install azure-storage-blob', enter
#   wait for the installation to finish, then restart your IDE
# -------------------------------------------------------------------------------------------------

import pandas as pd

from os import getenv
from azure.storage.blob import BlobServiceClient

# -------------------------------------------------------------------------------------------------
#   Create a connection with Azure storage container (staging area)
# -------------------------------------------------------------------------------------------------
azure_connection_string = 'DefaultEndpointsProtocol=https;AccountName=csci599;AccountKey=5pvO4q5tRwnLz87VDtJM4i07QEY8ewSwwCxqqfqSwPrc/wzjfOsFtmOyv7rl6+7fXZO96ORO7WpA+AStAkKckA==;EndpointSuffix=core.windows.net'

blob_service_client = BlobServiceClient.from_connection_string(
    getenv(azure_connection_string))

# -------------------------------------------------------------------------------------------------
#   The files are extracted from their location on Microsoft Teams / Sharepoint using a link
#   to the folder and a link to the specific file
# -------------------------------------------------------------------------------------------------

# Teams / Sharepoint Folder Links:
cyverse = r'https://emailuscupstateedu-my.sharepoint.com/:f:/g/personal/klavigne_email_uscupstate_edu/Epiqit7AySJKgWIcABAvj3IBhMPmdEvYE-esPfLeSB_BqQ?e=2vPfUz'
ofs_hysets = r'https://emailuscupstateedu-my.sharepoint.com/:f:/g/personal/klavigne_email_uscupstate_edu/EpDN_S3x6BtFt6qR_SC9tw0BCQ521959xH3rFwvJl-pgPw?e=JDzOYy'

# File Specific Teams / Sharepoint Links:
conus_subbasin_1km = r'https://emailuscupstateedu-my.sharepoint.com/:x:/g/personal/klavigne_email_uscupstate_edu/EY29khuvItlLjqBfcHOor-UBLWIbU7J3IccNZJ41pnkpvQ?e=0cQUZ5'
conus_subbasin_250m = r'https://emailuscupstateedu-my.sharepoint.com/:x:/g/personal/klavigne_email_uscupstate_edu/EX5q699o_S5El0QHY_ApHwMB6LjLHz9enuavxVdxgy-D9g?e=4oXCCo'
hyset_watershed_properties = r'https://emailuscupstateedu-my.sharepoint.com/:t:/g/personal/klavigne_email_uscupstate_edu/ESo87nrLn9FHo75wTdI1CvsBxzwRpAg9Or_zXZZTVHV2kA?e=O51sQI'
hyset_elevation_bands_100m = r'https://emailuscupstateedu-my.sharepoint.com/:x:/g/personal/klavigne_email_uscupstate_edu/EWjK3504eCxApkdNeIyNC0kBHEZJmX1uGQPMeUtokpK2PQ?e=3nZR2e'

# -------------------------------------------------------------------------------------------------
#   The files are put into an Azure storage container (staging area)
# -------------------------------------------------------------------------------------------------

#