# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import datahash_pb2 as datahash__pb2


class DataHashStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.hash_md5 = channel.unary_unary(
        '/DataHash/hash_md5',
        request_serializer=datahash__pb2.Text.SerializeToString,
        response_deserializer=datahash__pb2.Text.FromString,
        )
    self.hash_sha256 = channel.unary_unary(
        '/DataHash/hash_sha256',
        request_serializer=datahash__pb2.Text.SerializeToString,
        response_deserializer=datahash__pb2.Text.FromString,
        )


class DataHashServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def hash_md5(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def hash_sha256(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataHashServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'hash_md5': grpc.unary_unary_rpc_method_handler(
          servicer.hash_md5,
          request_deserializer=datahash__pb2.Text.FromString,
          response_serializer=datahash__pb2.Text.SerializeToString,
      ),
      'hash_sha256': grpc.unary_unary_rpc_method_handler(
          servicer.hash_sha256,
          request_deserializer=datahash__pb2.Text.FromString,
          response_serializer=datahash__pb2.Text.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DataHash', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
