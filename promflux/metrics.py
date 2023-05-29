# Copyright 2023 Lawrence Livermore National Security, LLC and other
# HPCIC DevTools Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

import collections

from prometheus_client import Gauge

from promflux.logger import logger

try:
    import flux
    import flux.job
    import flux.resource
except ImportError:
    logger.exit(
        "Cannot import flux. Please ensure that flux Python bindings are on the PYTHONPATH."
    )


# Keep a global handle so we make it just once
handle = flux.Flux()

# Metrics. Just simple for now (no histograms or counters)
QUEUE_METRIC = Gauge(
    "flux_queue_state_counts",
    "Gauge for the counting job states in the queue.",
    ["state"],
)

# Nodes and resources
NODE_CORES_METRIC = Gauge(
    "flux_node_cores_counts",
    "Gauge for the counting of cores in different states.",
    ["state"],
)

NODE_METRIC = Gauge(
    "flux_node_counts",
    "Total number of nodes in different states",
    ["state"],
)


def update_node_metrics():
    """
    Function to use the flux handle to update node metrics.
    """
    rpc = flux.resource.list.resource_list(handle)
    listing = rpc.get()

    # Update free and up
    NODE_CORES_METRIC.labels(state="up").set(listing.up.ncores)
    NODE_CORES_METRIC.labels(state="free").set(listing.up.ncores)

    # Total number of hosts we can see
    NODE_METRIC.labels(state="up").set(len(listing.up.nodelist))
    NODE_METRIC.labels(state="free").set(len(listing.free.nodelist))


def update_queue_metrics():
    """
    Update metrics for counts of jobs in the queue
    """
    jobs = flux.job.job_list(handle)
    listing = jobs.get()

    # Organize based on states
    states = [x["state"] for x in listing["jobs"]]
    print(states)
    counter = collections.Counter(states)

    # And update the gague based on the label
    for stateint, count in counter.items():
        state = flux.job.info.statetostr(stateint)
        QUEUE_METRIC.labels(state=state).set(count)


# Organize metrics by name so we can eventually support export of custom set (if needed)
metrics = {
    "queue_metrics": update_queue_metrics,
    "node_metrics": update_node_metrics,
}


def update_metrics(selection=None):
    """
    Use flux to get metrics about the current instance queue.
    """
    # We can customize to this selection
    selection = selection or list(metrics)

    # Update the selected metrics
    for name in selection:
        metrics[name]()
