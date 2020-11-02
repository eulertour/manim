#!/bin/sh

poetry run python \
    -m grpc_tools.protoc \
    -I./proto \
    --python_out=./gen \
    --grpc_python_out=./gen \
        ./proto/frameserver.proto \
        ./proto/renderserver.proto \
        ./proto/helloworld.proto
