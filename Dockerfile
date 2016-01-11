FROM python:2.7.11-wheezy

run apt-get update && apt-get install -y vim curl
run pip install requests
