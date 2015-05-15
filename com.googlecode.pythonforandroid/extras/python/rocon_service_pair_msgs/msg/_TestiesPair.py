"""autogenerated by genpy from rocon_service_pair_msgs/TestiesPair.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import rocon_service_pair_msgs.msg

class TestiesPair(genpy.Message):
  _md5sum = "7b5cb9b4ccdb74840ce04ea92d2a141d"
  _type = "rocon_service_pair_msgs/TestiesPair"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
TestiesPairRequest pair_request
TestiesPairResponse pair_response

================================================================================
MSG: rocon_service_pair_msgs/TestiesPairRequest
uuid_msgs/UniqueID id
TestiesRequest request

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

================================================================================
MSG: rocon_service_pair_msgs/TestiesRequest
string data

================================================================================
MSG: rocon_service_pair_msgs/TestiesPairResponse
uuid_msgs/UniqueID id
TestiesResponse response

================================================================================
MSG: rocon_service_pair_msgs/TestiesResponse
# ====== DO NOT MODIFY! AUTOGENERATED FROM A SERVICE PAIR DEFINITION ======
uuid_msgs/UniqueID id
string data

"""
  __slots__ = ['pair_request','pair_response']
  _slot_types = ['rocon_service_pair_msgs/TestiesPairRequest','rocon_service_pair_msgs/TestiesPairResponse']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pair_request,pair_response

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TestiesPair, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pair_request is None:
        self.pair_request = rocon_service_pair_msgs.msg.TestiesPairRequest()
      if self.pair_response is None:
        self.pair_response = rocon_service_pair_msgs.msg.TestiesPairResponse()
    else:
      self.pair_request = rocon_service_pair_msgs.msg.TestiesPairRequest()
      self.pair_response = rocon_service_pair_msgs.msg.TestiesPairResponse()

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
      _x = self.pair_request.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_request.request.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.pair_response.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_response.response.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_response.response.data
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
      if self.pair_request is None:
        self.pair_request = rocon_service_pair_msgs.msg.TestiesPairRequest()
      if self.pair_response is None:
        self.pair_response = rocon_service_pair_msgs.msg.TestiesPairResponse()
      end = 0
      start = end
      end += 16
      self.pair_request.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pair_request.request.data = str[start:end].decode('utf-8')
      else:
        self.pair_request.request.data = str[start:end]
      start = end
      end += 16
      self.pair_response.id.uuid = str[start:end]
      start = end
      end += 16
      self.pair_response.response.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pair_response.response.data = str[start:end].decode('utf-8')
      else:
        self.pair_response.response.data = str[start:end]
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
      _x = self.pair_request.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_request.request.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.pair_response.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_response.response.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self.pair_response.response.data
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
      if self.pair_request is None:
        self.pair_request = rocon_service_pair_msgs.msg.TestiesPairRequest()
      if self.pair_response is None:
        self.pair_response = rocon_service_pair_msgs.msg.TestiesPairResponse()
      end = 0
      start = end
      end += 16
      self.pair_request.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pair_request.request.data = str[start:end].decode('utf-8')
      else:
        self.pair_request.request.data = str[start:end]
      start = end
      end += 16
      self.pair_response.id.uuid = str[start:end]
      start = end
      end += 16
      self.pair_response.response.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pair_response.response.data = str[start:end].decode('utf-8')
      else:
        self.pair_response.response.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_16B = struct.Struct("<16B")
_struct_16s = struct.Struct("<16s")
