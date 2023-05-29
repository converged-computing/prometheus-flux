# Prometheus Flux

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![PyPI](https://img.shields.io/pypi/v/prometheus-flux)](https://pypi.org/project/prometheus-flux/)

Export Prometheus metrics about Flux.

🚧️ **under development** 🚧️

This tool is under development and is not ready for production use. It's fairly simple, so documentation
is provided in this README.md. To see the package on pypi:

 - 📦️ [Pypi Package](https://pypi.org/project/prometheus-flux/) 📦️

## Usage

### Install

You can install from pypi or from source:

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install prometheus-flux

# or

$ git clone https://github.com/converged-computing/prometheus-flux
$ cd prometheus-flux
$ pip install
# you can also do "pip install -e ."
```

This will install the executable to your path, which might be your local user bin:

```bash
$ which prometheus-flux
/home/vscode/.local/bin/prometheus-flux
```

Note that the provided [.devcontainer](.devcontainer) includes an environment for VSCode where you have Flux
and can install this and use ready to go!

### Start

You'll want to be running in a Flux instance, as we need to connect to the broker handle.

```bash
$ flux start --test-size=4
```

And then start the server. This will use a default port and host (0.0.0.0:8080) that you can customize
if desired.

```bash
$ prometheus-flux start

# customize the port or host
$ prometheus-flux start --port 9000 --host 127.0.0.1
```

As an example, when Flux is running with no jobs (and default options are used) we can open
the browser to [http://localhost:8080/metrics/](http://localhost:8080/metrics) to see:

```console
# HELP flux_queue_state_counts Gauge for the counting job states in the queue.
# TYPE flux_queue_state_counts gauge
flux_queue_state_counts{state="INACTIVE"} 2.0
# HELP flux_node_cores_counts Gauge for the counting of cores in different states.
# TYPE flux_node_cores_counts gauge
flux_node_cores_counts{state="up"} 16.0
flux_node_cores_counts{state="free"} 16.0
# HELP flux_node_counts Total number of nodes in different states
# TYPE flux_node_counts gauge
flux_node_counts{state="up"} 4.0
flux_node_counts{state="free"} 4.0
```

If you run in `--verbose` mode you'll also see metrics for the server itself:

```bash
$ prometheus-flux start --verbose
```

<details>

<summary>Example Prometheus Data Output</summary>

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 452.0
python_gc_objects_collected_total{generation="1"} 43.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 85.0
python_gc_collections_total{generation="1"} 7.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="10",version="3.8.10"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.24461056e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 3.4168832e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.68539579014e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.22
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 13.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP flux_queue_state_counts Gauge for the counting job states in the queue.
# TYPE flux_queue_state_counts gauge
flux_queue_state_counts{state="INACTIVE"} 2.0
# HELP flux_node_cores_counts Gauge for the counting of cores in different states.
# TYPE flux_node_cores_counts gauge
flux_node_cores_counts{state="up"} 16.0
flux_node_cores_counts{state="free"} 16.0
# HELP flux_node_counts Total number of nodes in different states
# TYPE flux_node_counts gauge
flux_node_counts{state="up"} 4.0
flux_node_counts{state="free"} 4.0
```

</details>

Note that we are testing this to help with an autoscaler for Kubernetes, meaning
the metrics will be used to determine if we should make a request to scale or shrink
a cluster.

### Docker

We have a docker container, which you can customize for your use case, but it's more intended to
be a demo. You can either build it yourself, or use our build.

```bash
$ docker build -t promflux .
$ docker run -it -p 8080:8080 promflux
```
or

```bash
$ docker run -it -p 8080:8080 ghcr.io/converged-computing/prometheus-flux
```

You can then open up the browser at [http://localhost:8080/metrics/](http://localhost:8080/metrics) to see
the metrics!

## 😁️ Contributors 😁️

We use the [all-contributors](https://github.com/all-contributors/all-contributors)
tool to generate a contributors graphic below.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://vsoch.github.io"><img src="https://avatars.githubusercontent.com/u/814322?v=4?s=100" width="100px;" alt="Vanessasaurus"/><br /><sub><b>Vanessasaurus</b></sub></a><br /><a href="https://github.com/converged-computing/prometheus-flux/commits?author=vsoch" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/prometheus-flux/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/prometheus-flux/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/prometheus-flux/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614
