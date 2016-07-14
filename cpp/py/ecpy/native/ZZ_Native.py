from library import *

class ZZ_Native(Structure):
  _fields_ = [("x", c_void_p)]

  def __add__(s, a):
    if not isinstance(a, ZZ_Native):
      a = ZZ_create(a)
    return cast(lib.ZZ_add(LPZZ(s), LPZZ(a)), LPZZ).contents

  def __neg__(s):
    return cast(lib.ZZ_neg(LPZZ(s)), LPZZ).contents

  def __mul__(s, a):
    if not isinstance(a, ZZ_Native):
      a = ZZ_create(a)
    return cast(lib.ZZ_mul(LPZZ(s), LPZZ(a)), LPZZ).contents

  def __div__(s, a):
    if not isinstance(a, ZZ_Native):
      a = ZZ_create(a)
    return cast(lib.ZZ_div(LPZZ(s), LPZZ(a)), LPZZ).contents

  def __mod__(s, a):
    if not isinstance(a, ZZ_Native):
      a = ZZ_create(a)
    return cast(lib.ZZ_mod(LPZZ(s), LPZZ(a)), LPZZ).contents

  def __str__(s):
    return cast(lib.ZZ_to_string(LPZZ(s)), c_char_p).value

  def __del__(s):
    lib.ZZ_destroy(LPZZ(s))

LPZZ = POINTER(ZZ_Native)

def ZZ_create(x):
  return cast(lib.ZZ_create(str(x)), LPZZ).contents
