# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/decline_friend_invite_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/decline_friend_invite_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nKpogoprotos/networking/social/responses/decline_friend_invite_response.proto\x12&pogoprotos.networking.social.responses\"\xf2\x01\n\x1b\x44\x65\x63lineFriendInviteResponse\x12Z\n\x06result\x18\x01 \x01(\x0e\x32J.pogoprotos.networking.social.responses.DeclineFriendInviteResponse.Result\"w\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1f\n\x1b\x45RROR_INVITE_DOES_NOT_EXIST\x10\x03\x12!\n\x1d\x45RROR_INVITE_ALREADY_DECLINED\x10\x04\x62\x06proto3')
)



_DECLINEFRIENDINVITERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.DeclineFriendInviteResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_DOES_NOT_EXIST', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_ALREADY_DECLINED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=362,
)
_sym_db.RegisterEnumDescriptor(_DECLINEFRIENDINVITERESPONSE_RESULT)


_DECLINEFRIENDINVITERESPONSE = _descriptor.Descriptor(
  name='DeclineFriendInviteResponse',
  full_name='pogoprotos.networking.social.responses.DeclineFriendInviteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.DeclineFriendInviteResponse.result', index=0,
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
    _DECLINEFRIENDINVITERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=362,
)

_DECLINEFRIENDINVITERESPONSE.fields_by_name['result'].enum_type = _DECLINEFRIENDINVITERESPONSE_RESULT
_DECLINEFRIENDINVITERESPONSE_RESULT.containing_type = _DECLINEFRIENDINVITERESPONSE
DESCRIPTOR.message_types_by_name['DeclineFriendInviteResponse'] = _DECLINEFRIENDINVITERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeclineFriendInviteResponse = _reflection.GeneratedProtocolMessageType('DeclineFriendInviteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DECLINEFRIENDINVITERESPONSE,
  __module__ = 'pogoprotos.networking.social.responses.decline_friend_invite_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.DeclineFriendInviteResponse)
  ))
_sym_db.RegisterMessage(DeclineFriendInviteResponse)


# @@protoc_insertion_point(module_scope)
