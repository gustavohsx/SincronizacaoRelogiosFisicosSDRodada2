# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clock_sync.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63lock_sync.proto\"\"\n\x0bTimeRequest\x12\x13\n\x0b\x63lient_time\x18\x01 \x01(\x03\"7\n\x0cTimeResponse\x12\x13\n\x0bserver_time\x18\x01 \x01(\x03\x12\x12\n\nadjustment\x18\x02 \x01(\x03\x32\x63\n\tClockSync\x12&\n\x07GetTime\x12\x0c.TimeRequest\x1a\r.TimeResponse\x12.\n\rGetTimeStream\x12\x0c.TimeRequest\x1a\r.TimeResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clock_sync_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMEREQUEST']._serialized_start=20
  _globals['_TIMEREQUEST']._serialized_end=54
  _globals['_TIMERESPONSE']._serialized_start=56
  _globals['_TIMERESPONSE']._serialized_end=111
  _globals['_CLOCKSYNC']._serialized_start=113
  _globals['_CLOCKSYNC']._serialized_end=212
# @@protoc_insertion_point(module_scope)