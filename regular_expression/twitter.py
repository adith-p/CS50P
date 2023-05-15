# https://twitter.com/OP_SPOILERS2023

import re
url = input("url: ")

if username := re.search(
        r"^https?://?(?:www\.)?twitter\.com/(.+)", url, re.IGNORECASE):

    print(username.group(1))
