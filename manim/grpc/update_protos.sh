#!/bin/sh

python \
    -m grpc_tools.protoc \
    -I./proto \
    --python_out=./gen \
    --grpc_python_out=./gen \
        ./proto/helloworld.proto \
        ./proto/frameserver.proto \
        ./proto/renderserver.proto
