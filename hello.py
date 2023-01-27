#!/usr/bin/env python3

import os
import json

# print("Content Type: application/json")
print("Content Type: text/html")
print()
# print(json.dumps(dict(os.environ), indent=2))
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")
