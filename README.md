# Zookeeper: Getting Started

## 1: Run local instance

docker run  -d --rm --name zookeeper -p 2181:2181 fabric8/zookeeper

## 2: Connect via CLI (inside the container)

docker exec -it _CONTAINER_ID_ bash
/opt/zookeeper/bin/zkCli.sh

## 4: Play with znodes

create /bla "test_data"

ls /
