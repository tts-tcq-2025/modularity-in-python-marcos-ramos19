import sys
from test_module import test_number_to_pair, test_pair_to_number, test_manual,output
from manual_reference_table import build_reference_table

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  test_manual_output()
  print('Done :)')
