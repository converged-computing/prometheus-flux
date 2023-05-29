FROM fluxrm/flux-sched:focal

# docker build -t promflux .
# docker run -it -p 8080:8080 promflux

LABEL maintainer="Vanessasaurus <@vsoch>"

USER root

# Assuming installing to /usr/local
ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /code
COPY . /code
RUN python3 -m pip install .
ENTRYPOINT ["flux", "start", "prometheus-flux"]
CMD ["start"]
