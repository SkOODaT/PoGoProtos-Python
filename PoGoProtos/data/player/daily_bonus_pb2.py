# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/daily_bonus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/daily_bonus.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/data/player/daily_bonus.proto\x12\x16pogoprotos.data.player\"c\n\nDailyBonus\x12#\n\x1bnext_collected_timestamp_ms\x18\x01 \x01(\x03\x12\x30\n(next_defender_bonus_collect_timestamp_ms\x18\x02 \x01(\x03\x62\x06proto3')
)




_DAILYBONUS = _descriptor.Descriptor(
  name='DailyBonus',
  full_name='pogoprotos.data.player.DailyBonus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_collected_timestamp_ms', full_name='pogoprotos.data.player.DailyBonus.next_collected_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_defender_bonus_collect_timestamp_ms', full_name='pogoprotos.data.player.DailyBonus.next_defender_bonus_collect_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=68,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['DailyBonus'] = _DAILYBONUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyBonus = _reflection.GeneratedProtocolMessageType('DailyBonus', (_message.Message,), dict(
  DESCRIPTOR = _DAILYBONUS,
  __module__ = 'pogoprotos.data.player.daily_bonus_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.DailyBonus)
  ))
_sym_db.RegisterMessage(DailyBonus)


# @@protoc_insertion_point(module_scope)
