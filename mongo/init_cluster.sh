#!/usr/bin/env bash

docker exec -it mongocfg1 sh -cx "mongosh < /scripts/config_server.js"
docker exec -it mongors1n1 sh -cx "mongosh < /scripts/shard_01.js"
docker exec -it mongors2n1 sh -cx "mongosh  < /scripts/shard_02.js"
docker exec -it mongos1 sh -cx "mongosh < /scripts/router.js"
docker exec -it mongos1 sh -cx "mongosh < /scripts/db.js"