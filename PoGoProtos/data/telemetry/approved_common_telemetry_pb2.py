# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/approved_common_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.analytics import client_telemetry_common_filter_pb2 as pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2
from pogoprotos.data.telemetry import common_telemetry_boot_time_pb2 as pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__boot__time__pb2
from pogoprotos.data.telemetry import common_telemetry_shop_click_pb2 as pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__click__pb2
from pogoprotos.data.telemetry import common_telemetry_shop_view_pb2 as pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__view__pb2
from pogoprotos.data.telemetry import server_record_metadata_pb2 as pogoprotos_dot_data_dot_telemetry_dot_server__record__metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/approved_common_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/data/telemetry/approved_common_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a>pogoprotos/data/analytics/client_telemetry_common_filter.proto\x1a:pogoprotos/data/telemetry/common_telemetry_boot_time.proto\x1a;pogoprotos/data/telemetry/common_telemetry_shop_click.proto\x1a:pogoprotos/data/telemetry/common_telemetry_shop_view.proto\x1a\x36pogoprotos/data/telemetry/server_record_metadata.proto\"\x9d\x03\n\x17\x41pprovedCommonTelemetry\x12G\n\tboot_time\x18\x01 \x01(\x0b\x32\x32.pogoprotos.data.telemetry.CommonTelemetryBootTimeH\x00\x12I\n\nshop_click\x18\x02 \x01(\x0b\x32\x33.pogoprotos.data.telemetry.CommonTelemetryShopClickH\x00\x12G\n\tshop_view\x18\x03 \x01(\x0b\x32\x32.pogoprotos.data.telemetry.CommonTelemetryShopViewH\x00\x12\x44\n\x0bserver_data\x18\x04 \x01(\x0b\x32/.pogoprotos.data.telemetry.ServerRecordMetadata\x12N\n\x0e\x63ommon_filters\x18\x05 \x01(\x0b\x32\x36.pogoprotos.data.analytics.ClientTelemetryCommonFilterB\x0f\n\rTelemetryDatab\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__boot__time__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__click__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__view__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_telemetry_dot_server__record__metadata__pb2.DESCRIPTOR,])




_APPROVEDCOMMONTELEMETRY = _descriptor.Descriptor(
  name='ApprovedCommonTelemetry',
  full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boot_time', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.boot_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shop_click', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.shop_click', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shop_view', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.shop_view', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_data', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.server_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_filters', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.common_filters', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='TelemetryData', full_name='pogoprotos.data.telemetry.ApprovedCommonTelemetry.TelemetryData',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=390,
  serialized_end=803,
)

_APPROVEDCOMMONTELEMETRY.fields_by_name['boot_time'].message_type = pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__boot__time__pb2._COMMONTELEMETRYBOOTTIME
_APPROVEDCOMMONTELEMETRY.fields_by_name['shop_click'].message_type = pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__click__pb2._COMMONTELEMETRYSHOPCLICK
_APPROVEDCOMMONTELEMETRY.fields_by_name['shop_view'].message_type = pogoprotos_dot_data_dot_telemetry_dot_common__telemetry__shop__view__pb2._COMMONTELEMETRYSHOPVIEW
_APPROVEDCOMMONTELEMETRY.fields_by_name['server_data'].message_type = pogoprotos_dot_data_dot_telemetry_dot_server__record__metadata__pb2._SERVERRECORDMETADATA
_APPROVEDCOMMONTELEMETRY.fields_by_name['common_filters'].message_type = pogoprotos_dot_data_dot_analytics_dot_client__telemetry__common__filter__pb2._CLIENTTELEMETRYCOMMONFILTER
_APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData'].fields.append(
  _APPROVEDCOMMONTELEMETRY.fields_by_name['boot_time'])
_APPROVEDCOMMONTELEMETRY.fields_by_name['boot_time'].containing_oneof = _APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData']
_APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData'].fields.append(
  _APPROVEDCOMMONTELEMETRY.fields_by_name['shop_click'])
_APPROVEDCOMMONTELEMETRY.fields_by_name['shop_click'].containing_oneof = _APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData']
_APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData'].fields.append(
  _APPROVEDCOMMONTELEMETRY.fields_by_name['shop_view'])
_APPROVEDCOMMONTELEMETRY.fields_by_name['shop_view'].containing_oneof = _APPROVEDCOMMONTELEMETRY.oneofs_by_name['TelemetryData']
DESCRIPTOR.message_types_by_name['ApprovedCommonTelemetry'] = _APPROVEDCOMMONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApprovedCommonTelemetry = _reflection.GeneratedProtocolMessageType('ApprovedCommonTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _APPROVEDCOMMONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.approved_common_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ApprovedCommonTelemetry)
  ))
_sym_db.RegisterMessage(ApprovedCommonTelemetry)


# @@protoc_insertion_point(module_scope)