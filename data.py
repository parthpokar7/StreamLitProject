import pandas as pd

def getData():
    data = {
        "Ads":[1000,2000,3000,4000,5000],
        "Sales":[5000,10000,15000,20000,25000]
    }

    return pd.DataFrame(data)