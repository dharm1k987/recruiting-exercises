import unittest
from inventory_allocator import InventoryAllocator


class InventoryAllocatorTest(unittest.TestCase):

    def setUp(self):
        self.invAlc = InventoryAllocator()

    def test_happy_case(self):
        print('\nTest: test_happy_case')
        order = {'apple': 1}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 1}}]
        expected = [{'owd': {'apple': 1}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_not_enough_inventory(self):
        print('\nTest: test_not_enough_inventory')
        order = {'apple': 10}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 5}}]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_multi_not_enough_inventory(self):
        print('\nTest: test_multi_not_enough_inventory')
        order = {'apple': 10, 'banana': 5}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 10,
                          'banana': 2}}]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_split_even(self):
        print('\nTest: test_split_even')
        order = {'apple': 10}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 5}},
                          {'name': 'dm', 'inventory': {'apple': 5}}]
        expected = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_split_odd(self):
        print('\nTest: test_split_odd')
        order = {'apple': 10}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 7}},
                          {'name': 'dm', 'inventory': {'apple': 3}}]
        expected = [{'owd': {'apple': 7}}, {'dm': {'apple': 3}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_multi_split_even(self):
        print('\nTest: test_multi_split_even')
        order = {'apple': 10, 'banana': 6}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 5,
                          'banana': 3}}, {'name': 'dm',
                          'inventory': {'apple': 5, 'banana': 3}}]
        expected = [{'owd': {'apple': 5, 'banana': 3}},
                    {'dm': {'apple': 5, 'banana': 3}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_multi_split_odd(self):
        print('\nTest: test_multi_split_odd')
        order = {'apple': 10, 'banana': 6}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 5,
                          'banana': 2}}, {'name': 'dm',
                          'inventory': {'apple': 5, 'banana': 4}}]
        expected = [{'owd': {'apple': 5, 'banana': 2}},
                    {'dm': {'apple': 5, 'banana': 4}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_split_more_than_needed(self):
        print('\nTest: test_split_more_than_needed')
        order = {'apple': 10}
        inventory_dist = [{'name': 'owd', 'inventory': {'apple': 7}},
                          {'name': 'dm', 'inventory': {'apple': 5}}]
        expected = [{'owd': {'apple': 7}}, {'dm': {'apple': 3}}]
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_tricky(self):
        print('\nTest: test_tricky')
        order = {
            'apple': 10,
            'banana': 3,
            'orange': 4,
            'mango': 5,
            'carrot': 6,
            }
        store1 = {'name': 'owd', 'inventory': {'mango': 3, 'apple': 5}}  # 7
        store2 = {'name': 'dm', 'inventory': {'carrot': 7, 'apple': 3}}  # 10
        store3 = {'name': 'bp', 'inventory': {'banana': 1, 'mango': 2,
                  'orange': 3}}  # 6
        store4 = {'name': 'lo', 'inventory': {'apple': 4, 'banana': 1,
                  'orange': 1}}  # 6
        store5 = {'name': 'aw', 'inventory': {'banana': 1, 'carrot': 1,
                  'orange': 1}}  # 3

        inventory_dist = [store5, store4, store3, store1, store2]
        expected = [{'aw': {'banana': 1, 'carrot': 1, 'orange': 1}},
                    {'lo': {'apple': 4, 'banana': 1, 'orange': 1}},
                    {'bp': {'mango': 2, 'banana': 1, 'orange': 2}},
                    {'dm': {'carrot': 5, 'apple': 1}},
                    {'owd': {'apple': 5, 'mango': 3}}]
        self.assertCountEqual(self.invAlc.allocate(order,
                              inventory_dist), expected)
        print('Passed!')

    def test_food_not_in_one_store(self):
        print('\nTest: test_food_not_in_one_store')
        order = {'apple': 5, 'banana': 10}
        store1 = {'name': 'owd', 'inventory': {'mango': 2, 'grapes': 2}}
        store2 = {'name': 'dm', 'inventory': {'banana': 12,
                  'radish': 2}}
        inventory_dist = [store1, store2]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_food_not_in_all_store(self):
        print('\nTest: test_food_not_in_all_store')
        order = {'apple': 5, 'pear': 10}
        store1 = {'name': 'owd', 'inventory': {'mango': 2, 'grapes': 2}}
        store2 = {'name': 'dm', 'inventory': {'banana': 12,
                  'radish': 2}}
        inventory_dist = [store1, store2]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_food_inventory_zero(self):
        print('\nTest: test_food_inventory_zero')
        order = {'apple': 5, 'pear': 10}
        store1 = {'name': 'owd', 'inventory': {'apple': 0, 'pear': 0}}
        store2 = {'name': 'dm', 'inventory': {'banana': 0, 'radish': 0}}
        inventory_dist = [store1, store2]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_no_stores(self):
        print('\nTest: test_no_stores')
        order = {'apple': 5, 'pear': 10}
        inventory_dist = []
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_no_order(self):
        print('\nTest: test_no_order')
        order = []
        inventory_dist = [{'name': 'dm', 'inventory': {'banana': 0,
                          'radish': 0}}]
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')

    def test_no_order_or_store(self):
        print('\nTest: test_no_order_or_store')
        order = []
        inventory_dist = []
        expected = []
        self.assertEqual(self.invAlc.allocate(order, inventory_dist),
                         expected)
        print('Passed!')


if __name__ == '__main__':
    unittest.main()
