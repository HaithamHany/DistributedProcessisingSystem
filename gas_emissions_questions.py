import pandas as pd
data = pd.read_csv('asset_cropland-fires_emissions.csv')

# what are the emission factors values were considered between the period of 2015 and 2018?
gas_factors = data[data['start_time'].str.contains('2015|2016|2017|2018')]
gas_factors['emissions_factor'].unique()

# country with the highest average emissions quantity
emissions_avg = data.groupby(['asset_name']).mean()
emissions_avg[emissions_avg['emissions_quantity']==emissions_avg['emissions_quantity'].max()]

# What are the types of gases that USA emits?
gas_types = data[data['iso3_country'] == 'USA']
gas_types['gas'].unique()

# how many times was the data modified?
data['created_date'].unique().size