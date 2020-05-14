#!/bin/bash

if [ $# -gt 0 ]; then
  echo $1
  export IMAGE_NAME=$1

else
  echo 'Usage: ./build_and_push.sh <IMAGE_NAME>'
  exit 1

fi


sudo docker build -t ${IMAGE_NAME} .

sudo docker tag ${IMAGE_NAME} ${IMAGE_NAME}:latest

sudo docker push ${IMAGE_NAME}:latest