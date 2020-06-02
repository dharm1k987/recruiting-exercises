#!/usr/bin/python
# -*- coding: utf-8 -*-


class InventoryAllocator:

    """
    Class dedicated to finding the best way to ship out orders based on inventory space of warehouses.
    """

    def allocate(self, order, inventory):
        '''(InventoryAllocator, dict, list of dicts) -> list of dicts

        Find an optimal distribution of items based on order and inventory space.

        order:
            A dictionary mapping items being ordered and their quantities
        inventory:
            A list of dictionary objects mapping warehouse name to inventory amounts.

        >>> invAlc = InventoryAllocator()
        >>> invAlc.allocate({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}])
        [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        '''

        result = []

        if not order or not inventory:
            return result

        # initialize the starting basket
        hand_basket = dict()
        for food in order.keys():
            hand_basket[food] = 0

        # go through each store, and try to fill up the order
        for store in inventory:
            name = store['name']

            # initialize the store basket (what can go in the store)
            store_basket = dict()

            # initialize the completed foods (if we have fully allocated this food, it will go in here)
            completed_foods = []

            for food in hand_basket.keys():

                # see if the current store has this food
                if food in store['inventory']:

                    # the amount we can put into this store
                    num_allowed_in_store = store['inventory'][food]

                    # the amount we need to put in this store is our order - what we already put
                    num_need_to_put = order[food] - hand_basket[food]

                    if num_need_to_put > 0 and num_allowed_in_store > 0:

                        # if there is space in the store
                        if num_allowed_in_store >= num_need_to_put:

                            # add it to the store basket, and mark this food as completed
                            # since we have allocated all of it
                            store_basket[food] = num_need_to_put
                            completed_foods.append(food)
                        else:

                            # there is not enough space in the store
                            # so, put how much is allowed
                            store_basket[food] = num_allowed_in_store
                            hand_basket[food] += num_allowed_in_store

            # we are done this store, so add to results
            if store_basket:
                result.append({name: store_basket})

            for food in completed_foods:

                # this has to be done outside, because otherwise we change the dict size
                # while in a loop, and this is not allowed
                del hand_basket[food]

            if not hand_basket:
                return result

        return []


if __name__ == '__main__':
    import doctest
    doctest.testmod()
