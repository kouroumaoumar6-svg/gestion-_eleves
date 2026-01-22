from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from database import Database

class StudentApp(App):
    def build(self):
        self.db = Database()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Champs de saisie
        self.first_name_input = TextInput(hint_text="Prénom")
        self.last_name_input = TextInput(hint_text="Nom")
        self.class_input = TextInput(hint_text="Classe")
        self.phone_input = TextInput(hint_text="Téléphone")

        # Bouton d'ajout
        add_btn = Button(text="Ajouter Élève", on_press=self.add_student)
        
        # Zone d'affichage
        self.display_label = Label(text="Liste des élèves s'affichera ici", size_hint_y=None, height=200)

        self.layout.add_widget(self.first_name_input)
        self.layout.add_widget(self.last_name_input)
        self.layout.add_widget(self.class_input)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(add_btn)
        self.layout.add_widget(self.display_label)

        self.refresh_student_list()
        return self.layout

    def add_student(self, instance):
        from student import Student
        s = Student(
            first_name=self.first_name_input.text,
            last_name=self.last_name_input.text,
            class_name=self.class_input.text,
            phone=self.phone_input.text
        )
        self.db.add_student(s)
        self.refresh_student_list()
        # Réinitialiser les champs
        self.first_name_input.text = ""
        self.last_name_input.text = ""

    def refresh_student_list(self):
        students = self.db.get_all_students()
        text = "\n".join([f"{s.last_name} {s.first_name} ({s.class_name})" for s in students])
        self.display_label.text = text or "Aucun élève"

    def on_stop(self):
        self.db.close()

StudentApp().run()
