# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("/home/prateek/Prateek/Courses/DataScience/Project/", "*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df.to_csv("spotify_music_consolidated.csv")