# %% [markdown]
# ## Web Scrapping

# %%
import requests as rq
import json
import pandas as pd
import numpy as np

# %%
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

# %%
URL = "https://www.zapimoveis.com.br/venda/casas/?pagina="
number_of_pages = 101
pages = [str(i) for i in range(1, number_of_pages)]


# %%
def process_json(json_dict):
    results_listining = json_dict["results"]["listings"]
    for i, house in enumerate(results_listining):
        parking_spaces = results_listining[i]["listing"]["parkingSpaces"]
        results_listining[i]["listing"]["parkingSpaces"] = (
            int(parking_spaces[0]) if parking_spaces else np.nan
        )
        suites = results_listining[i]["listing"]["suites"]
        results_listining[i]["listing"]["suites"] = int(suites[0]) if suites else np.nan
        bathrooms = results_listining[i]["listing"]["bathrooms"]
        results_listining[i]["listing"]["bathrooms"] = (
            int(bathrooms[0]) if bathrooms else np.nan
        )
        bedrooms = results_listining[i]["listing"]["bedrooms"]
        results_listining[i]["listing"]["bedrooms"] = (
            int(bedrooms[0]) if bedrooms else np.nan
        )
        usable_areas = results_listining[i]["listing"]["usableAreas"]
        results_listining[i]["listing"]["usableAreas"] = (
            int(usable_areas[0]) if usable_areas else np.nan
        )

        total_areas = results_listining[i]["listing"]["totalAreas"]
        results_listining[i]["listing"]["totalAreas"] = (
            int(total_areas[0]) if total_areas else np.nan
        )
        iptu = results_listining[i]["listing"]["pricingInfo"]["yearlyIptu"]
        results_listining[i]["listing"]["pricingInfo"]["yearlyIptu"] = (
            float(iptu.replace("R$ ", "").replace(".", "")) if iptu else np.nan
        )

    json_dict["results"]["listings"] = results_listining
    return json_dict


# %%
from tqdm.auto import tqdm


def get_house_info(html: str):
    json_start = html.find('"results":{"listings"')
    json_end = html.find(";(function(){var s")

    json_str = "{" + html[json_start:json_end]

    json_dict = json.loads(json_str)
    json_dict = process_json(json_dict)
    flattened_json = pd.json_normalize(json_dict["results"]["listings"])
    return flattened_json


def get_page_info(url: str, pages: list, columns: list):
    result = []
    for page in tqdm(pages):
        response = rq.get(URL + page, headers=HEADERS)
        if response.status_code == 200:
            html = str(response.text)
            try:
                result.append(get_house_info(html))
            except Exception as e:
                print()

    data = pd.concat(result, ignore_index=True)
    if columns:
        data = data[columns]

    return data


# %% [markdown]
# #### Extract Data

# %%
raw_data = get_page_info(URL, pages, [])

# %% [markdown]
# #### Save Data

# %%
raw_data.to_csv(f"raw_data_{len(raw_data)}.csv", index=False)

# %%
