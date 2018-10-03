import requests
from pprint import pprint
from sys import argv

# Load N2YO API key from file (get your own key by registering at N2YO.com)
API_KEY = open("N2YO_API_KEY.txt").read().strip()
key_info = {"apiKey" : API_KEY}

# Parameters of the observer and desired observation arcs (one day in the future, 
# minimum 60 second pass).
base_params = {
    "observer_lat" : 60.2172,
    "observer_lng" : 24.3946,
    "observer_alt" : 74.042,
    "days" : 1,
    "min_visibility" : 60
}

# URL templates to the N2YO API, used to produce the query URL below
BASE_URL = "https://www.n2yo.com/rest/v1/satellite/"
TEMPLATE = "visualpasses/{id:d}/{observer_lat:.5f}/{observer_lng:.5f}/{observer_alt:2f}/{days:d}/{min_visibility:d}"

def parse_query(params, debug=False):
    " Produce URL from parameter dictionary."
    URL = "".join([BASE_URL, TEMPLATE.format(**params)])
    if debug:
        print("Created query: {}".format(URL))
    return URL

def retrieve_data(QUERY_URL, debug=False):
    "Retrieve data from given URL."
    if debug:
        print("Requesting data from: {}".format(QUERY_URL))
    r = requests.get(QUERY_URL, params=key_info)
    if debug and r.status_code == requests.codes.ok:
        print("Success.")
        return r.json()
    elif debug:
        print("Failed (status code {})!".format(r.status_code))
        return ""

def read_ids(filename, debug=False):
    "Read a list of satellite ID numbers from given filename."
    IDs = []
    if debug:
        print("Parsing file: {}".format(filename))
    with open(filename, "r") as f:
        for line in f:
            ID = int(line.strip())
            if debug:
                print(ID)
            IDs.append(ID)
    return IDs

def get_single(ID, debug=False):
    "Retrieve data of a single satellite based on ID."
    query_params = base_params.copy()
    query_params["id"] = ID
    if debug:
        print("Query parameters:")
        print(query_params)
    URL = parse_query(query_params, debug)
    data = retrieve_data(URL, debug)
    return data

def get_all(filename, debug=False):
    "Retrieve data of all satellites in a list of IDs."
    IDs = read_ids(filename, debug)
    all_data = [get_single(ID, debug) for ID in IDs]
    return all_data

if __name__=="__main__":
    fname = argv[1]
    data = get_all(fname, debug=True)
    for result in data:
        pprint(result)
