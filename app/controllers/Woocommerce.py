from mock_data.woocommerce import woo_api, woo_variations


class Woocommerce:
    def __init__(self):
        pass

    def get_products(self):
        """Retrieves clean formatted products

        :return: formatted products
        :rtype: List
        """
        formatted_products = []
        resp = woo_api
        for product in resp:
            formatted = self._format_product(product)
            formatted_products.append(formatted)
        return formatted_products

    def _format_product(self, product):
        """Formats and filters a products data

        :param product: Product data
        :type product: Dict
        :return: Formatted product data
        :rtype: Dict
        """
        formatted = {}
        variants = []
        formatted['id'] = product.get('id')
        formatted['name'] = product.get('name')
        formatted['in_stock'] = True if product.get('stock_status') == 'instock' else False
        # Variants (Includes prices here since variants can be different prices)
        for variant in product.get('variations', []):
            formatted_variant = self._format_variant(variant)
            variants.append(formatted_variant)
        formatted['variants'] = variants
        # Options
        if product.get('attributes'):
            options = [{attribute.get('name').lower(): attribute.get('options')} for attribute in product['attributes']]
        elif product.get('default_attributes'):
            options = [{attribute.get('name').lower(): [attribute.get('option')]} for attribute in product['default_attributes']]
        else:
            options = {}
        formatted['options'] = options
        return formatted

    def _format_variant(self, variant):
        """Formats the variant data within a product

        :param variant: Product variant data
        :type variant: Dict
        :return: Formatted variant data
        :rtype: Dict
        """
        formatted = {}
        formatted['id'] = variant.get('id')
        formatted['prices'] = [{
            'code': None,
            'amount': variant.get('price'),
            'compare': variant.get('regular_price')
        }]
        formatted['inventory'] = variant.get('stock_quantity')
        formatted['weight'] = variant.get('weight')
        return formatted
