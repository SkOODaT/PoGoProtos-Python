# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/check_share_ex_raid_pass_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import share_ex_raid_pass_result_pb2 as pogoprotos_dot_enums_dot_share__ex__raid__pass__result__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/check_share_ex_raid_pass_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGpogoprotos/networking/responses/check_share_ex_raid_pass_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x30pogoprotos/enums/share_ex_raid_pass_result.proto\"W\n\x1c\x43heckShareExRaidPassResponse\x12\x37\n\x06result\x18\x01 \x01(\x0e\x32\'.pogoprotos.enums.ShareExRaidPassResultb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_share__ex__raid__pass__result__pb2.DESCRIPTOR,])




_CHECKSHAREEXRAIDPASSRESPONSE = _descriptor.Descriptor(
  name='CheckShareExRaidPassResponse',
  full_name='pogoprotos.networking.responses.CheckShareExRaidPassResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CheckShareExRaidPassResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=245,
)

_CHECKSHAREEXRAIDPASSRESPONSE.fields_by_name['result'].enum_type = pogoprotos_dot_enums_dot_share__ex__raid__pass__result__pb2._SHAREEXRAIDPASSRESULT
DESCRIPTOR.message_types_by_name['CheckShareExRaidPassResponse'] = _CHECKSHAREEXRAIDPASSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckShareExRaidPassResponse = _reflection.GeneratedProtocolMessageType('CheckShareExRaidPassResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKSHAREEXRAIDPASSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.check_share_ex_raid_pass_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CheckShareExRaidPassResponse)
  ))
_sym_db.RegisterMessage(CheckShareExRaidPassResponse)


# @@protoc_insertion_point(module_scope)
