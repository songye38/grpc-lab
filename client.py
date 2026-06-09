import grpc

from generated import user_pb2
from generated import user_pb2_grpc


# 연결 만듦
channel = grpc.insecure_channel(
    "localhost:50051"
)

# 설계도를 기반으로 만든 뼈대
stub = user_pb2_grpc.UserServiceStub(
    channel
)

# 실제 연결 후에 요청을 보내면 서버에서 응답이 돌아옴
response = stub.GetUser(
    user_pb2.UserRequest(id=1)
)

print(response.id)
print(response.name)