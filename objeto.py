class Conferencias:
    def __init__(self, id, name, description, date, place):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.place = place

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_date(self):
        return self.date
    
    def get_place(self):
        return self.place