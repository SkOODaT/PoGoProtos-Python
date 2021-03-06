# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/vs_seeker_start_matchmaking_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_challenge_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/vs_seeker_start_matchmaking_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nJpogoprotos/networking/responses/vs_seeker_start_matchmaking_response.proto\x12\x1fpogoprotos.networking.responses\x1a-pogoprotos/data/combat/combat_challenge.proto\"\xc5\x04\n VsSeekerStartMatchmakingResponse\x12X\n\x06result\x18\x01 \x01(\x0e\x32H.pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse.Result\x12:\n\tchallenge\x18\x02 \x01(\x0b\x32\'.pogoprotos.data.combat.CombatChallenge\x12\x10\n\x08queue_id\x18\x03 \x01(\t\"\xf8\x02\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x1a\n\x16SUCCESS_OPPONENT_FOUND\x10\x01\x12\x12\n\x0eSUCCESS_QUEUED\x10\x02\x12\x1f\n\x1b\x45RROR_NO_BATTLE_PASSES_LEFT\x10\x03\x12\x1a\n\x16\x45RROR_ALREADY_IN_QUEUE\x10\x04\x12*\n&ERROR_VS_SEEKER_PLAYER_IN_WRONG_SEASON\x10\x05\x12!\n\x1d\x45RROR_PLAYER_HAS_NO_VS_SEEKER\x10\x06\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x07\x12.\n*ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE\x10\x08\x12!\n\x1d\x45RROR_VS_SEEKER_NOT_ACTIVATED\x10\t\x12!\n\x1d\x45RROR_TEMPORARILY_UNAVAILABLE\x10\n\x12\x18\n\x14\x45RROR_EXCEEDED_LIMIT\x10\x0b\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2.DESCRIPTOR,])



_VSSEEKERSTARTMATCHMAKINGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_OPPONENT_FOUND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_QUEUED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_BATTLE_PASSES_LEFT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_IN_QUEUE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VS_SEEKER_PLAYER_IN_WRONG_SEASON', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_VS_SEEKER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VS_SEEKER_NOT_ACTIVATED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TEMPORARILY_UNAVAILABLE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_EXCEEDED_LIMIT', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=364,
  serialized_end=740,
)
_sym_db.RegisterEnumDescriptor(_VSSEEKERSTARTMATCHMAKINGRESPONSE_RESULT)


_VSSEEKERSTARTMATCHMAKINGRESPONSE = _descriptor.Descriptor(
  name='VsSeekerStartMatchmakingResponse',
  full_name='pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge', full_name='pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse.challenge', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue_id', full_name='pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse.queue_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VSSEEKERSTARTMATCHMAKINGRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=740,
)

_VSSEEKERSTARTMATCHMAKINGRESPONSE.fields_by_name['result'].enum_type = _VSSEEKERSTARTMATCHMAKINGRESPONSE_RESULT
_VSSEEKERSTARTMATCHMAKINGRESPONSE.fields_by_name['challenge'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2._COMBATCHALLENGE
_VSSEEKERSTARTMATCHMAKINGRESPONSE_RESULT.containing_type = _VSSEEKERSTARTMATCHMAKINGRESPONSE
DESCRIPTOR.message_types_by_name['VsSeekerStartMatchmakingResponse'] = _VSSEEKERSTARTMATCHMAKINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VsSeekerStartMatchmakingResponse = _reflection.GeneratedProtocolMessageType('VsSeekerStartMatchmakingResponse', (_message.Message,), dict(
  DESCRIPTOR = _VSSEEKERSTARTMATCHMAKINGRESPONSE,
  __module__ = 'pogoprotos.networking.responses.vs_seeker_start_matchmaking_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.VsSeekerStartMatchmakingResponse)
  ))
_sym_db.RegisterMessage(VsSeekerStartMatchmakingResponse)


# @@protoc_insertion_point(module_scope)
