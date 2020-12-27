# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hunter_local_planner/TrajectoryPointMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg

class TrajectoryPointMsg(genpy.Message):
  _md5sum = "4c309845772249e786605716950755c3"
  _type = "hunter_local_planner/TrajectoryPointMsg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Message that contains single point on a trajectory suited for mobile navigation.
# The trajectory is described by a sequence of poses, velocities,
# accelerations and temporal information.

# Why this message type?
# nav_msgs/Path describes only a path without temporal information.
# trajectory_msgs package contains only messages for joint trajectories.

# The pose of the robot
geometry_msgs/Pose pose

# Corresponding velocity
geometry_msgs/Twist velocity

# Corresponding acceleration
geometry_msgs/Twist acceleration

duration time_from_start




================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
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
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['pose','velocity','acceleration','time_from_start']
  _slot_types = ['geometry_msgs/Pose','geometry_msgs/Twist','geometry_msgs/Twist','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pose,velocity,acceleration,time_from_start

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrajectoryPointMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Twist()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Twist()
      if self.time_from_start is None:
        self.time_from_start = genpy.Duration()
    else:
      self.pose = geometry_msgs.msg.Pose()
      self.velocity = geometry_msgs.msg.Twist()
      self.acceleration = geometry_msgs.msg.Twist()
      self.time_from_start = genpy.Duration()

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
      buff.write(_get_struct_19d2i().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.velocity.linear.x, _x.velocity.linear.y, _x.velocity.linear.z, _x.velocity.angular.x, _x.velocity.angular.y, _x.velocity.angular.z, _x.acceleration.linear.x, _x.acceleration.linear.y, _x.acceleration.linear.z, _x.acceleration.angular.x, _x.acceleration.angular.y, _x.acceleration.angular.z, _x.time_from_start.secs, _x.time_from_start.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Twist()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Twist()
      if self.time_from_start is None:
        self.time_from_start = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 160
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.velocity.linear.x, _x.velocity.linear.y, _x.velocity.linear.z, _x.velocity.angular.x, _x.velocity.angular.y, _x.velocity.angular.z, _x.acceleration.linear.x, _x.acceleration.linear.y, _x.acceleration.linear.z, _x.acceleration.angular.x, _x.acceleration.angular.y, _x.acceleration.angular.z, _x.time_from_start.secs, _x.time_from_start.nsecs,) = _get_struct_19d2i().unpack(str[start:end])
      self.time_from_start.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_19d2i().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.velocity.linear.x, _x.velocity.linear.y, _x.velocity.linear.z, _x.velocity.angular.x, _x.velocity.angular.y, _x.velocity.angular.z, _x.acceleration.linear.x, _x.acceleration.linear.y, _x.acceleration.linear.z, _x.acceleration.angular.x, _x.acceleration.angular.y, _x.acceleration.angular.z, _x.time_from_start.secs, _x.time_from_start.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Twist()
      if self.acceleration is None:
        self.acceleration = geometry_msgs.msg.Twist()
      if self.time_from_start is None:
        self.time_from_start = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 160
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.velocity.linear.x, _x.velocity.linear.y, _x.velocity.linear.z, _x.velocity.angular.x, _x.velocity.angular.y, _x.velocity.angular.z, _x.acceleration.linear.x, _x.acceleration.linear.y, _x.acceleration.linear.z, _x.acceleration.angular.x, _x.acceleration.angular.y, _x.acceleration.angular.z, _x.time_from_start.secs, _x.time_from_start.nsecs,) = _get_struct_19d2i().unpack(str[start:end])
      self.time_from_start.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_19d2i = None
def _get_struct_19d2i():
    global _struct_19d2i
    if _struct_19d2i is None:
        _struct_19d2i = struct.Struct("<19d2i")
    return _struct_19d2i
