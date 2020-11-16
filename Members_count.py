import pandas as pd
datafile = '/Users/Alessandro/Desktop/1.xlsx'
df = pd.read_excel(datafile, header=8, index_col='Member Name')
df = df[df.columns.drop(list(df.filter(regex='Unnamed:')))]

resigned = 0
suspended = 0
non_signing = 0

for x in df['Status']:
    if x == 'Resigned':
        resigned += 1
    elif x == 'Suspended':
        suspended += 1
    elif x == 'Non-Signing':
        non_signing += 1
        
print('Members resigned = '+ str(resigned))
print('Members suspended = '+ str(suspended))
print('Members non-signing = ' + str(non_signing))


"""
NON-LOOPED CODE V. 
resigned_bool = df[df['Status'] == 'Resigned']
resigned_col = resigned_bool['Status']
resigned_count = resigned_col.count()

print('Members resigned = ' + str(resigned_count))

suspended_bool = df[df['Status'] == 'Suspended']
suspended_col = suspended_bool['Status']
suspended_count = suspended_col.count()

print('Members suspended = ' + str(suspended_count))

non_signing_bool = df[df['Status'] == 'Non-Signing']
non_signing_col = non_signing_bool['Status']
non_signing_count = non_signing_col.count()

print('Members non signing = ' + str(non_signing_count))"""