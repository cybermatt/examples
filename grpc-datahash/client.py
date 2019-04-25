import grpc

import datahash_pb2
import datahash_pb2_grpc


# открываем канал и создаем клиент
channel = grpc.insecure_channel('localhost:6066')
stub = datahash_pb2_grpc.DataHashStub(channel)

# текст для хеширования
text = 'Scio me nihil scire'

# запрос за md5
to_md5 = datahash_pb2.Text(data=text)
response = stub.hash_md5(to_md5)
print(response.data)

# запрос за ha256
to_sha256 = datahash_pb2.Text(data=text)
response = stub.hash_sha256(to_sha256)
print(response.data)
