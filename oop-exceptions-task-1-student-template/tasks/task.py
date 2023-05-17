class Pagination:
    def __init__(self, text, items_on_page):
        self.text = text
        self.items_on_page = items_on_page
        self.item_count = len(text)
        self.page_count = (self.item_count + items_on_page - 1) // items_on_page

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = min(start_index + self.items_on_page, self.item_count)
        return end_index - start_index

    def find_page(self, data):
        if not data:
            raise Exception(f"'{data}' is missing on the pages")
        if len(data) > self.items_on_page:
            return [i for i in range(self.page_count) if data in self.get_page(i)]
        else:
            return [i for i in range(self.page_count) if data in self.text[i*self.items_on_page:(i+1)*self.items_on_page]]

    def display_page(self, page_number):
        return self.get_page(page_number)

    def get_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = min(start_index + self.items_on_page, self.item_count)
        return self.text[start_index:end_index]
