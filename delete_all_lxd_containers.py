#!/usr/bin/env python3
""" This script deletes all LXC containers running on a machine

All containers are deleted, including running containers.

The script assumes that the user running the script has non-sudo access to lxc

No dependencies.

The command that is run: lxc delete --force <container_name>.

Author: Ilhaan Rasheed
Date: March 6th, 2018
"""

import json
from pprint import pprint
import subprocess

# Run lxc list command to get JSON output as a string
lxc_output = subprocess.run(["lxc", "list", "-c", "n", "--format=json"],
                            stdout=subprocess.PIPE).stdout.decode('utf-8')

# Load json string output
data = json.loads(lxc_output)

# Create empty list to store LXC Container names
container_names = []
for x in range(len(data)):
    container_names.append(data[x]["name"])

# Run LXD Delete command for each container
for container in container_names:
    subprocess.run(["lxc", "delete", "--force", container])
