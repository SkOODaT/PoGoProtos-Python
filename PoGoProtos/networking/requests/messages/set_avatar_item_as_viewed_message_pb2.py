# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/set_avatar_item_as_viewed_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/set_avatar_item_as_viewed_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nOpogoprotos/networking/requests/messages/set_avatar_item_as_viewed_message.proto\x12\'pogoprotos.networking.requests.messages\":\n\x1cSetAvatarItemAsViewedMessage\x12\x1a\n\x12\x61vatar_template_id\x18\x01 \x03(\tb\x06proto3')
)




_SETAVATARITEMASVIEWEDMESSAGE = _descriptor.Descriptor(
  name='SetAvatarItemAsViewedMessage',
  full_name='pogoprotos.networking.requests.messages.SetAvatarItemAsViewedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='pogoprotos.networking.requests.messages.SetAvatarItemAsViewedMessage.avatar_template_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=124,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['SetAvatarItemAsViewedMessage'] = _SETAVATARITEMASVIEWEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetAvatarItemAsViewedMessage = _reflection.GeneratedProtocolMessageType('SetAvatarItemAsViewedMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETAVATARITEMASVIEWEDMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.set_avatar_item_as_viewed_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SetAvatarItemAsViewedMessage)
  ))
_sym_db.RegisterMessage(SetAvatarItemAsViewedMessage)


# @@protoc_insertion_point(module_scope)
