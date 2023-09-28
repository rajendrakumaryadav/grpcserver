from concurrent import futures

import grpc

import messages_pb2 as pb
import messages_pb2_grpc as gpb


class RequestHandlerServer(gpb.RequestHandlerServicer):
    def HandleRequest(self, request, context):
        print("Message Received: %s, content: %s" % (request, context))
        context.set_code(grpc.StatusCode.OK)
        context.set_details("Data Received and all operations completed")
        return pb.ResponseBody(status=pb.ResponseBody.StatusEnum.RECORDED)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpb.add_RequestHandlerServicer_to_server(RequestHandlerServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        print("Running the GRPC server on port 50051")
        main()
    except KeyboardInterrupt as e:
        print("Closing the application...")
