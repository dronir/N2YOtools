
# Get next satellite passes from N2YO API

`get_passes.py` is a quick and simple Python code that downloads the next visible passes of a
list of satellites from the [N2YO API]. Currently it just creates a query and returns the JSON
that the API returns.

Requires Python 3 and the `requests` and `toml` packages.

## Usage

Run `python get_passes.py satellites.txt`, with the following

* `satellites.txt` is a file containing the desired satellite IDs, one per line. The file
  `test_list.txt` can be used for testing. It contains the IDs of the International Space
  Station and the AALTO-1 cubesat.

* The file `config.toml` must exist and contain the station coordinates, number of days to look
  up from the current time, and the minimum pass duration (in seconds) to be accepted. See the
  example.

* The file `N2YO_API_KEY.txt` must exist and contain your API key. This is provided on the user
  page when logged in on [N2YO].

[N2YO]: https://www.n2yo.com
[N2YO API]: https://www.n2yo.com/api/
