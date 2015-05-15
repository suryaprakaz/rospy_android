"""autogenerated by genpy from capabilities/RunningCapability.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import capabilities.msg

class RunningCapability(genpy.Message):
  _md5sum = "f97e2b23f907893008679ba2ff64fafc"
  _type = "capabilities/RunningCapability"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Name and provider of this running capability
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
  __slots__ = ['capability','dependent_capabilities','started_by','pid']
  _slot_types = ['capabilities/Capability','capabilities/Capability[]','string','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       capability,dependent_capabilities,started_by,pid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RunningCapability, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.capability is None:
        self.capability = capabilities.msg.Capability()
      if self.dependent_capabilities is None:
        self.dependent_capabilities = []
      if self.started_by is None:
        self.started_by = ''
      if self.pid is None:
        self.pid = 0
    else:
      self.capability = capabilities.msg.Capability()
      self.dependent_capabilities = []
      self.started_by = ''
      self.pid = 0

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
      _x = self.capability.capability
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.capability.provider
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dependent_capabilities)
      buff.write(_struct_I.pack(length))
      for val1 in self.dependent_capabilities:
        _x = val1.capability
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.provider
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.started_by
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.pid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.capability is None:
        self.capability = capabilities.msg.Capability()
      if self.dependent_capabilities is None:
        self.dependent_capabilities = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.capability.capability = str[start:end].decode('utf-8')
      else:
        self.capability.capability = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.capability.provider = str[start:end].decode('utf-8')
      else:
        self.capability.provider = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dependent_capabilities = []
      for i in range(0, length):
        val1 = capabilities.msg.Capability()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.capability = str[start:end].decode('utf-8')
        else:
          val1.capability = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.provider = str[start:end].decode('utf-8')
        else:
          val1.provider = str[start:end]
        self.dependent_capabilities.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.started_by = str[start:end].decode('utf-8')
      else:
        self.started_by = str[start:end]
      start = end
      end += 4
      (self.pid,) = _struct_i.unpack(str[start:end])
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
      _x = self.capability.capability
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.capability.provider
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dependent_capabilities)
      buff.write(_struct_I.pack(length))
      for val1 in self.dependent_capabilities:
        _x = val1.capability
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.provider
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.started_by
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.pid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.capability is None:
        self.capability = capabilities.msg.Capability()
      if self.dependent_capabilities is None:
        self.dependent_capabilities = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.capability.capability = str[start:end].decode('utf-8')
      else:
        self.capability.capability = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.capability.provider = str[start:end].decode('utf-8')
      else:
        self.capability.provider = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dependent_capabilities = []
      for i in range(0, length):
        val1 = capabilities.msg.Capability()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.capability = str[start:end].decode('utf-8')
        else:
          val1.capability = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.provider = str[start:end].decode('utf-8')
        else:
          val1.provider = str[start:end]
        self.dependent_capabilities.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.started_by = str[start:end].decode('utf-8')
      else:
        self.started_by = str[start:end]
      start = end
      end += 4
      (self.pid,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")