import usaddress
import pandas as pd

df = pd.read_csv('/mnt/c/Linux/ucs/Users_input.csv', encoding='latin1')

# df['address_long'] = df['street'].astype(str) + ' ' + df['secondary'].astype(str) + \
#                      ' ' + df['city'].astype(str)  + ' ' + df['state'].astype(str) + \
#                      ' ' + df['zipcode'].astype(str)

df['address_long'] = df['street'].astype(str) + ' ' + df['city'].astype(str) \
                     + ' ' + df['state'].astype(str) + ' ' + df['zipcode'].astype(str)

df['tagged_address'] = None
df['address_type'] = None

for index, row in df.iterrows():
	try:
	    tagged_address, address_type = usaddress.tag(row['address_long'])
	    df.at[index, 'tagged_address'] = tagged_address
	    df.at[index,'address_type'] = address_type
	except usaddress.RepeatedLabelError as e :
	    df.at[index, 'tagged_address'] = e.parsed_string
	    df.at[index, 'address_type'] = "invalid"

df.to_csv('/mnt/c/Linux/ucs/Users_output.csv', encoding='utf8')
