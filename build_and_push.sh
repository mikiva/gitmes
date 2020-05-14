#!/bin/bash


sudo docker build -t ivahl/gitmes .

sudo docker tag ivahl/gitmes ivahl/gitmes:latest

sudo docker push ivahl/gitmes:latest