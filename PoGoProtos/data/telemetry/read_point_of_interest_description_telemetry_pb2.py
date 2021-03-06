# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/read_point_of_interest_description_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import fort_type_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/read_point_of_interest_description_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nLpogoprotos/data/telemetry/read_point_of_interest_description_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a#pogoprotos/map/fort/fort_type.proto\"\x90\x01\n\'ReadPointOfInterestDescriptionTelemetry\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x30\n\tfort_type\x18\x03 \x01(\x0e\x32\x1d.pogoprotos.map.fort.FortType\x12\x12\n\npartner_id\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_fort__type__pb2.DESCRIPTOR,])




_READPOINTOFINTERESTDESCRIPTIONTELEMETRY = _descriptor.Descriptor(
  name='ReadPointOfInterestDescriptionTelemetry',
  full_name='pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_type', full_name='pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry.fort_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry.partner_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=145,
  serialized_end=289,
)

_READPOINTOFINTERESTDESCRIPTIONTELEMETRY.fields_by_name['fort_type'].enum_type = pogoprotos_dot_map_dot_fort_dot_fort__type__pb2._FORTTYPE
DESCRIPTOR.message_types_by_name['ReadPointOfInterestDescriptionTelemetry'] = _READPOINTOFINTERESTDESCRIPTIONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadPointOfInterestDescriptionTelemetry = _reflection.GeneratedProtocolMessageType('ReadPointOfInterestDescriptionTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _READPOINTOFINTERESTDESCRIPTIONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.read_point_of_interest_description_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ReadPointOfInterestDescriptionTelemetry)
  ))
_sym_db.RegisterMessage(ReadPointOfInterestDescriptionTelemetry)


# @@protoc_insertion_point(module_scope)
