class CustomSet:
    

    def __init__(self):
        self.items = []

    def add(self, item: str):
        if item not in self.items:
            self.items.append(item)
    
    def remove(self, item: str):
        if item in self.items:
            self.items.remove(item)
        elif item not in self.items:
            raise KeyError(f"Item {item} is not found")
        

    def as_list(self) -> list[str]:
        return self.items

    def clear(self): 
        self.items.clear()








def main():

    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list()) # ["item 1", "item 2"]

    my_set.remove("item 2")
    print(my_set.as_list()) # ["item 1"]

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list()) # []









if __name__ == "__main__":
    main()
    



