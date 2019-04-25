import time
from concurrent import futures

import grpc

import datahash
import datahash_pb2
import datahash_pb2_grpc


class DataHashServicer(datahash_pb2_grpc.DataHashServicer):

    def hash_md5(self, request, context):
        response = datahash_pb2.Text()
        response.data = datahash.hash_md5(request.data)
        return response

    def hash_sha256(self, request, context):
        response = datahash_pb2.Text()
        response.data = datahash.hash_sha256(request.data)
        return response


def serve():
    # создаем сервер
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))

    # прикреплям хандлеры
    datahash_pb2_grpc.add_DataHashServicer_to_server(DataHashServicer(), server)

    # запускаемся на порту 6066
    print('Starting server on port 6066.')
    server.add_insecure_port('[::]:6066')
    server.start()

    # работаем час или до прерывания с клавиатуры
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
