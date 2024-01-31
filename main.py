import logging
import os
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
    grpc_port = os.getenv('PORT', '50051')
    host_name = os.getenv('HOSTNAME', 'grpcserver')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpb.add_RequestHandlerServicer_to_server(RequestHandlerServer(), server)
    server.add_insecure_port(f':{grpc_port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        logging.warning("Running the GRPC server on port 50051")
        main()
    except KeyboardInterrupt as e:
        logging.warning("Closing the application...")
