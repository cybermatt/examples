init:
	pip install grpcio
	pip install grpcio-tools

genRPC:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. datahash.proto

run_server:
	python server.py

.PHONY: init genRPC run_server
