# Copyright 2023 Lawrence Livermore National Security, LLC and other
# HPCIC DevTools Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

import os

from prometheus_client import (
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR,
    REGISTRY,
    CollectorRegistry,
)
from prometheus_client.multiprocess import MultiProcessCollector

FLUX_REGISTRY = REGISTRY


def setup_registry(verbose_mode=False):
    """
    Function to call once to set the verbosity of the registry
    """
    global FLUX_REGISTRY
    if "prometheus_multiproc_dir" in os.environ:
        FLUX_REGISTRY = CollectorRegistry()
        MultiProcessCollector(FLUX_REGISTRY)

    # If we want the default streamlined view
    if not verbose_mode:
        print("Removing verbose endpoints...")
        FLUX_REGISTRY.unregister(PROCESS_COLLECTOR)
        FLUX_REGISTRY.unregister(PLATFORM_COLLECTOR)

        # gc_collector registers itself as multiple different collectors
        names = set()
        for collector in FLUX_REGISTRY._names_to_collectors:
            if collector.startswith("python_gc"):
                names.add(collector)

        # This should only need to happen once
        for name in names:
            if name in FLUX_REGISTRY._names_to_collectors:
                FLUX_REGISTRY.unregister(FLUX_REGISTRY._names_to_collectors[name])
