from colors import MAJOR_COLORS, MINOR_COLORS
from translator import get_color_from_pair_number

def build_reference_table():
  """
  Devuelve un string imprimible que mapea nombres de colores a su número de par.
  Formato:
   25-Pair Color Code Reference
    # | Major  | Minor
   ---+--------+--------
    1 | White  | Blue
    ...
  """
  total = len(MAJOR_COLORS) * len(MINOR_COLORS)
  lines = [
    "25-Pair Color Code Reference",
    " # | Major  | Minor ",
    "---+--------+--------",
  ]
  for n in range(1, total + 1):
    major, minor = get_color_from_pair_number(n)
    lines.append(f"{n:2d} | {major:<6} | {minor:<6}")
  return "\n".join(lines)
