# newrelic_api_playground

A place to test the newrelice API.  This is written in Python, which is not my
language, so don't judge.

## Steup

You have to have docker-machine installed and your env set up.  Once you have a
docker client running, run this:

```
./build.sh
```

## Run

There's a few commands that need to be run for docker to do the thing.  So,
we've written them into a `run.sh` script.  Inspect that to see what it is
doing.  Under the covers, the docker container runs `scripts/parse.py`, which
you can view to get a good idea of what's happening.  Buuuut, if you just want
to get some metric data, run this:

```
./run.sh api_key app_id metric_name
```

For example:

```
./run.sh asdfasdfasdfasdfasdfasfd 1234 ActiveRecord/all
```

## Todo

- [ ] allow time to be passed in (right now only gets last 30m of data)
- [ ] store to db for later analysis
- [ ] cron every 30m
