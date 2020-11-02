# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameserver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='frameserver.proto',
  package='frameserver',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x66rameserver.proto\x12\x0b\x66rameserver\"$\n\x0c\x46rameRequest\x12\x14\n\x0cscene_offset\x18\x01 \x01(\x02\"u\n\x05Style\x12\x12\n\nfill_color\x18\x01 \x01(\t\x12\x14\n\x0c\x66ill_opacity\x18\x02 \x01(\x02\x12\x14\n\x0cstroke_color\x18\x03 \x01(\t\x12\x16\n\x0estroke_opacity\x18\x04 \x01(\x02\x12\x14\n\x0cstroke_width\x18\x05 \x01(\x02\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"v\n\x0bMobjectData\x12\n\n\x02id\x18\x01 \x01(\x03\x12\"\n\x06points\x18\x02 \x03(\x0b\x32\x12.frameserver.Point\x12!\n\x05style\x18\x03 \x01(\x0b\x32\x12.frameserver.Style\x12\x14\n\x0cneeds_redraw\x18\x04 \x01(\x08\"\xb0\x01\n\rFrameResponse\x12*\n\x08mobjects\x18\x01 \x03(\x0b\x32\x18.frameserver.MobjectData\x12\x15\n\rframe_pending\x18\x02 \x01(\x08\x12\x1a\n\x12\x61nimation_finished\x18\x03 \x01(\x08\x12\x16\n\x0escene_finished\x18\x04 \x01(\x08\x12\x10\n\x08\x64uration\x18\x05 \x01(\x02\x12\x16\n\x0e\x61nimation_name\x18\x06 \x01(\t\"\x17\n\x15RendererStatusRequest\",\n\x16RendererStatusResponse\x12\x12\n\nscene_name\x18\x01 \x01(\t\"\x16\n\x14SceneLocationRequest\"\x17\n\x15SceneLocationResponse2\x8f\x02\n\x0b\x46rameServer\x12G\n\x0eGetFrameAtTime\x12\x19.frameserver.FrameRequest\x1a\x1a.frameserver.FrameResponse\x12Y\n\x0eRendererStatus\x12\".frameserver.RendererStatusRequest\x1a#.frameserver.RendererStatusResponse\x12\\\n\x13UpdateSceneLocation\x12!.frameserver.SceneLocationRequest\x1a\".frameserver.SceneLocationResponseb\x06proto3'
)




_FRAMEREQUEST = _descriptor.Descriptor(
  name='FrameRequest',
  full_name='frameserver.FrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_offset', full_name='frameserver.FrameRequest.scene_offset', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=34,
  serialized_end=70,
)


_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='frameserver.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill_color', full_name='frameserver.Style.fill_color', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fill_opacity', full_name='frameserver.Style.fill_opacity', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stroke_color', full_name='frameserver.Style.stroke_color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stroke_opacity', full_name='frameserver.Style.stroke_opacity', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stroke_width', full_name='frameserver.Style.stroke_width', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=189,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='frameserver.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='frameserver.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='frameserver.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='frameserver.Point.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=191,
  serialized_end=231,
)


_MOBJECTDATA = _descriptor.Descriptor(
  name='MobjectData',
  full_name='frameserver.MobjectData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='frameserver.MobjectData.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='frameserver.MobjectData.points', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='style', full_name='frameserver.MobjectData.style', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='needs_redraw', full_name='frameserver.MobjectData.needs_redraw', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=233,
  serialized_end=351,
)


_FRAMERESPONSE = _descriptor.Descriptor(
  name='FrameResponse',
  full_name='frameserver.FrameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobjects', full_name='frameserver.FrameResponse.mobjects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_pending', full_name='frameserver.FrameResponse.frame_pending', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='animation_finished', full_name='frameserver.FrameResponse.animation_finished', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scene_finished', full_name='frameserver.FrameResponse.scene_finished', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='frameserver.FrameResponse.duration', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='animation_name', full_name='frameserver.FrameResponse.animation_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=354,
  serialized_end=530,
)


_RENDERERSTATUSREQUEST = _descriptor.Descriptor(
  name='RendererStatusRequest',
  full_name='frameserver.RendererStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=532,
  serialized_end=555,
)


_RENDERERSTATUSRESPONSE = _descriptor.Descriptor(
  name='RendererStatusResponse',
  full_name='frameserver.RendererStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_name', full_name='frameserver.RendererStatusResponse.scene_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=557,
  serialized_end=601,
)


_SCENELOCATIONREQUEST = _descriptor.Descriptor(
  name='SceneLocationRequest',
  full_name='frameserver.SceneLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=603,
  serialized_end=625,
)


_SCENELOCATIONRESPONSE = _descriptor.Descriptor(
  name='SceneLocationResponse',
  full_name='frameserver.SceneLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=627,
  serialized_end=650,
)

_MOBJECTDATA.fields_by_name['points'].message_type = _POINT
_MOBJECTDATA.fields_by_name['style'].message_type = _STYLE
_FRAMERESPONSE.fields_by_name['mobjects'].message_type = _MOBJECTDATA
DESCRIPTOR.message_types_by_name['FrameRequest'] = _FRAMEREQUEST
DESCRIPTOR.message_types_by_name['Style'] = _STYLE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['MobjectData'] = _MOBJECTDATA
DESCRIPTOR.message_types_by_name['FrameResponse'] = _FRAMERESPONSE
DESCRIPTOR.message_types_by_name['RendererStatusRequest'] = _RENDERERSTATUSREQUEST
DESCRIPTOR.message_types_by_name['RendererStatusResponse'] = _RENDERERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['SceneLocationRequest'] = _SCENELOCATIONREQUEST
DESCRIPTOR.message_types_by_name['SceneLocationResponse'] = _SCENELOCATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameRequest = _reflection.GeneratedProtocolMessageType('FrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEREQUEST,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.FrameRequest)
  })
_sym_db.RegisterMessage(FrameRequest)

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {
  'DESCRIPTOR' : _STYLE,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.Style)
  })
_sym_db.RegisterMessage(Style)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.Point)
  })
_sym_db.RegisterMessage(Point)

MobjectData = _reflection.GeneratedProtocolMessageType('MobjectData', (_message.Message,), {
  'DESCRIPTOR' : _MOBJECTDATA,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.MobjectData)
  })
_sym_db.RegisterMessage(MobjectData)

FrameResponse = _reflection.GeneratedProtocolMessageType('FrameResponse', (_message.Message,), {
  'DESCRIPTOR' : _FRAMERESPONSE,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.FrameResponse)
  })
_sym_db.RegisterMessage(FrameResponse)

RendererStatusRequest = _reflection.GeneratedProtocolMessageType('RendererStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENDERERSTATUSREQUEST,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.RendererStatusRequest)
  })
_sym_db.RegisterMessage(RendererStatusRequest)

RendererStatusResponse = _reflection.GeneratedProtocolMessageType('RendererStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _RENDERERSTATUSRESPONSE,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.RendererStatusResponse)
  })
_sym_db.RegisterMessage(RendererStatusResponse)

SceneLocationRequest = _reflection.GeneratedProtocolMessageType('SceneLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCENELOCATIONREQUEST,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.SceneLocationRequest)
  })
_sym_db.RegisterMessage(SceneLocationRequest)

SceneLocationResponse = _reflection.GeneratedProtocolMessageType('SceneLocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCENELOCATIONRESPONSE,
  '__module__' : 'frameserver_pb2'
  # @@protoc_insertion_point(class_scope:frameserver.SceneLocationResponse)
  })
_sym_db.RegisterMessage(SceneLocationResponse)



_FRAMESERVER = _descriptor.ServiceDescriptor(
  name='FrameServer',
  full_name='frameserver.FrameServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=653,
  serialized_end=924,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFrameAtTime',
    full_name='frameserver.FrameServer.GetFrameAtTime',
    index=0,
    containing_service=None,
    input_type=_FRAMEREQUEST,
    output_type=_FRAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RendererStatus',
    full_name='frameserver.FrameServer.RendererStatus',
    index=1,
    containing_service=None,
    input_type=_RENDERERSTATUSREQUEST,
    output_type=_RENDERERSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSceneLocation',
    full_name='frameserver.FrameServer.UpdateSceneLocation',
    index=2,
    containing_service=None,
    input_type=_SCENELOCATIONREQUEST,
    output_type=_SCENELOCATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FRAMESERVER)

DESCRIPTOR.services_by_name['FrameServer'] = _FRAMESERVER

# @@protoc_insertion_point(module_scope)
