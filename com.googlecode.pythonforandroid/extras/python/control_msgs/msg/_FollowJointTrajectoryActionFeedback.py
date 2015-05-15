"""autogenerated by genpy from control_msgs/FollowJointTrajectoryActionFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import trajectory_msgs.msg
import control_msgs.msg
import genpy
import actionlib_msgs.msg
import std_msgs.msg

class FollowJointTrajectoryActionFeedback(genpy.Message):
  _md5sum = "d8920dc4eae9fc107e00999cce4be641"
  _type = "control_msgs/FollowJointTrajectoryActionFeedback"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
FollowJointTrajectoryFeedback feedback

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
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: control_msgs/FollowJointTrajectoryFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
Header header
string[] joint_names
trajectory_msgs/JointTrajectoryPoint desired
trajectory_msgs/JointTrajectoryPoint actual
trajectory_msgs/JointTrajectoryPoint error


================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start

"""
  __slots__ = ['header','status','feedback']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalStatus','control_msgs/FollowJointTrajectoryFeedback']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,status,feedback

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FollowJointTrajectoryActionFeedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = control_msgs.msg.FollowJointTrajectoryFeedback()
    else:
      self.header = std_msgs.msg.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.feedback = control_msgs.msg.FollowJointTrajectoryFeedback()

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
      _x = self
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.feedback.header.seq, _x.feedback.header.stamp.secs, _x.feedback.header.stamp.nsecs))
      _x = self.feedback.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.feedback.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.feedback.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.feedback.desired.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.desired.positions))
      length = len(self.feedback.desired.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.desired.velocities))
      length = len(self.feedback.desired.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.desired.accelerations))
      length = len(self.feedback.desired.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.desired.effort))
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.desired.time_from_start.secs, _x.feedback.desired.time_from_start.nsecs))
      length = len(self.feedback.actual.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.actual.positions))
      length = len(self.feedback.actual.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.actual.velocities))
      length = len(self.feedback.actual.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.actual.accelerations))
      length = len(self.feedback.actual.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.actual.effort))
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.actual.time_from_start.secs, _x.feedback.actual.time_from_start.nsecs))
      length = len(self.feedback.error.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.error.positions))
      length = len(self.feedback.error.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.error.velocities))
      length = len(self.feedback.error.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.error.accelerations))
      length = len(self.feedback.error.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.feedback.error.effort))
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.error.time_from_start.secs, _x.feedback.error.time_from_start.nsecs))
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
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = control_msgs.msg.FollowJointTrajectoryFeedback()
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
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.feedback.header.seq, _x.feedback.header.stamp.secs, _x.feedback.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.feedback.joint_names = []
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
        self.feedback.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.positions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.velocities = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.accelerations = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.effort = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 8
      (_x.feedback.desired.time_from_start.secs, _x.feedback.desired.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.positions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.velocities = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.accelerations = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.effort = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 8
      (_x.feedback.actual.time_from_start.secs, _x.feedback.actual.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.positions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.velocities = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.accelerations = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.effort = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 8
      (_x.feedback.error.time_from_start.secs, _x.feedback.error.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.feedback.header.seq, _x.feedback.header.stamp.secs, _x.feedback.header.stamp.nsecs))
      _x = self.feedback.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.feedback.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.feedback.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.feedback.desired.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.desired.positions.tostring())
      length = len(self.feedback.desired.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.desired.velocities.tostring())
      length = len(self.feedback.desired.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.desired.accelerations.tostring())
      length = len(self.feedback.desired.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.desired.effort.tostring())
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.desired.time_from_start.secs, _x.feedback.desired.time_from_start.nsecs))
      length = len(self.feedback.actual.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.actual.positions.tostring())
      length = len(self.feedback.actual.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.actual.velocities.tostring())
      length = len(self.feedback.actual.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.actual.accelerations.tostring())
      length = len(self.feedback.actual.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.actual.effort.tostring())
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.actual.time_from_start.secs, _x.feedback.actual.time_from_start.nsecs))
      length = len(self.feedback.error.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.error.positions.tostring())
      length = len(self.feedback.error.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.error.velocities.tostring())
      length = len(self.feedback.error.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.error.accelerations.tostring())
      length = len(self.feedback.error.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.feedback.error.effort.tostring())
      _x = self
      buff.write(_struct_2i.pack(_x.feedback.error.time_from_start.secs, _x.feedback.error.time_from_start.nsecs))
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
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = control_msgs.msg.FollowJointTrajectoryFeedback()
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
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.feedback.header.seq, _x.feedback.header.stamp.secs, _x.feedback.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.feedback.joint_names = []
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
        self.feedback.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.desired.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 8
      (_x.feedback.desired.time_from_start.secs, _x.feedback.desired.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.actual.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 8
      (_x.feedback.actual.time_from_start.secs, _x.feedback.actual.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.feedback.error.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 8
      (_x.feedback.error.time_from_start.secs, _x.feedback.error.time_from_start.nsecs,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2I = struct.Struct("<2I")
_struct_2i = struct.Struct("<2i")
