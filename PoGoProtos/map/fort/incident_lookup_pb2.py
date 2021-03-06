# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/incident_lookup.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/incident_lookup.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/map/fort/incident_lookup.proto\x12\x13pogoprotos.map.fort\"Z\n\x0eIncidentLookup\x12\x13\n\x0bincident_id\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x10\n\x08\x66ort_lat\x18\x03 \x01(\x01\x12\x10\n\x08\x66ort_lng\x18\x04 \x01(\x01\x62\x06proto3')
)




_INCIDENTLOOKUP = _descriptor.Descriptor(
  name='IncidentLookup',
  full_name='pogoprotos.map.fort.IncidentLookup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incident_id', full_name='pogoprotos.map.fort.IncidentLookup.incident_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.map.fort.IncidentLookup.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_lat', full_name='pogoprotos.map.fort.IncidentLookup.fort_lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_lng', full_name='pogoprotos.map.fort.IncidentLookup.fort_lng', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=66,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['IncidentLookup'] = _INCIDENTLOOKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncidentLookup = _reflection.GeneratedProtocolMessageType('IncidentLookup', (_message.Message,), dict(
  DESCRIPTOR = _INCIDENTLOOKUP,
  __module__ = 'pogoprotos.map.fort.incident_lookup_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.IncidentLookup)
  ))
_sym_db.RegisterMessage(IncidentLookup)


# @@protoc_insertion_point(module_scope)
