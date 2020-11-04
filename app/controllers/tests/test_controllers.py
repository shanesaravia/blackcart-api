from ..Shopify import Shopify

shopify = Shopify()
products = shopify.get_products()

def test_endpoint_format():
    assert isinstance(products, list)

def test_product_keys():
    for product in products:
        wanted_keys = ('id', 'in_stock', 'name', 'options', 'variants')
        assert all(k in product for k in wanted_keys)

def test_product_value_types():
    for product in products:
        assert isinstance(product['id'], int)
        assert isinstance(product['in_stock'], bool)
        assert isinstance(product['name'], str)
        assert isinstance(product['options'], list)
        assert isinstance(product['variants'], list)

def test_variant_keys():
    for product in products:
        for variant in product['variants']:
            wanted_keys = ('id', 'inventory', 'prices', 'weight')
            assert all(k in variant for k in wanted_keys)

def test_variant_value_types():
    for product in products:
        for variant in product['variants']:
            assert isinstance(variant['id'], int)
            assert isinstance(variant['inventory'], int)
            assert isinstance(variant['prices'], list)
            assert isinstance(variant['weight'], dict)

def test_variant_prices_are_float_strings():
    for product in products:
        for variant in product['variants']:
            for prices in variant['prices']:
                assert isinstance(prices['amount'], str)
                assert isinstance(float(prices['amount']), float)