"""autogenerated by genpy from rocon_std_msgs/Strings.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Strings(genpy.Message):
  _md5sum = "58fa1e54e6c0338b3faebae82a13e892"
  _type = "rocon_std_msgs/Strings"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Strings used in the rocon framework.

################################ Versions ####################################

# Rocon versions come from the names of classical composers.
#
# ACDC - http://en.wikipedia.org/?title=AC/DC
#     Australian, awesome and on a highway to hell.

string ROCON_VERSION=acdc

######################## Rocon URIS ###########################################

# These are a convenience to help avoid typos and make easy lookups whatever
# language you are in. The real deal is in rocon_uri/yaml/rules.yaml - make
# sure these stay up to date with respect to each other (TODO: perhaps an
# autogenerator of this msg file?).

###### GENERAL IDENTIFIERS ######

string URI_WILDCARD=*

###### HARDWARE_PLATFORMS ######
string HW_PC=pc
string HW_TURTLEBOT2=turtlebot2
string HW_PR2=pr2
string HW_WAITERBOT=waiterbot
string HW_ROBOT_OTHER=robot_other
# Phones
string HW_GALAXY=galaxy
string HW_MEGA=mega
string HW_NOTE3=note3
string HW_PHONE_OTHER=phone_other
# Tablets
string HW_XOOM=xoom
string HW_NOTE10=note10
string HW_TABLET_OTHER=tablet_other

###### APPLICATION_FRAMEWORKS ######
string APPLICATION_FRAMEWORK_OTHER=application_framework_other
string APPLICATION_FRAMEWORK_OPROS=opros
# Ros
string APPLICATION_FRAMEWORK_GROOVY=groovy
string APPLICATION_FRAMEWORK_HYDRO=hydro
string APPLICATION_FRAMEWORK_INDIGO=indigo
string APPLICATION_FRAMEWORK_ROS_OTHER=ros_other

###### OPERATING SYSTEMS ######
string OS_OSX=osx
string OS_FREEBSD=freebsd
# Windows
string OS_WINXP=winxp
string OS_WINDOWS7=windows7
# linux
string OS_ARCH=arch
string OS_DEBIAN=debian
string OS_FEDORA=fedora
string OS_GENTOO=gentoo
# linux/ubuntu 
string OS_PRECISE=precise
string OS_QUANTAL=quantal
string OS_RARING=raring
string OS_SAUCY=saucy
# Android
string OS_HONEYCOMB=honeycomb
string OS_ICE_CREAM_SANDWICH=ice_cream_sandwich
string OS_JELLYBEAN=jellybean
string OS_KITKAT=kitkat
# Web
string OS_CHROME=chrome
string OS_FIREFOX=firefox
string OS_INTERNET_EXPLORER=internet_explorer
string OS_SAFARI=safari
string OS_OPERA=opera

######################## Rocon Export Tags################################

# Package exports used in concert_service_manager and rocon_app_utilities
string TAG_SERVICE=concert_service
string TAG_RAPP=rocon_app
string TAG_GAZEBO_ROBOT_TYPE=concert_gazebo
string TAG_SOFTWARE=software_farm

"""
  # Pseudo-constants
  ROCON_VERSION = 'acdc'
  URI_WILDCARD = '*'
  HW_PC = 'pc'
  HW_TURTLEBOT2 = 'turtlebot2'
  HW_PR2 = 'pr2'
  HW_WAITERBOT = 'waiterbot'
  HW_ROBOT_OTHER = 'robot_other'
  HW_GALAXY = 'galaxy'
  HW_MEGA = 'mega'
  HW_NOTE3 = 'note3'
  HW_PHONE_OTHER = 'phone_other'
  HW_XOOM = 'xoom'
  HW_NOTE10 = 'note10'
  HW_TABLET_OTHER = 'tablet_other'
  APPLICATION_FRAMEWORK_OTHER = 'application_framework_other'
  APPLICATION_FRAMEWORK_OPROS = 'opros'
  APPLICATION_FRAMEWORK_GROOVY = 'groovy'
  APPLICATION_FRAMEWORK_HYDRO = 'hydro'
  APPLICATION_FRAMEWORK_INDIGO = 'indigo'
  APPLICATION_FRAMEWORK_ROS_OTHER = 'ros_other'
  OS_OSX = 'osx'
  OS_FREEBSD = 'freebsd'
  OS_WINXP = 'winxp'
  OS_WINDOWS7 = 'windows7'
  OS_ARCH = 'arch'
  OS_DEBIAN = 'debian'
  OS_FEDORA = 'fedora'
  OS_GENTOO = 'gentoo'
  OS_PRECISE = 'precise'
  OS_QUANTAL = 'quantal'
  OS_RARING = 'raring'
  OS_SAUCY = 'saucy'
  OS_HONEYCOMB = 'honeycomb'
  OS_ICE_CREAM_SANDWICH = 'ice_cream_sandwich'
  OS_JELLYBEAN = 'jellybean'
  OS_KITKAT = 'kitkat'
  OS_CHROME = 'chrome'
  OS_FIREFOX = 'firefox'
  OS_INTERNET_EXPLORER = 'internet_explorer'
  OS_SAFARI = 'safari'
  OS_OPERA = 'opera'
  TAG_SERVICE = 'concert_service'
  TAG_RAPP = 'rocon_app'
  TAG_GAZEBO_ROBOT_TYPE = 'concert_gazebo'
  TAG_SOFTWARE = 'software_farm'

  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Strings, self).__init__(*args, **kwds)

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
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
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
      pass
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
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
