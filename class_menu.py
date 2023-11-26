class Menu:
    def __init__(self, widget_list, screen) -> None:
        self.widget_list = widget_list
        self.dialogue = ""
        self.screen = screen
        self.child_form = None
    
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
    
    def read_dialogue(self):
        dialogue = self.get_dialogue()

        if dialogue  == "Back":
            self.delete_child()
        
    def set_child(self, child):
        self.child_form = child
    
    def delete_child(self):
        self.child_form = None

    def get_dialogue(self):
        return self.child_form.dialogue

    def update(self, event_list):
        if self.child_form == None:
            for widget in self.widget_list:
               
                widget.update(self.screen, event_list)
        else:
            self.child_form.update(event_list)
            self.read_dialogue()
        