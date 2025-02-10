
class InventoryApiClient:
    def __init__(self, use_empty_header=False):
        self.host = "https://qxrbiyv22g.execute-api.ap-south-1.amazonaws.com/prod"
        self.client_secret = "9lAp03FjIb6eYjflO8x9U3rSteJnk1VSaVVs8BUp"
        #self.app_api_object = ActivateAppApi(self.host, self.client_secret, use_empty_header)


    def get_health_helper(self):
        """Helper method to get health status."""
        return self.app_api_object.get_health()

    def create_product_helper(self, product_data):
        """Helper method to create a product."""
        return self.app_api_object.create_product(product_data)

    def get_products_helper(self):
        """Helper method to get a list of products."""
        return self.app_api_object.get_products()

    def get_product_helper(self, product_id):
        """Helper method to get a specific product by ID."""
        return self.app_api_object.get_product(product_id)

    def update_product_helper(self, data):
        """Helper method to update a product."""
        return self.app_api_object.update_product(data)

    def delete_product_helper(self, product_id):
        """Helper method to delete a product."""
        return self.app_api_object.delete_product(product_id)
