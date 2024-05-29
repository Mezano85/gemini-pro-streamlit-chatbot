FROM alpine:latest as tini

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

ARG TARGETARCH
# download tini
RUN wget https://github.com/krallin/tini/releases/download/v0.19.0/tini-${TARGETARCH} -O /tini && \
    chmod +x /tini

FROM mambaorg/micromamba:latest AS runtime
# get tini
COPY --from=tini /tini /tini

USER root
RUN apt-get update && apt-get install -y build-essential

# install dependencies
ENV PYTHON_VERSION=3.10.5
RUN micromamba install -y -c conda-forge -n base \
    python==${PYTHON_VERSION} \
    pipenv==2023.12.1 \
    gcc==12.3.0 \
    && micromamba clean -a -y

ARG MAMBA_DOCKERFILE_ACTIVATE=1
# install environment
ARG pipenv_flags=""
COPY requirements.txt ./
# install pipenv packages
RUN pip install -r requirements.txt
# prepare deploy path
ENV SRC_PATH=/app/src/
ENV PYTHONPATH $SRC_PATH:$PYTHONPATH
WORKDIR $SRC_PATH

# get files
ARG src=./
COPY --chown=$MAMBA_USER $src $src

ENTRYPOINT ["/tini", "--", "/usr/local/bin/_entrypoint.sh", "pipenv", "run"]