"""autogenerated by genpy from gazebo_msgs/WorldState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class WorldState(genpy.Message):
  _md5sum = "de1a9de3ab7ba97ac0e9ec01a4eb481e"
  _type = "gazebo_msgs/WorldState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This is a message that holds data necessary to reconstruct a snapshot of the world
#
# = Approach to Message Passing =
# The state of the world is defined by either
#   1. Inertial Model pose, twist
#      * kinematic data - connectivity graph from Model to each Link
#      * joint angles
#      * joint velocities
#      * Applied forces - Body wrench
#        * relative transform from Body to each collision Geom
# Or
#   2. Inertial (absolute) Body pose, twist, wrench
#      * relative transform from Body to each collision Geom - constant, so not sent over wire
#      * back compute from canonical body info to get Model pose and twist.
#
# Chooing (2.) because it matches most physics engines out there
#   and is simpler.
#
# = Future =
# Consider impacts on using reduced coordinates / graph (parent/child links) approach
#   constraint and physics solvers.
#
# = Application =
# This message is used to do the following:
#   * reconstruct the world and objects for sensor generation
#   * stop / start simulation - need pose, twist, wrench of each body
#   * collision detection - need pose of each collision geometry.  velocity/acceleration if 
#
# = Assumptions =
# Assuming that each (physics) processor node locally already has
#   * collision information - Trimesh for Geoms, etc
#   * relative transforms from Body to Geom - this is assumed to be fixed, do not send oved wire
#   * inertial information - does not vary in time
#   * visual information - does not vary in time
#

Header header

string[] name
geometry_msgs/Pose[] pose
geometry_msgs/Twist[] twist
geometry_msgs/Wrench[] wrench

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
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Wrench
# This represents force in free space, separated into
# its linear and angular parts.
Vector3  force
Vector3  torque

"""
  __slots__ = ['header','name','pose','twist','wrench']
  _slot_types = ['std_msgs/Header','string[]','geometry_msgs/Pose[]','geometry_msgs/Twist[]','geometry_msgs/Wrench[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,name,pose,twist,wrench

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WorldState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.name is None:
        self.name = []
      if self.pose is None:
        self.pose = []
      if self.twist is None:
        self.twist = []
      if self.wrench is None:
        self.wrench = []
    else:
      self.header = std_msgs.msg.Header()
      self.name = []
      self.pose = []
      self.twist = []
      self.wrench = []

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
      length = len(self.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.pose:
        _v1 = val1.position
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.twist)
      buff.write(_struct_I.pack(length))
      for val1 in self.twist:
        _v3 = val1.linear
        _x = _v3
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v4 = val1.angular
        _x = _v4
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.wrench)
      buff.write(_struct_I.pack(length))
      for val1 in self.wrench:
        _v5 = val1.force
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.torque
        _x = _v6
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
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
      if self.pose is None:
        self.pose = None
      if self.twist is None:
        self.twist = None
      if self.wrench is None:
        self.wrench = None
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v7 = val1.position
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v8 = val1.orientation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.twist = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Twist()
        _v9 = val1.linear
        _x = _v9
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v10 = val1.angular
        _x = _v10
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.twist.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.wrench = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Wrench()
        _v11 = val1.force
        _x = _v11
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v12 = val1.torque
        _x = _v12
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.wrench.append(val1)
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
      length = len(self.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.pose:
        _v13 = val1.position
        _x = _v13
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v14 = val1.orientation
        _x = _v14
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.twist)
      buff.write(_struct_I.pack(length))
      for val1 in self.twist:
        _v15 = val1.linear
        _x = _v15
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v16 = val1.angular
        _x = _v16
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.wrench)
      buff.write(_struct_I.pack(length))
      for val1 in self.wrench:
        _v17 = val1.force
        _x = _v17
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v18 = val1.torque
        _x = _v18
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
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
      if self.pose is None:
        self.pose = None
      if self.twist is None:
        self.twist = None
      if self.wrench is None:
        self.wrench = None
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v19 = val1.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v20 = val1.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.twist = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Twist()
        _v21 = val1.linear
        _x = _v21
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v22 = val1.angular
        _x = _v22
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.twist.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.wrench = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Wrench()
        _v23 = val1.force
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v24 = val1.torque
        _x = _v24
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.wrench.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_3d = struct.Struct("<3d")
