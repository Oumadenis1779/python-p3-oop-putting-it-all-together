#!/usr/bin/env python3

class Book:
    def __init__ (self,title,page_count):
        self.title=title
        self._page_count=272
        self.current_page = 1

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count=property(get_page_count,set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    pass

soldiers=Book("we are the soldiers",272)
print(soldiers.title)
print(soldiers.page_count)
soldiers.page_count=300
print(soldiers.page_count)
print(soldiers.turn_page)


    
        