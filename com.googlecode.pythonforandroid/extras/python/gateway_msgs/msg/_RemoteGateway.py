"""autogenerated by genpy from gateway_msgs/RemoteGateway.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import gateway_msgs.msg

class RemoteGateway(genpy.Message):
  _md5sum = "58607c66cd963e494a28cb3f919087f2"
  _type = "gateway_msgs/RemoteGateway"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """###### Gateway information ######
string name
string ip
#TODO blocking status
bool firewall

# Remote Gateway Statistics

# Constants
int8 WIRED = 1
int8 WIRELESS = 2

#Connection Statistics
ConnectionStatistics conn_stats

###### Public Interface ######

Rule[] public_interface

###### Flipped Interface ######

# Flipped and pulled interfaces would be useful for debugging 
#    https://github.com/robotics-in-concert/rocon_multimaster/issues/84

RemoteRule[] flipped_interface
RemoteRule[] pulled_interface

###### Foreign Interface ######

# Q) Should we show these?
# A) Probably not, in the overall scheme of things, 
#    it doubles up the information from above

# RemoteRule[] flipped_in_connections
# RemoteRule[] pulled_connections

================================================================================
MSG: gateway_msgs/ConnectionStatistics
# Constants
int8 WIRED = 1
int8 WIRELESS = 2
int32 MAX_TTL = 86400

# Gateway ping indicators
bool gateway_available
int64 time_since_last_seen #time in seconds since last ping successful
float32 ping_latency_min
float32 ping_latency_max
float32 ping_latency_avg
float32 ping_latency_mdev #mean absolute deviation

# Gateway network information indicators
bool network_info_available
int8 network_type
float32 wireless_bitrate
int8 wireless_link_quality
float32 wireless_signal_level
float32 wireless_noise_level



================================================================================
MSG: gateway_msgs/Rule
# Standard gateway connection rule

# type of connection (from gateway_msgs.msg.Connection)
string type

# this is the topic/service name or the action base name (a regex is supported)
string name 

# (optional) an optional node name can be provided. if node name is not provided
# then all nodes are matched (also supports regex)
string node

================================================================================
MSG: gateway_msgs/RemoteRule
# Definition for a flip. It represents either:
#
# 1) an existing flipped connection (from the local gateway)
# 2) a rule that is put on a watchlist

# The target recipient of the flip
string gateway

# Connection has the following parameters that need setting
# - name : fully qualified name of the connection (str)
# - type : connection type (str)
#  
# Use one of the types defined in Connection string constants:
#     (publisher, subscriber, service, action_client, action_server)
#
# - node : name of the node it originates from (str)(optional)
#
# Node name is necessary, for instance, if you have multiple subscribers
# publishing to a single topic. Most of the time it is not necessary,
# but in some cases it helps refine the rule. It helps refine the rule.
#
Rule rule

"""
  # Pseudo-constants
  WIRED = 1
  WIRELESS = 2

  __slots__ = ['name','ip','firewall','conn_stats','public_interface','flipped_interface','pulled_interface']
  _slot_types = ['string','string','bool','gateway_msgs/ConnectionStatistics','gateway_msgs/Rule[]','gateway_msgs/RemoteRule[]','gateway_msgs/RemoteRule[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,ip,firewall,conn_stats,public_interface,flipped_interface,pulled_interface

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RemoteGateway, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.ip is None:
        self.ip = ''
      if self.firewall is None:
        self.firewall = False
      if self.conn_stats is None:
        self.conn_stats = gateway_msgs.msg.ConnectionStatistics()
      if self.public_interface is None:
        self.public_interface = []
      if self.flipped_interface is None:
        self.flipped_interface = []
      if self.pulled_interface is None:
        self.pulled_interface = []
    else:
      self.name = ''
      self.ip = ''
      self.firewall = False
      self.conn_stats = gateway_msgs.msg.ConnectionStatistics()
      self.public_interface = []
      self.flipped_interface = []
      self.pulled_interface = []

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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.ip
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2Bq4fBbfb2f.pack(_x.firewall, _x.conn_stats.gateway_available, _x.conn_stats.time_since_last_seen, _x.conn_stats.ping_latency_min, _x.conn_stats.ping_latency_max, _x.conn_stats.ping_latency_avg, _x.conn_stats.ping_latency_mdev, _x.conn_stats.network_info_available, _x.conn_stats.network_type, _x.conn_stats.wireless_bitrate, _x.conn_stats.wireless_link_quality, _x.conn_stats.wireless_signal_level, _x.conn_stats.wireless_noise_level))
      length = len(self.public_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.public_interface:
        _x = val1.type
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
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.flipped_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.flipped_interface:
        _x = val1.gateway
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v1 = val1.rule
        _x = _v1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.pulled_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.pulled_interface:
        _x = val1.gateway
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v2 = val1.rule
        _x = _v2.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v2.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v2.node
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
      if self.conn_stats is None:
        self.conn_stats = gateway_msgs.msg.ConnectionStatistics()
      if self.public_interface is None:
        self.public_interface = None
      if self.flipped_interface is None:
        self.flipped_interface = None
      if self.pulled_interface is None:
        self.pulled_interface = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ip = str[start:end].decode('utf-8')
      else:
        self.ip = str[start:end]
      _x = self
      start = end
      end += 41
      (_x.firewall, _x.conn_stats.gateway_available, _x.conn_stats.time_since_last_seen, _x.conn_stats.ping_latency_min, _x.conn_stats.ping_latency_max, _x.conn_stats.ping_latency_avg, _x.conn_stats.ping_latency_mdev, _x.conn_stats.network_info_available, _x.conn_stats.network_type, _x.conn_stats.wireless_bitrate, _x.conn_stats.wireless_link_quality, _x.conn_stats.wireless_signal_level, _x.conn_stats.wireless_noise_level,) = _struct_2Bq4fBbfb2f.unpack(str[start:end])
      self.firewall = bool(self.firewall)
      self.conn_stats.gateway_available = bool(self.conn_stats.gateway_available)
      self.conn_stats.network_info_available = bool(self.conn_stats.network_info_available)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.public_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.Rule()
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
          val1.node = str[start:end].decode('utf-8')
        else:
          val1.node = str[start:end]
        self.public_interface.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flipped_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteRule()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gateway = str[start:end].decode('utf-8')
        else:
          val1.gateway = str[start:end]
        _v3 = val1.rule
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.type = str[start:end].decode('utf-8')
        else:
          _v3.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.name = str[start:end].decode('utf-8')
        else:
          _v3.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.node = str[start:end].decode('utf-8')
        else:
          _v3.node = str[start:end]
        self.flipped_interface.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pulled_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteRule()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gateway = str[start:end].decode('utf-8')
        else:
          val1.gateway = str[start:end]
        _v4 = val1.rule
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.type = str[start:end].decode('utf-8')
        else:
          _v4.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.name = str[start:end].decode('utf-8')
        else:
          _v4.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.node = str[start:end].decode('utf-8')
        else:
          _v4.node = str[start:end]
        self.pulled_interface.append(val1)
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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.ip
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2Bq4fBbfb2f.pack(_x.firewall, _x.conn_stats.gateway_available, _x.conn_stats.time_since_last_seen, _x.conn_stats.ping_latency_min, _x.conn_stats.ping_latency_max, _x.conn_stats.ping_latency_avg, _x.conn_stats.ping_latency_mdev, _x.conn_stats.network_info_available, _x.conn_stats.network_type, _x.conn_stats.wireless_bitrate, _x.conn_stats.wireless_link_quality, _x.conn_stats.wireless_signal_level, _x.conn_stats.wireless_noise_level))
      length = len(self.public_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.public_interface:
        _x = val1.type
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
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.flipped_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.flipped_interface:
        _x = val1.gateway
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v5 = val1.rule
        _x = _v5.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v5.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v5.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.pulled_interface)
      buff.write(_struct_I.pack(length))
      for val1 in self.pulled_interface:
        _x = val1.gateway
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v6 = val1.rule
        _x = _v6.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v6.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v6.node
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
      if self.conn_stats is None:
        self.conn_stats = gateway_msgs.msg.ConnectionStatistics()
      if self.public_interface is None:
        self.public_interface = None
      if self.flipped_interface is None:
        self.flipped_interface = None
      if self.pulled_interface is None:
        self.pulled_interface = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ip = str[start:end].decode('utf-8')
      else:
        self.ip = str[start:end]
      _x = self
      start = end
      end += 41
      (_x.firewall, _x.conn_stats.gateway_available, _x.conn_stats.time_since_last_seen, _x.conn_stats.ping_latency_min, _x.conn_stats.ping_latency_max, _x.conn_stats.ping_latency_avg, _x.conn_stats.ping_latency_mdev, _x.conn_stats.network_info_available, _x.conn_stats.network_type, _x.conn_stats.wireless_bitrate, _x.conn_stats.wireless_link_quality, _x.conn_stats.wireless_signal_level, _x.conn_stats.wireless_noise_level,) = _struct_2Bq4fBbfb2f.unpack(str[start:end])
      self.firewall = bool(self.firewall)
      self.conn_stats.gateway_available = bool(self.conn_stats.gateway_available)
      self.conn_stats.network_info_available = bool(self.conn_stats.network_info_available)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.public_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.Rule()
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
          val1.node = str[start:end].decode('utf-8')
        else:
          val1.node = str[start:end]
        self.public_interface.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flipped_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteRule()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gateway = str[start:end].decode('utf-8')
        else:
          val1.gateway = str[start:end]
        _v7 = val1.rule
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.type = str[start:end].decode('utf-8')
        else:
          _v7.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.name = str[start:end].decode('utf-8')
        else:
          _v7.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.node = str[start:end].decode('utf-8')
        else:
          _v7.node = str[start:end]
        self.flipped_interface.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pulled_interface = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteRule()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gateway = str[start:end].decode('utf-8')
        else:
          val1.gateway = str[start:end]
        _v8 = val1.rule
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.type = str[start:end].decode('utf-8')
        else:
          _v8.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.name = str[start:end].decode('utf-8')
        else:
          _v8.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.node = str[start:end].decode('utf-8')
        else:
          _v8.node = str[start:end]
        self.pulled_interface.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2Bq4fBbfb2f = struct.Struct("<2Bq4fBbfb2f")