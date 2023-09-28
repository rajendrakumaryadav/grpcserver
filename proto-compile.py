from grpc_tools import protoc


def main():
    protoc.main(['-I./', './messages.proto', "--python_out=.", "--grpc_python_out=.", "--pyi_out=."])


if __name__ == '__main__':
    main()
