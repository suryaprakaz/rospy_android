"""autogenerated by genpy from capabilities/GetRunningCapabilitiesRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetRunningCapabilitiesRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "capabilities/GetRunningCapabilitiesRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetRunningCapabilitiesRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
"""autogenerated by genpy from capabilities/GetRunningCapabilitiesResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import capabilities.msg

class GetRunningCapabilitiesResponse(genpy.Message):
  _md5sum = "e8e5cf68c34711ffaa719728f34ea7a3"
  _type = "capabilities/GetRunningCapabilitiesResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """RunningCapability[] running_capabilities


================================================================================
MSG: capabilities/RunningCapability
# Name and provider of this running capability
Capability capability
# Capabilities which depend on this one
Capability[] dependent_capabilities
# Message stating what started this capability
string started_by
# Process ID of the running provider
int32 pid

================================================================================
MSG: capabilities/Capability
# Capability
string capability
# Used provider
string provider

"""
  __slots__ = ['running_capabilities']
  _slot_types = ['capabilities/RunningCapability[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       running_capabilities

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetRunningCapabilitiesResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.running_capabilities is None:
        self.running_capabilities = []
    else:
      self.running_capabilities = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.running_capabilities)
      buff.write(_struct_I.pack(length))
      for val1 in self.running_capabilities:
        _v1 = val1.capability
        _x = _v1.capability
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1.provider
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.dependent_capabilities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.dependent_capabilities:
          _x = val2.capability
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.provider
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.started_by
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.pid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.running_capabilities is None:
        self.running_capabilities = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.running_capabilities = []
      for i in range(0, length):
        val1 = capabilities.msg.RunningCapability()
        _v2 = val1.capability
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v2.capability = str[start:end].decode('utf-8')
        else:
          _v2.capability = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v2.provider = str[start:end].decode('utf-8')
        else:
          _v2.provider = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.dependent_capabilities = []
        for i in range(0, length):
          val2 = capabilities.msg.Capability()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.capability = str[start:end].decode('utf-8')
          else:
            val2.capability = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.provider = str[start:end].decode('utf-8')
          else:
            val2.provider = str[start:end]
          val1.dependent_capabilities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.started_by = str[start:end].decode('utf-8')
        else:
          val1.started_by = str[start:end]
        start = end
        end += 4
        (val1.pid,) = _struct_i.unpack(str[start:end])
        self.running_capabilities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.running_capabilities)
      buff.write(_struct_I.pack(length))
      for val1 in self.running_capabilities:
        _v3 = val1.capability
        _x = _v3.capability
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v3.provider
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.dependent_capabilities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.dependent_capabilities:
          _x = val2.capability
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.provider
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.started_by
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.pid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.running_capabilities is None:
        self.running_capabilities = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.running_capabilities = []
      for i in range(0, length):
        val1 = capabilities.msg.RunningCapability()
        _v4 = val1.capability
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.capability = str[start:end].decode('utf-8')
        else:
          _v4.capability = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.provider = str[start:end].decode('utf-8')
        else:
          _v4.provider = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.dependent_capabilities = []
        for i in range(0, length):
          val2 = capabilities.msg.Capability()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.capability = str[start:end].decode('utf-8')
          else:
            val2.capability = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.provider = str[start:end].decode('utf-8')
          else:
            val2.provider = str[start:end]
          val1.dependent_capabilities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.started_by = str[start:end].decode('utf-8')
        else:
          val1.started_by = str[start:end]
        start = end
        end += 4
        (val1.pid,) = _struct_i.unpack(str[start:end])
        self.running_capabilities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
class GetRunningCapabilities(object):
  _type          = 'capabilities/GetRunningCapabilities'
  _md5sum = 'e8e5cf68c34711ffaa719728f34ea7a3'
  _request_class  = GetRunningCapabilitiesRequest
  _response_class = GetRunningCapabilitiesResponse
