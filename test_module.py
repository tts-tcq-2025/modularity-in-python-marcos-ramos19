from translate import get_color_from_pair_number, get_pair_number_from_color
from manual_reference_table import build_reference_table

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)

def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)
  
def test_manual_output():
  s = build_reference_table()
  lines = s.splitlines()
  assert len(lines) == 28                      
  assert lines[0] == "25-Pair Color Code Reference"
  assert lines[1] == " # | Major  | Minor "
  assert lines[2].startswith("---+")
  assert lines[3].startswith(" 1 | White  | Blue")      
  assert any(l.startswith("12 | Black  | Orange") for l in lines)  
  assert lines[-1].startswith("25 | Violet | Slate")   
  for i, l in enumerate(lines[3:], 1):                 
    assert l.startswith(f"{i:2d} |")
