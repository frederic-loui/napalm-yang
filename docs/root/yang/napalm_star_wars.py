
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
 import builtins as __builtin__
 long = int
 unicode = str
elif six.PY2:
  import __builtin__

class yc_individual_napalm_star_wars__universe_individual(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module napalm-star-wars - based on the path /universe/individual. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__age','__affiliation',)

  _yang_name = 'individual'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__affiliation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'napalm-star-wars:EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'napalm-star-wars:REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}},), is_leaf=True, yang_name="affiliation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='identityref', is_config=True)
    self.__age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..2000']}), is_leaf=True, yang_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='age', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='string', is_config=True)

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
      return [u'universe', u'individual']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /universe/individual/name (string)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /universe/individual/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='string', is_config=True)


  def _get_age(self):
    """
    Getter method for age, mapped from YANG variable /universe/individual/age (age)
    """
    return self.__age
      
  def _set_age(self, v, load=False):
    """
    Setter method for age, mapped from YANG variable /universe/individual/age (age)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_age() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..2000']}), is_leaf=True, yang_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='age', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """age must be of a type compatible with age""",
          'defined-type': "napalm-star-wars:age",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..2000']}), is_leaf=True, yang_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='age', is_config=True)""",
        })

    self.__age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_age(self):
    self.__age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..2000']}), is_leaf=True, yang_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='age', is_config=True)


  def _get_affiliation(self):
    """
    Getter method for affiliation, mapped from YANG variable /universe/individual/affiliation (identityref)
    """
    return self.__affiliation
      
  def _set_affiliation(self, v, load=False):
    """
    Setter method for affiliation, mapped from YANG variable /universe/individual/affiliation (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_affiliation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_affiliation() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'napalm-star-wars:EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'napalm-star-wars:REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}},), is_leaf=True, yang_name="affiliation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """affiliation must be of a type compatible with identityref""",
          'defined-type': "napalm-star-wars:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'napalm-star-wars:EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'napalm-star-wars:REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}},), is_leaf=True, yang_name="affiliation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='identityref', is_config=True)""",
        })

    self.__affiliation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_affiliation(self):
    self.__affiliation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'napalm-star-wars:EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'EMPIRE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'napalm-star-wars:REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}, u'REBEL_ALLIANCE': {'@namespace': u'https://napalm-yang.readthedocs.io/napalm-star-wars', '@module': u'napalm-star-wars'}},), is_leaf=True, yang_name="affiliation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='identityref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  age = __builtin__.property(_get_age, _set_age)
  affiliation = __builtin__.property(_get_affiliation, _set_affiliation)


  _pyangbind_elements = {'name': name, 'age': age, 'affiliation': affiliation, }


class yc_universe_napalm_star_wars__universe(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module napalm-star-wars - based on the path /universe. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__individual',)

  _yang_name = 'universe'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__individual = YANGDynClass(base=YANGListType("name",yc_individual_napalm_star_wars__universe_individual, yang_name="individual", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="individual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='list', is_config=True)

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
      return [u'universe']

  def _get_individual(self):
    """
    Getter method for individual, mapped from YANG variable /universe/individual (list)
    """
    return self.__individual
      
  def _set_individual(self, v, load=False):
    """
    Setter method for individual, mapped from YANG variable /universe/individual (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_individual is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_individual() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",yc_individual_napalm_star_wars__universe_individual, yang_name="individual", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="individual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """individual must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",yc_individual_napalm_star_wars__universe_individual, yang_name="individual", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="individual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='list', is_config=True)""",
        })

    self.__individual = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_individual(self):
    self.__individual = YANGDynClass(base=YANGListType("name",yc_individual_napalm_star_wars__universe_individual, yang_name="individual", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="individual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='list', is_config=True)

  individual = __builtin__.property(_get_individual, _set_individual)


  _pyangbind_elements = {'individual': individual, }


class napalm_star_wars(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module napalm-star-wars - based on the path /napalm-star-wars. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__universe',)

  _yang_name = 'napalm-star-wars'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__universe = YANGDynClass(base=yc_universe_napalm_star_wars__universe, is_container='container', yang_name="universe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='container', is_config=True)

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
      return []

  def _get_universe(self):
    """
    Getter method for universe, mapped from YANG variable /universe (container)
    """
    return self.__universe
      
  def _set_universe(self, v, load=False):
    """
    Setter method for universe, mapped from YANG variable /universe (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_universe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_universe() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_universe_napalm_star_wars__universe, is_container='container', yang_name="universe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """universe must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_universe_napalm_star_wars__universe, is_container='container', yang_name="universe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='container', is_config=True)""",
        })

    self.__universe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_universe(self):
    self.__universe = YANGDynClass(base=yc_universe_napalm_star_wars__universe, is_container='container', yang_name="universe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://napalm-yang.readthedocs.io/napalm-star-wars', defining_module='napalm-star-wars', yang_type='container', is_config=True)

  universe = __builtin__.property(_get_universe, _set_universe)


  _pyangbind_elements = {'universe': universe, }

