# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/list_friends_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.friends import friend_pb2 as pogoprotos_dot_data_dot_friends_dot_friend__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/list_friends_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBpogoprotos/networking/social/responses/list_friends_response.proto\x12&pogoprotos.networking.social.responses\x1a$pogoprotos/data/friends/friend.proto\"\xcf\x01\n\x13ListFriendsResponse\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.social.responses.ListFriendsResponse.Result\x12/\n\x06\x66riend\x18\x02 \x03(\x0b\x32\x1f.pogoprotos.data.friends.Friend\"3\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_friends_dot_friend__pb2.DESCRIPTOR,])



_LISTFRIENDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.ListFriendsResponse.Result',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=305,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_LISTFRIENDSRESPONSE_RESULT)


_LISTFRIENDSRESPONSE = _descriptor.Descriptor(
  name='ListFriendsResponse',
  full_name='pogoprotos.networking.social.responses.ListFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.ListFriendsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend', full_name='pogoprotos.networking.social.responses.ListFriendsResponse.friend', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTFRIENDSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=356,
)

_LISTFRIENDSRESPONSE.fields_by_name['result'].enum_type = _LISTFRIENDSRESPONSE_RESULT
_LISTFRIENDSRESPONSE.fields_by_name['friend'].message_type = pogoprotos_dot_data_dot_friends_dot_friend__pb2._FRIEND
_LISTFRIENDSRESPONSE_RESULT.containing_type = _LISTFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['ListFriendsResponse'] = _LISTFRIENDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListFriendsResponse = _reflection.GeneratedProtocolMessageType('ListFriendsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTFRIENDSRESPONSE,
  __module__ = 'pogoprotos.networking.social.responses.list_friends_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.ListFriendsResponse)
  ))
_sym_db.RegisterMessage(ListFriendsResponse)


# @@protoc_insertion_point(module_scope)
