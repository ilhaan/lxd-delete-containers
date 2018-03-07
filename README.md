# lxd-delete-containers

The Python script in this repo can delete all [LXD](https://linuxcontainers.org/lxd/) containers. This script was inspired by the following [Docker](https://www.docker.com/) command that can delete all stopped containers: 
```
docker rm $(docker ps -f status=exited -q)
```
As you may be already aware, the above command finds stopped docker containers and deletes them. As of now, a similar command cannot be run in LXD since it cannot list containers in "quiet" mode (`-q` in the command above - where only numerical IDs of containers are listed, allowing them to be sent to the `rm` command). This can be problematic if you have a large number of containers that are launched and not stopped on a machine, where you have to manually run the container delete command for each container (E.g.: `lxc delete awaited-mallard`). 

The script `delete_all_lxd_containers.py` in this repo can delete **ALL** containers (running or stopped) on a machine. This is the equivalent to running the following command for each container: 
```
lxc delete --force <container_name> 
```

The `--force` option above forces the remove of running containers. 

This has been tested on Ubuntu 16.04. 

## Requirements 
* Python3 
* Ability to run `lxc` without `sudo`

## Instructions
1. Clone this repo and `cd` into the cloned directory. 
2. Make sure you have execute permissions on `delete_all_lxd_containers.py`. You can set this for the current user by running: `chmod u+x delete_all_lxd_containers.py`
3. Run the script: `./delete_all_lxd_containers.py`

After running the script, you will have no LXD containers on your machine as can be seen by running `lxc list`. 
