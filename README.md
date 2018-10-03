
# Get next satellite passes from N2YO API

Quick and simple Python code that downloads the next visible passes of a list of satellites
from [n2yo.com]. Currently it just formulates a query and returns the JSON that the API
returns.

Requires Python 3 and the `requests` package.

## Usage

Run `python get_passes.py satellites.txt`, where `satellite.txt` is a file containing the
desired satellite IDs, one per line. The file `test_list.txt` can be used for testing. It
contains the IDs of the International Space Station and the AALTO-1 cubesat.

You need to have your own API key in the file `N2YO_API_KEY.txt`. This is provided on the
user page when logged in on [n2yo.com]

