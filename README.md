# mlc-exporter
Experimental Prometheus exporter which scrapes remote JSON metrics collected from [Intel's Memory Latency Checker (MLC) tool](https://www.intel.com/content/www/us/en/developer/articles/tool/intelr-memory-latency-checker.html)

## Usage
Run the following commands from the ``mlc-exporter`` directory:
```
$ make 
$ ./json_exporter --config.file examples/config.yml &
$ python3 -m http.server 8000 &

$ docker run --rm -it -p 9090:9090 -v $PWD/examples/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
Go to http://localhost:9090/graph?g0.range_input=1h&g0.expr=example_value_active&g0.tab=1 to see scraped metrics.
Note: Run them from the mlc-exporter directory

## Helpful Information
- json_exporter runs on ``localhost:7979`` : you can test queries by accessing the /probe endpoint followed by your target parameters (or use curl in CLI)
  - Example: ``http://localhost:7979/probe?module=bandwidths&target=http://localhost:8000/examples/sample_bw_numa.json``
  - Parameters:
    - module: specified in ``config.yml``
    - target: URL of the JSON file to be scraped
- exporter uses [JSONPath formatting](https://kubernetes.io/docs/reference/kubectl/jsonpath/)

## Acknowledgements
Source code: https://github.com/prometheus-community/json_exporter
