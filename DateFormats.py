#!/usr/local/bin/python3

import pandas as pd

df = pd.DataFrame({
'id':[1,2,3,4,5],
'mydate': ['2001-04-20', '2023-02-28', '5/22/2019', '17-DEC-16', '2005-04-19'],
''
})


#blah = df['mydate']
#result = blah.str.match(pat = '^\d{4}-\d{2}-\d{2}')
#result

#show me date values converted from original data
df.apply(lambda d: pd.to_datetime( d['mydate']) , axis=1)

#add new date column based on original data
df.insert(len(df.columns),'NewDateColumnName', df.apply(lambda d: pd.to_datetime( d['mydate']), axis=1).values)

df
