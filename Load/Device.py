class Device:
    def __init__(self, product_name, current_price, user_name, user_rating, user_comment, user_time_comment):
        self._product_name = product_name
        self._current_price = current_price  # Thêm current_price
        self._user_name = user_name
        self._user_rating = user_rating
        self._user_comment = user_comment
        self._user_time_comment = user_time_comment
    
    @property
    def product_name(self):
        return self._product_name

    @property
    def current_price(self):
        return self._current_price  # Getter for current_price
    
    @property
    def user_name(self):
        return self._user_name
    
    @property
    def user_rating(self):
        return self._user_rating
    
    @property
    def user_comment(self):
        return self._user_comment
    
    @property
    def user_time_comment(self):
        return self._user_time_comment
