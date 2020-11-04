from mock_data.shopify import shopify_api

class Shopify:
    def __init__(self):
        pass

    def get_products(self):
        """Retrieves clean formatted products

        :return: formatted products
        :rtype: List
        """
        formatted_products = []
        resp = shopify_api
        for product in resp.get('products'):
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
        formatted['name'] = product.get('title')
        formatted['in_stock'] = False
        # Variants (Includes prices here since variants can be different prices)
        for variant in product.get('variants', []):
            formatted_variant = self._format_variant(variant)
            if formatted_variant.get('inventory'):
                formatted['in_stock'] = True
            variants.append(formatted_variant)
        formatted['variants'] = variants
        # Options
        if product.get('options'):
            options = [{option.get('name').lower(): option.get('values')} for option in product['options']]
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
            'code': price['price'].get('currency_code') if price.get('price') else None,
            'amount': price['price'].get('amount') if price.get('price') else None,
            'compare': price['compare_at_price'].get('amount') if price.get('compare_at_price') else None
        } for price in variant.get('presentment_prices')]
        formatted['inventory'] = variant.get('inventory_quantity')
        formatted['weight'] = {'weight': variant.get('weight'), 'unit': variant.get('weight_unit')}
        return formatted
