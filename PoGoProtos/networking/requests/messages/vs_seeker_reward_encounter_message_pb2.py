# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/vs_seeker_reward_encounter_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/vs_seeker_reward_encounter_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nPpogoprotos/networking/requests/messages/vs_seeker_reward_encounter_message.proto\x12\'pogoprotos.networking.requests.messages\"3\n\x1eVsSeekerRewardEncounterMessage\x12\x11\n\twin_index\x18\x01 \x01(\x05\x62\x06proto3')
)




_VSSEEKERREWARDENCOUNTERMESSAGE = _descriptor.Descriptor(
  name='VsSeekerRewardEncounterMessage',
  full_name='pogoprotos.networking.requests.messages.VsSeekerRewardEncounterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='win_index', full_name='pogoprotos.networking.requests.messages.VsSeekerRewardEncounterMessage.win_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=125,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['VsSeekerRewardEncounterMessage'] = _VSSEEKERREWARDENCOUNTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VsSeekerRewardEncounterMessage = _reflection.GeneratedProtocolMessageType('VsSeekerRewardEncounterMessage', (_message.Message,), dict(
  DESCRIPTOR = _VSSEEKERREWARDENCOUNTERMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.vs_seeker_reward_encounter_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.VsSeekerRewardEncounterMessage)
  ))
_sym_db.RegisterMessage(VsSeekerRewardEncounterMessage)


# @@protoc_insertion_point(module_scope)
