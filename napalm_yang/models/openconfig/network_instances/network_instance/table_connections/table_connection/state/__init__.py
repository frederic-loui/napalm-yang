
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/table-connections/table-connection/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the connection between
tables
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__src_protocol','__address_family','__dst_protocol','__import_policy','__default_import_policy',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__src_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)
    self.__dst_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__address_family = YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__import_policy = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'table-connections', u'table-connection', u'state']

  def _get_src_protocol(self):
    """
    Getter method for src_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/src_protocol (leafref)

    YANG Description: The source protocol for the table connection
    """
    return self.__src_protocol
      
  def _set_src_protocol(self, v, load=False):
    """
    Setter method for src_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/src_protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_protocol() directly.

    YANG Description: The source protocol for the table connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__src_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_protocol(self):
    self.__src_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/address_family (leafref)

    YANG Description: The address family associated with the connection. This
must be defined for the source protocol. The target
address family is implicitly defined by the address family
specified for the source protocol.
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/address_family (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: The address family associated with the connection. This
must be defined for the source protocol. The target
address family is implicitly defined by the address family
specified for the source protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_dst_protocol(self):
    """
    Getter method for dst_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/dst_protocol (leafref)

    YANG Description: The destination protocol for the table connection
    """
    return self.__dst_protocol
      
  def _set_dst_protocol(self, v, load=False):
    """
    Setter method for dst_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/dst_protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_protocol() directly.

    YANG Description: The destination protocol for the table connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__dst_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_protocol(self):
    self.__dst_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)

  src_protocol = __builtin__.property(_get_src_protocol)
  address_family = __builtin__.property(_get_address_family)
  dst_protocol = __builtin__.property(_get_dst_protocol)
  import_policy = __builtin__.property(_get_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy)


  _pyangbind_elements = {'src_protocol': src_protocol, 'address_family': address_family, 'dst_protocol': dst_protocol, 'import_policy': import_policy, 'default_import_policy': default_import_policy, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/table-connections/table-connection/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the connection between
tables
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__src_protocol','__address_family','__dst_protocol','__import_policy','__default_import_policy',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__src_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)
    self.__dst_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__address_family = YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__import_policy = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'table-connections', u'table-connection', u'state']

  def _get_src_protocol(self):
    """
    Getter method for src_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/src_protocol (leafref)

    YANG Description: The source protocol for the table connection
    """
    return self.__src_protocol
      
  def _set_src_protocol(self, v, load=False):
    """
    Setter method for src_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/src_protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_protocol() directly.

    YANG Description: The source protocol for the table connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__src_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_protocol(self):
    self.__src_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/address_family (leafref)

    YANG Description: The address family associated with the connection. This
must be defined for the source protocol. The target
address family is implicitly defined by the address family
specified for the source protocol.
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/address_family (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: The address family associated with the connection. This
must be defined for the source protocol. The target
address family is implicitly defined by the address family
specified for the source protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=unicode, is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_dst_protocol(self):
    """
    Getter method for dst_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/dst_protocol (leafref)

    YANG Description: The destination protocol for the table connection
    """
    return self.__dst_protocol
      
  def _set_dst_protocol(self, v, load=False):
    """
    Setter method for dst_protocol, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/dst_protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_protocol() directly.

    YANG Description: The destination protocol for the table connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__dst_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_protocol(self):
    self.__dst_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="dst-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/table_connections/table_connection/state/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCEPT_ROUTE': {}, u'REJECT_ROUTE': {}},), default=unicode("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=False)

  src_protocol = __builtin__.property(_get_src_protocol)
  address_family = __builtin__.property(_get_address_family)
  dst_protocol = __builtin__.property(_get_dst_protocol)
  import_policy = __builtin__.property(_get_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy)


  _pyangbind_elements = {'src_protocol': src_protocol, 'address_family': address_family, 'dst_protocol': dst_protocol, 'import_policy': import_policy, 'default_import_policy': default_import_policy, }


