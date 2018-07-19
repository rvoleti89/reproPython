import importlib

country = importlib.import_module('.data.03_country-subset', 'src')

interim_data = "data/interim/2018-07-18-winemag_priceGBP.csv"
processed_data = "data/processed/2018-07-18-winemag_Chile.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
