"""autogenerated by genpy from world_canvas_msgs/PubAnnotationsDataRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg

class PubAnnotationsDataRequest(genpy.Message):
  _md5sum = "1f37618ab20aa1492050e9599baf8ad0"
  _type = "world_canvas_msgs/PubAnnotationsDataRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """






uuid_msgs/UniqueID[] annotation_ids
string topic_name
string topic_type
bool pub_as_list


================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

"""
  __slots__ = ['annotation_ids','topic_name','topic_type','pub_as_list']
  _slot_types = ['uuid_msgs/UniqueID[]','string','string','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       annotation_ids,topic_name,topic_type,pub_as_list

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PubAnnotationsDataRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.annotation_ids is None:
        self.annotation_ids = []
      if self.topic_name is None:
        self.topic_name = ''
      if self.topic_type is None:
        self.topic_type = ''
      if self.pub_as_list is None:
        self.pub_as_list = False
    else:
      self.annotation_ids = []
      self.topic_name = ''
      self.topic_type = ''
      self.pub_as_list = False

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
      length = len(self.annotation_ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation_ids:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
      _x = self.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topic_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.pub_as_list))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.annotation_ids is None:
        self.annotation_ids = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation_ids = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation_ids.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_name = str[start:end].decode('utf-8')
      else:
        self.topic_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_type = str[start:end].decode('utf-8')
      else:
        self.topic_type = str[start:end]
      start = end
      end += 1
      (self.pub_as_list,) = _struct_B.unpack(str[start:end])
      self.pub_as_list = bool(self.pub_as_list)
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
      length = len(self.annotation_ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation_ids:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
      _x = self.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.topic_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.pub_as_list))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.annotation_ids is None:
        self.annotation_ids = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation_ids = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation_ids.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_name = str[start:end].decode('utf-8')
      else:
        self.topic_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic_type = str[start:end].decode('utf-8')
      else:
        self.topic_type = str[start:end]
      start = end
      end += 1
      (self.pub_as_list,) = _struct_B.unpack(str[start:end])
      self.pub_as_list = bool(self.pub_as_list)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_16B = struct.Struct("<16B")
_struct_16s = struct.Struct("<16s")
"""autogenerated by genpy from world_canvas_msgs/PubAnnotationsDataResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PubAnnotationsDataResponse(genpy.Message):
  _md5sum = "b543fbd3518c791be28589b850702201"
  _type = "world_canvas_msgs/PubAnnotationsDataResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
bool result
string message


"""
  __slots__ = ['result','message']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       result,message

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PubAnnotationsDataResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = False
      if self.message is None:
        self.message = ''
    else:
      self.result = False
      self.message = ''

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
      buff.write(_struct_B.pack(self.result))
      _x = self.message
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
      end = 0
      start = end
      end += 1
      (self.result,) = _struct_B.unpack(str[start:end])
      self.result = bool(self.result)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
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
      buff.write(_struct_B.pack(self.result))
      _x = self.message
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
      end = 0
      start = end
      end += 1
      (self.result,) = _struct_B.unpack(str[start:end])
      self.result = bool(self.result)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class PubAnnotationsData(object):
  _type          = 'world_canvas_msgs/PubAnnotationsData'
  _md5sum = 'efc54bf1b4a6309b22d598d89ee85d1f'
  _request_class  = PubAnnotationsDataRequest
  _response_class = PubAnnotationsDataResponse