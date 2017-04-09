
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import state
import unknown_tlv
class tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/grace-lsa/tlvs/tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: TLV entry in the Grace LSA, advertised by a system undergoing
graceful restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__unknown_tlv',)

  _yang_name = 'tlv'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_tlv = YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'grace-lsa', u'tlvs', u'tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/state (container)

    YANG Description: Per-TLV state parameters of the Grace LSA
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Per-TLV state parameters of the Grace LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_tlv(self):
    """
    Getter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/unknown_tlv (container)

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
    return self.__unknown_tlv
      
  def _set_unknown_tlv(self, v, load=False):
    """
    Setter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/unknown_tlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_tlv() directly.

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_tlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_tlv(self):
    self.__unknown_tlv = YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_tlv = __builtin__.property(_get_unknown_tlv)


  _pyangbind_elements = {'state': state, 'unknown_tlv': unknown_tlv, }


import state
import unknown_tlv
class tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/grace-lsa/tlvs/tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: TLV entry in the Grace LSA, advertised by a system undergoing
graceful restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__unknown_tlv',)

  _yang_name = 'tlv'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_tlv = YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'grace-lsa', u'tlvs', u'tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/state (container)

    YANG Description: Per-TLV state parameters of the Grace LSA
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Per-TLV state parameters of the Grace LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_tlv(self):
    """
    Getter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/unknown_tlv (container)

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
    return self.__unknown_tlv
      
  def _set_unknown_tlv(self, v, load=False):
    """
    Setter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs/tlv/unknown_tlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_tlv() directly.

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_tlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_tlv(self):
    self.__unknown_tlv = YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_tlv = __builtin__.property(_get_unknown_tlv)


  _pyangbind_elements = {'state': state, 'unknown_tlv': unknown_tlv, }


