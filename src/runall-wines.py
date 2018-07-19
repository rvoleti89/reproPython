import importlib
import sys
import recipy

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')



if __name__ == '__main__':
    filename = sys.argv[1]
    country = sys.argv[2]
    
    print(filename)
    print(country)
    interim_data = subset.process_data_GBP(filename)
    print(interim_data)
    print(plotwines.create_plots(interim_data))
    
    
    print(f'Subsetting: {filename}')
    print(f'Country searched: {country}')

    print(country_sub.get_country(filename, country))
    