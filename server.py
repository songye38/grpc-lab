from concurrent import futures
import grpc

from generated import user_pb2
from generated import user_pb2_grpc, user_pb2


# 상속받아서 실제 구현
class UserService(user_pb2_grpc.UserServiceServicer):

    def GetUser(self, request, context):

        print("요청 받은 id:", request.id)

        return user_pb2.UserResponse(
            id=request.id,
            name="song"
        )
    


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(),
        server
    )

    server.add_insecure_port("[::]:50051")

    server.start()

    print("gRPC Server Running...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()