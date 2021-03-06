"""autogenerated by genpy from gateway_msgs/RemoteGatewayInfoRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RemoteGatewayInfoRequest(genpy.Message):
  _md5sum = "e005eaac1f4b29980f211758e562aa6e"
  _type = "gateway_msgs/RemoteGatewayInfoRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

string[] gateways

"""
  __slots__ = ['gateways']
  _slot_types = ['string[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gateways

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RemoteGatewayInfoRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.gateways is None:
        self.gateways = []
    else:
      self.gateways = []

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
      length = len(self.gateways)
      buff.write(_struct_I.pack(length))
      for val1 in self.gateways:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.gateways = []
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
        self.gateways.append(val1)
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
      length = len(self.gateways)
      buff.write(_struct_I.pack(length))
      for val1 in self.gateways:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.gateways = []
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
        self.gateways.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
"""autogenerated by genpy from gateway_msgs/RemoteGatewayInfoResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import gateway_msgs.msg

class RemoteGatewayInfoResponse(genpy.Message):
  _md5sum = "21c329af996537695f35402c601485df"
  _type = "gateway_msgs/RemoteGatewayInfoResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """RemoteGateway[] gateways


================================================================================
MSG: gateway_msgs/RemoteGateway
###### Gateway information ######
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
  __slots__ = ['gateways']
  _slot_types = ['gateway_msgs/RemoteGateway[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gateways

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RemoteGatewayInfoResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.gateways is None:
        self.gateways = []
    else:
      self.gateways = []

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
      length = len(self.gateways)
      buff.write(_struct_I.pack(length))
      for val1 in self.gateways:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.ip
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(val1.firewall))
        _v1 = val1.conn_stats
        _x = _v1
        buff.write(_struct_Bq4fBbfb2f.pack(_x.gateway_available, _x.time_since_last_seen, _x.ping_latency_min, _x.ping_latency_max, _x.ping_latency_avg, _x.ping_latency_mdev, _x.network_info_available, _x.network_type, _x.wireless_bitrate, _x.wireless_link_quality, _x.wireless_signal_level, _x.wireless_noise_level))
        length = len(val1.public_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.public_interface:
          _x = val2.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.flipped_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.flipped_interface:
          _x = val2.gateway
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v2 = val2.rule
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
        length = len(val1.pulled_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pulled_interface:
          _x = val2.gateway
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v3 = val2.rule
          _x = _v3.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v3.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v3.node
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
      if self.gateways is None:
        self.gateways = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.gateways = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteGateway()
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
          val1.ip = str[start:end].decode('utf-8')
        else:
          val1.ip = str[start:end]
        start = end
        end += 1
        (val1.firewall,) = _struct_B.unpack(str[start:end])
        val1.firewall = bool(val1.firewall)
        _v4 = val1.conn_stats
        _x = _v4
        start = end
        end += 40
        (_x.gateway_available, _x.time_since_last_seen, _x.ping_latency_min, _x.ping_latency_max, _x.ping_latency_avg, _x.ping_latency_mdev, _x.network_info_available, _x.network_type, _x.wireless_bitrate, _x.wireless_link_quality, _x.wireless_signal_level, _x.wireless_noise_level,) = _struct_Bq4fBbfb2f.unpack(str[start:end])
        _v4.gateway_available = bool(_v4.gateway_available)
        _v4.network_info_available = bool(_v4.network_info_available)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.public_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.Rule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.type = str[start:end].decode('utf-8')
          else:
            val2.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8')
          else:
            val2.node = str[start:end]
          val1.public_interface.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.flipped_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.RemoteRule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.gateway = str[start:end].decode('utf-8')
          else:
            val2.gateway = str[start:end]
          _v5 = val2.rule
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v5.type = str[start:end].decode('utf-8')
          else:
            _v5.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v5.name = str[start:end].decode('utf-8')
          else:
            _v5.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v5.node = str[start:end].decode('utf-8')
          else:
            _v5.node = str[start:end]
          val1.flipped_interface.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pulled_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.RemoteRule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.gateway = str[start:end].decode('utf-8')
          else:
            val2.gateway = str[start:end]
          _v6 = val2.rule
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v6.type = str[start:end].decode('utf-8')
          else:
            _v6.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v6.name = str[start:end].decode('utf-8')
          else:
            _v6.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v6.node = str[start:end].decode('utf-8')
          else:
            _v6.node = str[start:end]
          val1.pulled_interface.append(val2)
        self.gateways.append(val1)
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
      length = len(self.gateways)
      buff.write(_struct_I.pack(length))
      for val1 in self.gateways:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.ip
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(val1.firewall))
        _v7 = val1.conn_stats
        _x = _v7
        buff.write(_struct_Bq4fBbfb2f.pack(_x.gateway_available, _x.time_since_last_seen, _x.ping_latency_min, _x.ping_latency_max, _x.ping_latency_avg, _x.ping_latency_mdev, _x.network_info_available, _x.network_type, _x.wireless_bitrate, _x.wireless_link_quality, _x.wireless_signal_level, _x.wireless_noise_level))
        length = len(val1.public_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.public_interface:
          _x = val2.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.flipped_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.flipped_interface:
          _x = val2.gateway
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v8 = val2.rule
          _x = _v8.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v8.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v8.node
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.pulled_interface)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pulled_interface:
          _x = val2.gateway
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v9 = val2.rule
          _x = _v9.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v9.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = _v9.node
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
      if self.gateways is None:
        self.gateways = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.gateways = []
      for i in range(0, length):
        val1 = gateway_msgs.msg.RemoteGateway()
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
          val1.ip = str[start:end].decode('utf-8')
        else:
          val1.ip = str[start:end]
        start = end
        end += 1
        (val1.firewall,) = _struct_B.unpack(str[start:end])
        val1.firewall = bool(val1.firewall)
        _v10 = val1.conn_stats
        _x = _v10
        start = end
        end += 40
        (_x.gateway_available, _x.time_since_last_seen, _x.ping_latency_min, _x.ping_latency_max, _x.ping_latency_avg, _x.ping_latency_mdev, _x.network_info_available, _x.network_type, _x.wireless_bitrate, _x.wireless_link_quality, _x.wireless_signal_level, _x.wireless_noise_level,) = _struct_Bq4fBbfb2f.unpack(str[start:end])
        _v10.gateway_available = bool(_v10.gateway_available)
        _v10.network_info_available = bool(_v10.network_info_available)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.public_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.Rule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.type = str[start:end].decode('utf-8')
          else:
            val2.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.node = str[start:end].decode('utf-8')
          else:
            val2.node = str[start:end]
          val1.public_interface.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.flipped_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.RemoteRule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.gateway = str[start:end].decode('utf-8')
          else:
            val2.gateway = str[start:end]
          _v11 = val2.rule
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v11.type = str[start:end].decode('utf-8')
          else:
            _v11.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v11.name = str[start:end].decode('utf-8')
          else:
            _v11.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v11.node = str[start:end].decode('utf-8')
          else:
            _v11.node = str[start:end]
          val1.flipped_interface.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pulled_interface = []
        for i in range(0, length):
          val2 = gateway_msgs.msg.RemoteRule()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.gateway = str[start:end].decode('utf-8')
          else:
            val2.gateway = str[start:end]
          _v12 = val2.rule
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v12.type = str[start:end].decode('utf-8')
          else:
            _v12.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v12.name = str[start:end].decode('utf-8')
          else:
            _v12.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v12.node = str[start:end].decode('utf-8')
          else:
            _v12.node = str[start:end]
          val1.pulled_interface.append(val2)
        self.gateways.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_Bq4fBbfb2f = struct.Struct("<Bq4fBbfb2f")
class RemoteGatewayInfo(object):
  _type          = 'gateway_msgs/RemoteGatewayInfo'
  _md5sum = '21b6c2a53d6cebe0c03f90dd0c85b58d'
  _request_class  = RemoteGatewayInfoRequest
  _response_class = RemoteGatewayInfoResponse
