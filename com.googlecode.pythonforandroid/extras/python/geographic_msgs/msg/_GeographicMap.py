"""autogenerated by genpy from geographic_msgs/GeographicMap.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import geographic_msgs.msg
import std_msgs.msg

class GeographicMap(genpy.Message):
  _md5sum = "0f4ce6d2ebf9ac9c7c4f3308f6ae0731"
  _type = "geographic_msgs/GeographicMap"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Geographic map for a specified region.

Header header            # stamp specifies time
                         # frame_id (normally /map)

uuid_msgs/UniqueID id    # identifier for this map
BoundingBox  bounds      # 2D bounding box containing map

WayPoint[]   points      # way-points
MapFeature[] features    # map features
KeyValue[]   props       # map properties

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

================================================================================
MSG: geographic_msgs/BoundingBox
# Geographic map bounding box. 
#
# The two GeoPoints denote diagonally opposite corners of the box.
#
# If min_pt.latitude is NaN, the bounding box is "global", matching
# any valid latitude, longitude and altitude.
#
# If min_pt.altitude is NaN, the bounding box is two-dimensional and
# matches any altitude within the specified latitude and longitude
# range.

GeoPoint min_pt         # lowest and most Southwestern corner
GeoPoint max_pt         # highest and most Northeastern corner

================================================================================
MSG: geographic_msgs/GeoPoint
# Geographic point, using the WGS 84 reference ellipsoid.

# Latitude [degrees]. Positive is north of equator; negative is south
# (-90 <= latitude <= +90).
float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is
# west (-180 <= longitude <= +180). At the poles, latitude is -90 or
# +90, and longitude is irrelevant, but must be in range.
float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).
float64 altitude

================================================================================
MSG: geographic_msgs/WayPoint
# Way-point element for a geographic map.

uuid_msgs/UniqueID id   # Unique way-point identifier
GeoPoint   position     # Position relative to WGS 84 ellipsoid
KeyValue[] props        # Key/value properties for this point

================================================================================
MSG: geographic_msgs/KeyValue
# Geographic map tag (key, value) pair
#
# This is equivalent to diagnostic_msgs/KeyValue, repeated here to
# avoid introducing a trivial stack dependency.

string key                     # tag label
string value                   # corresponding value

================================================================================
MSG: geographic_msgs/MapFeature
# Geographic map feature.
#
# A list of WayPoint IDs for features like streets, highways, hiking
# trails, the outlines of buildings and parking lots in sequential
# order.
#
# Feature lists may also contain other feature lists as members.

uuid_msgs/UniqueID   id         # Unique feature identifier
uuid_msgs/UniqueID[] components # Sequence of feature components
KeyValue[] props                # Key/value properties for this feature

"""
  __slots__ = ['header','id','bounds','points','features','props']
  _slot_types = ['std_msgs/Header','uuid_msgs/UniqueID','geographic_msgs/BoundingBox','geographic_msgs/WayPoint[]','geographic_msgs/MapFeature[]','geographic_msgs/KeyValue[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id,bounds,points,features,props

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GeographicMap, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.bounds is None:
        self.bounds = geographic_msgs.msg.BoundingBox()
      if self.points is None:
        self.points = []
      if self.features is None:
        self.features = []
      if self.props is None:
        self.props = []
    else:
      self.header = std_msgs.msg.Header()
      self.id = uuid_msgs.msg.UniqueID()
      self.bounds = geographic_msgs.msg.BoundingBox()
      self.points = []
      self.features = []
      self.props = []

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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self
      buff.write(_struct_6d.pack(_x.bounds.min_pt.latitude, _x.bounds.min_pt.longitude, _x.bounds.min_pt.altitude, _x.bounds.max_pt.latitude, _x.bounds.max_pt.longitude, _x.bounds.max_pt.altitude))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _v1 = val1.id
        _x = _v1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _v2 = val1.position
        _x = _v2
        buff.write(_struct_3d.pack(_x.latitude, _x.longitude, _x.altitude))
        length = len(val1.props)
        buff.write(_struct_I.pack(length))
        for val2 in val1.props:
          _x = val2.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.features)
      buff.write(_struct_I.pack(length))
      for val1 in self.features:
        _v3 = val1.id
        _x = _v3.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        length = len(val1.components)
        buff.write(_struct_I.pack(length))
        for val2 in val1.components:
          _x = val2.uuid
          # - if encoded as a list instead, serialize as bytes instead of string
          if type(_x) in [list, tuple]:
            buff.write(_struct_16B.pack(*_x))
          else:
            buff.write(_struct_16s.pack(_x))
        length = len(val1.props)
        buff.write(_struct_I.pack(length))
        for val2 in val1.props:
          _x = val2.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.props)
      buff.write(_struct_I.pack(length))
      for val1 in self.props:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.bounds is None:
        self.bounds = geographic_msgs.msg.BoundingBox()
      if self.points is None:
        self.points = None
      if self.features is None:
        self.features = None
      if self.props is None:
        self.props = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 16
      self.id.uuid = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.bounds.min_pt.latitude, _x.bounds.min_pt.longitude, _x.bounds.min_pt.altitude, _x.bounds.max_pt.latitude, _x.bounds.max_pt.longitude, _x.bounds.max_pt.altitude,) = _struct_6d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.WayPoint()
        _v4 = val1.id
        start = end
        end += 16
        _v4.uuid = str[start:end]
        _v5 = val1.position
        _x = _v5
        start = end
        end += 24
        (_x.latitude, _x.longitude, _x.altitude,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.props = []
        for i in range(0, length):
          val2 = geographic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.key = str[start:end].decode('utf-8')
          else:
            val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.props.append(val2)
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.features = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.MapFeature()
        _v6 = val1.id
        start = end
        end += 16
        _v6.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.components = []
        for i in range(0, length):
          val2 = uuid_msgs.msg.UniqueID()
          start = end
          end += 16
          val2.uuid = str[start:end]
          val1.components.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.props = []
        for i in range(0, length):
          val2 = geographic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.key = str[start:end].decode('utf-8')
          else:
            val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.props.append(val2)
        self.features.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.props = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8')
        else:
          val1.value = str[start:end]
        self.props.append(val1)
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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_16B.pack(*_x))
      else:
        buff.write(_struct_16s.pack(_x))
      _x = self
      buff.write(_struct_6d.pack(_x.bounds.min_pt.latitude, _x.bounds.min_pt.longitude, _x.bounds.min_pt.altitude, _x.bounds.max_pt.latitude, _x.bounds.max_pt.longitude, _x.bounds.max_pt.altitude))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _v7 = val1.id
        _x = _v7.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _v8 = val1.position
        _x = _v8
        buff.write(_struct_3d.pack(_x.latitude, _x.longitude, _x.altitude))
        length = len(val1.props)
        buff.write(_struct_I.pack(length))
        for val2 in val1.props:
          _x = val2.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.features)
      buff.write(_struct_I.pack(length))
      for val1 in self.features:
        _v9 = val1.id
        _x = _v9.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        length = len(val1.components)
        buff.write(_struct_I.pack(length))
        for val2 in val1.components:
          _x = val2.uuid
          # - if encoded as a list instead, serialize as bytes instead of string
          if type(_x) in [list, tuple]:
            buff.write(_struct_16B.pack(*_x))
          else:
            buff.write(_struct_16s.pack(_x))
        length = len(val1.props)
        buff.write(_struct_I.pack(length))
        for val2 in val1.props:
          _x = val2.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.props)
      buff.write(_struct_I.pack(length))
      for val1 in self.props:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = uuid_msgs.msg.UniqueID()
      if self.bounds is None:
        self.bounds = geographic_msgs.msg.BoundingBox()
      if self.points is None:
        self.points = None
      if self.features is None:
        self.features = None
      if self.props is None:
        self.props = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 16
      self.id.uuid = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.bounds.min_pt.latitude, _x.bounds.min_pt.longitude, _x.bounds.min_pt.altitude, _x.bounds.max_pt.latitude, _x.bounds.max_pt.longitude, _x.bounds.max_pt.altitude,) = _struct_6d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.WayPoint()
        _v10 = val1.id
        start = end
        end += 16
        _v10.uuid = str[start:end]
        _v11 = val1.position
        _x = _v11
        start = end
        end += 24
        (_x.latitude, _x.longitude, _x.altitude,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.props = []
        for i in range(0, length):
          val2 = geographic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.key = str[start:end].decode('utf-8')
          else:
            val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.props.append(val2)
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.features = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.MapFeature()
        _v12 = val1.id
        start = end
        end += 16
        _v12.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.components = []
        for i in range(0, length):
          val2 = uuid_msgs.msg.UniqueID()
          start = end
          end += 16
          val2.uuid = str[start:end]
          val1.components.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.props = []
        for i in range(0, length):
          val2 = geographic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.key = str[start:end].decode('utf-8')
          else:
            val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.props.append(val2)
        self.features.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.props = []
      for i in range(0, length):
        val1 = geographic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8')
        else:
          val1.value = str[start:end]
        self.props.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_3d = struct.Struct("<3d")
_struct_6d = struct.Struct("<6d")
_struct_16B = struct.Struct("<16B")
_struct_16s = struct.Struct("<16s")
