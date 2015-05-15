"""autogenerated by genpy from world_canvas_msgs/SaveAnnotationsDataRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import world_canvas_msgs.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class SaveAnnotationsDataRequest(genpy.Message):
  _md5sum = "d204dc5afba8bb6886ec4a83711f9c6e"
  _type = "world_canvas_msgs/SaveAnnotationsDataRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


Annotation[] annotations
AnnotationData[] data

================================================================================
MSG: world_canvas_msgs/Annotation
# Annotation: a generic descriptor for an element (object) in a semantic map
# An annotation can be used to introspect, visualize or key into database filters/searches without
# having to touch the described object directly
#  - timestamp : Creation/last update time
#  - world     : World the object belongs to
#  - id        : Annotation unique id
#  - data_id   : Referenced object unique id (an object can be reference by 1 or more annotations)
#  - name      : Referenced object name
#  - type      : Referenced object type (a message type, as world canvas objects are ROS messages)
#  - shape     : One of 1 (CUBE), 2 (SPHERE), 3 (CYLINDER), 9 (TEXT)
#  - color     : R, G, B, A (optional)
#  - size      : X, Y, Z (optional)
#  - keywords  : Generic properties of this object: allows basic filtering without introspecting
#                the object itself
#  - relationships : List of associated annotations, used for retrieving operational sets of objects

# General properties
time timestamp
uuid_msgs/UniqueID id
uuid_msgs/UniqueID data_id
string world
string name
string type

# Physical properties
int32  shape
std_msgs/ColorRGBA color
geometry_msgs/Vector3 size
geometry_msgs/PoseWithCovarianceStamped pose

# Querying properties
string[] keywords
uuid_msgs/UniqueID[] relationships

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/PoseWithCovarianceStamped
# This expresses an estimated pose with a reference coordinate frame and timestamp

Header header
PoseWithCovariance pose

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
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: world_canvas_msgs/AnnotationData
# Data for an element in a semantic map stored as a byte array generated by ros::serialization
# These objects are unique, although they can be referenced by one or more annotations
#  - id   : Object unique id; data_id field on Annotation messages point to this uuid
#  - type : Object type; duplicated from annotation for convenience on deserialization
#  - data : Serialized data
uuid_msgs/UniqueID id
string type
uint8[] data

"""
  __slots__ = ['annotations','data']
  _slot_types = ['world_canvas_msgs/Annotation[]','world_canvas_msgs/AnnotationData[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       annotations,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SaveAnnotationsDataRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.annotations is None:
        self.annotations = []
      if self.data is None:
        self.data = []
    else:
      self.annotations = []
      self.data = []

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
      length = len(self.annotations)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotations:
        _v1 = val1.timestamp
        _x = _v1
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _v2 = val1.id
        _x = _v2.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _v3 = val1.data_id
        _x = _v3.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _x = val1.world
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.shape))
        _v4 = val1.color
        _x = _v4
        buff.write(_struct_4f.pack(_x.r, _x.g, _x.b, _x.a))
        _v5 = val1.size
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.pose
        _v7 = _v6.header
        buff.write(_struct_I.pack(_v7.seq))
        _v8 = _v7.stamp
        _x = _v8
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v7.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v9 = _v6.pose
        _v10 = _v9.pose
        _v11 = _v10.position
        _x = _v11
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v12 = _v10.orientation
        _x = _v12
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_36d.pack(*_v9.covariance))
        length = len(val1.keywords)
        buff.write(_struct_I.pack(length))
        for val2 in val1.keywords:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *val2))
          else:
            buff.write(struct.pack('<I%ss'%length, length, val2))
        length = len(val1.relationships)
        buff.write(_struct_I.pack(length))
        for val2 in val1.relationships:
          _x = val2.uuid
          # - if encoded as a list instead, serialize as bytes instead of string
          if type(_x) in [list, tuple]:
            buff.write(_struct_16B.pack(*_x))
          else:
            buff.write(_struct_16s.pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _v13 = val1.id
        _x = _v13.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
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
      if self.annotations is None:
        self.annotations = None
      if self.data is None:
        self.data = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotations = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.Annotation()
        _v14 = val1.timestamp
        _x = _v14
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        _v15 = val1.id
        start = end
        end += 16
        _v15.uuid = str[start:end]
        _v16 = val1.data_id
        start = end
        end += 16
        _v16.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.world = str[start:end].decode('utf-8')
        else:
          val1.world = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (val1.shape,) = _struct_i.unpack(str[start:end])
        _v17 = val1.color
        _x = _v17
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _struct_4f.unpack(str[start:end])
        _v18 = val1.size
        _x = _v18
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v19 = val1.pose
        _v20 = _v19.header
        start = end
        end += 4
        (_v20.seq,) = _struct_I.unpack(str[start:end])
        _v21 = _v20.stamp
        _x = _v21
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v20.frame_id = str[start:end].decode('utf-8')
        else:
          _v20.frame_id = str[start:end]
        _v22 = _v19.pose
        _v23 = _v22.pose
        _v24 = _v23.position
        _x = _v24
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v25 = _v23.orientation
        _x = _v25
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v22.covariance = _struct_36d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.keywords = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.keywords.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.relationships = []
        for i in range(0, length):
          val2 = uuid_msgs.msg.UniqueID()
          start = end
          end += 16
          val2.uuid = str[start:end]
          val1.relationships.append(val2)
        self.annotations.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.AnnotationData()
        _v26 = val1.id
        start = end
        end += 16
        _v26.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        self.data.append(val1)
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
      length = len(self.annotations)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotations:
        _v27 = val1.timestamp
        _x = _v27
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _v28 = val1.id
        _x = _v28.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _v29 = val1.data_id
        _x = _v29.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _x = val1.world
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.shape))
        _v30 = val1.color
        _x = _v30
        buff.write(_struct_4f.pack(_x.r, _x.g, _x.b, _x.a))
        _v31 = val1.size
        _x = _v31
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v32 = val1.pose
        _v33 = _v32.header
        buff.write(_struct_I.pack(_v33.seq))
        _v34 = _v33.stamp
        _x = _v34
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v33.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v35 = _v32.pose
        _v36 = _v35.pose
        _v37 = _v36.position
        _x = _v37
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v38 = _v36.orientation
        _x = _v38
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_v35.covariance.tostring())
        length = len(val1.keywords)
        buff.write(_struct_I.pack(length))
        for val2 in val1.keywords:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *val2))
          else:
            buff.write(struct.pack('<I%ss'%length, length, val2))
        length = len(val1.relationships)
        buff.write(_struct_I.pack(length))
        for val2 in val1.relationships:
          _x = val2.uuid
          # - if encoded as a list instead, serialize as bytes instead of string
          if type(_x) in [list, tuple]:
            buff.write(_struct_16B.pack(*_x))
          else:
            buff.write(_struct_16s.pack(_x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _v39 = val1.id
        _x = _v39.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_struct_16B.pack(*_x))
        else:
          buff.write(_struct_16s.pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
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
      if self.annotations is None:
        self.annotations = None
      if self.data is None:
        self.data = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotations = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.Annotation()
        _v40 = val1.timestamp
        _x = _v40
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        _v41 = val1.id
        start = end
        end += 16
        _v41.uuid = str[start:end]
        _v42 = val1.data_id
        start = end
        end += 16
        _v42.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.world = str[start:end].decode('utf-8')
        else:
          val1.world = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (val1.shape,) = _struct_i.unpack(str[start:end])
        _v43 = val1.color
        _x = _v43
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _struct_4f.unpack(str[start:end])
        _v44 = val1.size
        _x = _v44
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v45 = val1.pose
        _v46 = _v45.header
        start = end
        end += 4
        (_v46.seq,) = _struct_I.unpack(str[start:end])
        _v47 = _v46.stamp
        _x = _v47
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v46.frame_id = str[start:end].decode('utf-8')
        else:
          _v46.frame_id = str[start:end]
        _v48 = _v45.pose
        _v49 = _v48.pose
        _v50 = _v49.position
        _x = _v50
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v51 = _v49.orientation
        _x = _v51
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v48.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.keywords = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.keywords.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.relationships = []
        for i in range(0, length):
          val2 = uuid_msgs.msg.UniqueID()
          start = end
          end += 16
          val2.uuid = str[start:end]
          val1.relationships.append(val2)
        self.annotations.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.AnnotationData()
        _v52 = val1.id
        start = end
        end += 16
        _v52.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        self.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_36d = struct.Struct("<36d")
_struct_16B = struct.Struct("<16B")
_struct_4f = struct.Struct("<4f")
_struct_4d = struct.Struct("<4d")
_struct_16s = struct.Struct("<16s")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
"""autogenerated by genpy from world_canvas_msgs/SaveAnnotationsDataResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SaveAnnotationsDataResponse(genpy.Message):
  _md5sum = "b543fbd3518c791be28589b850702201"
  _type = "world_canvas_msgs/SaveAnnotationsDataResponse"
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
      super(SaveAnnotationsDataResponse, self).__init__(*args, **kwds)
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
class SaveAnnotationsData(object):
  _type          = 'world_canvas_msgs/SaveAnnotationsData'
  _md5sum = '60d78492918896c3c2a6be65553f2c9e'
  _request_class  = SaveAnnotationsDataRequest
  _response_class = SaveAnnotationsDataResponse
