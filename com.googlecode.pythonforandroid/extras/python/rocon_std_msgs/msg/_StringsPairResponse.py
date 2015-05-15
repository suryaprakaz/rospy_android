"""autogenerated by genpy from rocon_std_msgs/StringsPairResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import rocon_std_msgs.msg

class StringsPairResponse(genpy.Message):
  _md5sum = "7b20492548347a7692aa8c5680af8d1b"
  _type = "rocon_std_msgs/StringsPairResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM A SERVICE PAIR DEFINITION ======

uuid_msgs/UniqueID id
StringsResponse response

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

================================================================================
MSG: rocon_std_msgs/StringsResponse
# ====== DO NOT MODIFY! AUTOGENERATED FROM A SERVICE PAIR DEFINITION ======

string data


"""
  __slots__ = ['id','response']
  _slot_types = ['uuid_msgs/UniqueID','rocon_std_msgs/StringsResponse']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,response

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StringsPairResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.response is None:
        self.response = rocon_std_msgs.msg.StringsResponse()
    else:
      self.id = uuid_msgs.msg.UniqueID()
      self.response = rocon_std_msgs.msg.StringsResponse()

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
      _x = self.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.response.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.response is None:
        self.response = rocon_std_msgs.msg.StringsResponse()
      end = 0
      start = end
      end += 16
      self.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.response.data = str[start:end].decode('utf-8')
      else:
        self.response.data = str[start:end]
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
      _x = self.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.response.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.response is None:
        self.response = rocon_std_msgs.msg.StringsResponse()
      end = 0
      start = end
      end += 16
      self.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.response.data = str[start:end].decode('utf-8')
      else:
        self.response.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_16B = struct.Struct("<16B")
_struct_16s = struct.Struct("<16s")
