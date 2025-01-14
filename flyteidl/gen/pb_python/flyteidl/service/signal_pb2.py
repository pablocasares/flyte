# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/service/signal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from flyteidl.admin import signal_pb2 as flyteidl_dot_admin_dot_signal__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66lyteidl/service/signal.proto\x12\x10\x66lyteidl.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x66lyteidl/admin/signal.proto\x1a.protoc-gen-openapiv2/options/annotations.proto2\xa9\x07\n\rSignalService\x12\x90\x01\n\x11GetOrCreateSignal\x12(.flyteidl.admin.SignalGetOrCreateRequest\x1a\x16.flyteidl.admin.Signal\"9\x92\x41\x36\x1a\x34Retrieve a signal, creating it if it does not exist.\x12\xa0\x03\n\x0bListSignals\x12!.flyteidl.admin.SignalListRequest\x1a\x1a.flyteidl.admin.SignalList\"\xd1\x02\x92\x41I\x1aGFetch existing signal definitions matching the input signal id filters.\x82\xd3\xe4\x93\x02\xfe\x01Z\x8e\x01\x12\x8b\x01/api/v1/signals/org/{workflow_execution_id.org}/{workflow_execution_id.project}/{workflow_execution_id.domain}/{workflow_execution_id.name}\x12k/api/v1/signals/{workflow_execution_id.project}/{workflow_execution_id.domain}/{workflow_execution_id.name}\x12\xe1\x02\n\tSetSignal\x12 .flyteidl.admin.SignalSetRequest\x1a!.flyteidl.admin.SignalSetResponse\"\x8e\x02\x92\x41\xc0\x01\x1a\x13Set a signal value.JB\n\x03\x34\x30\x30\x12;\n9Returned for bad request that may have failed validation.Je\n\x03\x34\x30\x39\x12^\n\\Returned for a request that references an identical entity that has already been registered.\x82\xd3\xe4\x93\x02\x44:\x01*Z.:\x01*\")/api/v1/signals/org/{id.execution_id.org}\"\x0f/api/v1/signalsB\xc3\x01\n\x14\x63om.flyteidl.serviceB\x0bSignalProtoP\x01Z=github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/service\xa2\x02\x03\x46SX\xaa\x02\x10\x46lyteidl.Service\xca\x02\x10\x46lyteidl\\Service\xe2\x02\x1c\x46lyteidl\\Service\\GPBMetadata\xea\x02\x11\x46lyteidl::Serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.service.signal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.flyteidl.serviceB\013SignalProtoP\001Z=github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/service\242\002\003FSX\252\002\020Flyteidl.Service\312\002\020Flyteidl\\Service\342\002\034Flyteidl\\Service\\GPBMetadata\352\002\021Flyteidl::Service'
  _SIGNALSERVICE.methods_by_name['GetOrCreateSignal']._options = None
  _SIGNALSERVICE.methods_by_name['GetOrCreateSignal']._serialized_options = b'\222A6\0324Retrieve a signal, creating it if it does not exist.'
  _SIGNALSERVICE.methods_by_name['ListSignals']._options = None
  _SIGNALSERVICE.methods_by_name['ListSignals']._serialized_options = b'\222AI\032GFetch existing signal definitions matching the input signal id filters.\202\323\344\223\002\376\001Z\216\001\022\213\001/api/v1/signals/org/{workflow_execution_id.org}/{workflow_execution_id.project}/{workflow_execution_id.domain}/{workflow_execution_id.name}\022k/api/v1/signals/{workflow_execution_id.project}/{workflow_execution_id.domain}/{workflow_execution_id.name}'
  _SIGNALSERVICE.methods_by_name['SetSignal']._options = None
  _SIGNALSERVICE.methods_by_name['SetSignal']._serialized_options = b'\222A\300\001\032\023Set a signal value.JB\n\003400\022;\n9Returned for bad request that may have failed validation.Je\n\003409\022^\n\\Returned for a request that references an identical entity that has already been registered.\202\323\344\223\002D:\001*Z.:\001*\")/api/v1/signals/org/{id.execution_id.org}\"\017/api/v1/signals'
  _globals['_SIGNALSERVICE']._serialized_start=159
  _globals['_SIGNALSERVICE']._serialized_end=1096
# @@protoc_insertion_point(module_scope)
