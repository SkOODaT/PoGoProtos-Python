# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_vs_seeker_status_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings.master.item import vs_seeker_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_vs__seeker__attributes__pb2
from pogoprotos.data.combat import combat_log_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_vs_seeker_status_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpogoprotos/networking/responses/get_vs_seeker_status_response.proto\x12\x1fpogoprotos.networking.responses\x1a:pogoprotos/settings/master/item/vs_seeker_attributes.proto\x1a\'pogoprotos/data/combat/combat_log.proto\"\xa2\x03\n\x19GetVsSeekerStatusResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.GetVsSeekerStatusResponse.Result\x12\x46\n\tvs_seeker\x18\x02 \x01(\x0b\x32\x33.pogoprotos.settings.master.item.VsSeekerAttributes\x12\x14\n\x0cseason_ended\x18\x03 \x01(\x08\x12\x35\n\ncombat_log\x18\x04 \x01(\x0b\x32!.pogoprotos.data.combat.CombatLog\"\x9c\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x19\n\x15SUCCESS_FULLY_CHARGED\x10\x01\x12!\n\x1dSUCCESS_NOT_FULLY_CHARGED_YET\x10\x02\x12\x1d\n\x19\x45RROR_VS_SEEKER_NOT_FOUND\x10\x03\x12*\n&ERROR_VS_SEEKER_NEVER_STARTED_CHARGING\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_master_dot_item_dot_vs__seeker__attributes__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_combat__log__pb2.DESCRIPTOR,])



_GETVSSEEKERSTATUSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_FULLY_CHARGED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_NOT_FULLY_CHARGED_YET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VS_SEEKER_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VS_SEEKER_NEVER_STARTED_CHARGING', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=468,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_GETVSSEEKERSTATUSRESPONSE_RESULT)


_GETVSSEEKERSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetVsSeekerStatusResponse',
  full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vs_seeker', full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse.vs_seeker', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='season_ended', full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse.season_ended', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_log', full_name='pogoprotos.networking.responses.GetVsSeekerStatusResponse.combat_log', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETVSSEEKERSTATUSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=624,
)

_GETVSSEEKERSTATUSRESPONSE.fields_by_name['result'].enum_type = _GETVSSEEKERSTATUSRESPONSE_RESULT
_GETVSSEEKERSTATUSRESPONSE.fields_by_name['vs_seeker'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_vs__seeker__attributes__pb2._VSSEEKERATTRIBUTES
_GETVSSEEKERSTATUSRESPONSE.fields_by_name['combat_log'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__log__pb2._COMBATLOG
_GETVSSEEKERSTATUSRESPONSE_RESULT.containing_type = _GETVSSEEKERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['GetVsSeekerStatusResponse'] = _GETVSSEEKERSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVsSeekerStatusResponse = _reflection.GeneratedProtocolMessageType('GetVsSeekerStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETVSSEEKERSTATUSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_vs_seeker_status_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetVsSeekerStatusResponse)
  ))
_sym_db.RegisterMessage(GetVsSeekerStatusResponse)


# @@protoc_insertion_point(module_scope)
