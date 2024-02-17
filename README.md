Using json_exporter
========================
### Usage

```console
$ make 
$ ./json_exporter --config.file examples/config.yml &
$ python3 -m http.server 8000 &

$ docker run --rm -it -p 9090:9090 -v $PWD/examples/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
Then head over to http://localhost:9090/graph?g0.range_input=1h&g0.expr=example_value_active&g0.tab=1 to see scraped metrics
