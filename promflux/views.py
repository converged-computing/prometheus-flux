# Copyright 2023 Lawrence Livermore National Security, LLC and other
# HPCIC DevTools Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.requests import Request
from starlette.responses import Response

import promflux.metrics as metrics
import promflux.registry as registry


def metrics_view(request: Request) -> Response:
    """
    The metrics registry view handles processing requests.

    Prometheus is designed to just have one /metrics endpoint that delivers single-line
    metrics. This function provides that.
    """
    # This seems to be a standard
    # https://github.com/prometheus/client_python/blob/1b9709e3322c17f342e991178e092d1f49ad8cc4/prometheus_client/multiprocess.py#L25
    # Update to get latest metrics
    metrics.update_metrics()
    return Response(
        generate_latest(registry.FLUX_REGISTRY),
        headers={"Content-Type": CONTENT_TYPE_LATEST},
    )
