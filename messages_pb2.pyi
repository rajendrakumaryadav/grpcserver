from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestData(_message.Message):
    __slots__ = ["page_name", "client_address", "request_body"]
    PAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    page_name: str
    client_address: str
    request_body: str
    def __init__(self, page_name: _Optional[str] = ..., client_address: _Optional[str] = ..., request_body: _Optional[str] = ...) -> None: ...

class ResponseBody(_message.Message):
    __slots__ = ["status"]
    class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED: _ClassVar[ResponseBody.StatusEnum]
        RECEIVED: _ClassVar[ResponseBody.StatusEnum]
        RECORDED: _ClassVar[ResponseBody.StatusEnum]
        ERROR_WHILE_RECORDING: _ClassVar[ResponseBody.StatusEnum]
    UNDEFINED: ResponseBody.StatusEnum
    RECEIVED: ResponseBody.StatusEnum
    RECORDED: ResponseBody.StatusEnum
    ERROR_WHILE_RECORDING: ResponseBody.StatusEnum
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ResponseBody.StatusEnum
    def __init__(self, status: _Optional[_Union[ResponseBody.StatusEnum, str]] = ...) -> None: ...
