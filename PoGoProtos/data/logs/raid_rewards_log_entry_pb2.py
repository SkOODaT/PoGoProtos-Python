# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/raid_rewards_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_data_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/raid_rewards_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/data/logs/raid_rewards_log_entry.proto\x12\x14pogoprotos.data.logs\x1a)pogoprotos/inventory/item/item_data.proto\"\x93\x02\n\x13RaidRewardsLogEntry\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.pogoprotos.data.logs.RaidRewardsLogEntry.Result\x12\x14\n\x0cis_exclusive\x18\x02 \x01(\x08\x12\x32\n\x05items\x18\x03 \x03(\x0b\x32#.pogoprotos.inventory.item.ItemData\x12<\n\x0f\x64\x65\x66\x61ult_rewards\x18\x04 \x03(\x0b\x32#.pogoprotos.inventory.item.ItemData\x12\x10\n\x08stardust\x18\x05 \x01(\x05\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__data__pb2.DESCRIPTOR,])



_RAIDREWARDSLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.RaidRewardsLogEntry.Result',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=362,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_RAIDREWARDSLOGENTRY_RESULT)


_RAIDREWARDSLOGENTRY = _descriptor.Descriptor(
  name='RaidRewardsLogEntry',
  full_name='pogoprotos.data.logs.RaidRewardsLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.RaidRewardsLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_exclusive', full_name='pogoprotos.data.logs.RaidRewardsLogEntry.is_exclusive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='pogoprotos.data.logs.RaidRewardsLogEntry.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_rewards', full_name='pogoprotos.data.logs.RaidRewardsLogEntry.default_rewards', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='pogoprotos.data.logs.RaidRewardsLogEntry.stardust', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RAIDREWARDSLOGENTRY_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=394,
)

_RAIDREWARDSLOGENTRY.fields_by_name['result'].enum_type = _RAIDREWARDSLOGENTRY_RESULT
_RAIDREWARDSLOGENTRY.fields_by_name['items'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__data__pb2._ITEMDATA
_RAIDREWARDSLOGENTRY.fields_by_name['default_rewards'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__data__pb2._ITEMDATA
_RAIDREWARDSLOGENTRY_RESULT.containing_type = _RAIDREWARDSLOGENTRY
DESCRIPTOR.message_types_by_name['RaidRewardsLogEntry'] = _RAIDREWARDSLOGENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidRewardsLogEntry = _reflection.GeneratedProtocolMessageType('RaidRewardsLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _RAIDREWARDSLOGENTRY,
  __module__ = 'pogoprotos.data.logs.raid_rewards_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.RaidRewardsLogEntry)
  ))
_sym_db.RegisterMessage(RaidRewardsLogEntry)


# @@protoc_insertion_point(module_scope)