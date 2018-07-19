#!/usr/bin/env python


import sys
import datetime

import pandas as pd

def get_mean_price(filename):
    """
    function to get the mean price of the wines rounded to 4 decimal places
    """
    wine = pd.read_csv(filename)
    mean_price = wine['price'].mean()
    return round(mean_price, 4)


def get_country(filename, country):
    """
    Do a simple analysis per country
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    country: str
        Country to be used to subset

    Returns:
    -----
    fname: st
        Path to the created data set
    """

    # Load table
    wine = pd.read_csv(filename)

    # Use the country name to subset data
    subset_country = wine[wine['country'] == country ].copy()
    subset_country.reset_index(drop=True, inplace=True) 

    # Constructing the fname
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    fname = f'data/processed/{today}-winemag_{country}.csv'

    # Saving the csv
    subset_country.to_csv(fname, index =False)
    
    print(fname) # prints the fname from here
    
    return(subset_country) # returns the data frame


if __name__ == '__main__':
    filename = sys.argv[1]
    country = sys.argv[2]
    print(f'Subsetting: {filename}')
    print(f'Country searched: {country}')

    print(get_country(filename, country))
