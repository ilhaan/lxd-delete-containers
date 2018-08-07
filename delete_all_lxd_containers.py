#!/usr/bin/env python3
""" This script deletes all LXC containers and/or images.

All containers and images are deleted. This incldes running containers
and OS images.

The script assumes that the user running the script has non-sudo access
to lxc

No dependencies.

Author: Ilhaan Rasheed
"""

import json
from pprint import pprint
import subprocess
import argparse
import sys


def get_args():
    """Get args from command line"""

    parser = argparse.ArgumentParser(description='Delete LXC Containers and \
                                                  Images')
    parser.add_argument('-c', '--containers', dest='container_delete',
                        default=False, action='store_true',
                        help='Enable this to delete all LXC containers')
    parser.add_argument('-i', '--images', dest='image_delete', default=False,
                        action='store_true',
                        help='Enable this to delete all LXC images')
    args = parser.parse_args()

    if args.container_delete is False and args.image_delete is False:
        print("You need to enable either container or images or both. \
               Use --help for more info.")
        sys.exit()
    else:
        return (args.container_delete, args.image_delete)


def container_delete():
    """Function that deletes all containers"""

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


def image_delete():
    """Function that deletes all images"""

    # Run lxc image list command to get JSON output as a string
    lxc_output = subprocess.run(["/snap/bin/lxc", "image", "list", "--format=json"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8')

    # Load json string output
    data = json.loads(lxc_output)

    # Create empty list to store LXC Image fingerprints
    image_fingerprints = []
    for x in range(len(data)):
        image_fingerprints.append(data[x]["fingerprint"])

    # Run LXD Image Delete command for each container
    for image in image_fingerprints:
        subprocess.run(["lxc", "image", "delete", image])


if __name__ == '__main__':
    (container, image) = get_args()

    if container:
        container_delete()
    if image:
        image_delete()
