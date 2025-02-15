import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

kivy.require('2.0.0')

class PresentationApp(App):
    def build(self):
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Arrière-plan gris clair de la fenêtre

        self.slides = [
            {"title": "Bienvenue", "content": "Bienvenue chez [Nom de l'entreprise]", "image": "banner.png"},
            {"title": "Mission", "content": "Fournir des produits et services de haute qualité.", "image": "mission.png"},
            {"title": "Valeurs", "content": "Intégrité, Innovation, Service Client.", "image": "valeurs.png"},
            {"title": "Contact", "content": "Email: contact@entreprise.com\nTéléphone: +123 456 7890", "image": "contact.png"}
        ]

        tab_panel = TabbedPanel(do_default_tab=False)
        tab_panel.background_color = (0.7, 1, 0.7, 1)  # Couleur de fond des onglets (vert clair)
        tab_panel.tab_width = 150

        for slide in self.slides:
            tab = TabbedPanelItem(text=slide["title"])
            layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            with layout.canvas.before:
                Color(1, 1, 1, 1)  # Couleur de fond des onglets (blanc)
                Rectangle(size=layout.size, pos=layout.pos)

            image_layout = BoxLayout(size_hint_y=0.5)  # Image occupe 50% de l'espace vertical
            content_layout = BoxLayout(size_hint_y=0.5)  # Contenu occupe 50% de l'espace vertical

            if "image" in slide:
                image_layout.add_widget(Image(source=slide["image"]))

            content_layout.add_widget(Label(text=slide["content"], font_size='18sp', color=(0, 0, 0, 1)))

            layout.add_widget(image_layout)
            layout.add_widget(content_layout)
            tab.add_widget(layout)
            tab_panel.add_widget(tab)

        # Ajouter un onglet avec un programme hebdomadaire
        programme_tab = TabbedPanelItem(text="Programme Hebdomadaire")
        programme_layout = GridLayout(cols=3, padding=10, spacing=10)

        # Ajouter des entêtes de colonne
        programme_layout.add_widget(Label(text="Jour", font_size='18sp', color=(0, 0, 0, 1)))
        programme_layout.add_widget(Label(text="Heure", font_size='18sp', color=(0, 0, 0, 1)))
        programme_layout.add_widget(Label(text="Activité", font_size='18sp', color=(0, 0, 0, 1)))

        # Ajouter des données pour chaque jour de la semaine
        programme = {
            "Lundi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Mardi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Mercredi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Jeudi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Vendredi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Samedi": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")],
            "Dimanche": [("8h00", "Départ"), ("9h00", "Départ"), ("10h00", "Arrivée")]
        }

        for jour, activités in programme.items():
            for heure, activité in activités:
                programme_layout.add_widget(Label(text=jour, font_size='16sp', color=(0, 0, 0, 1)))
                programme_layout.add_widget(Label(text=heure, font_size='16sp', color=(0, 0, 0, 1)))
                programme_layout.add_widget(Label(text=activité, font_size='16sp', color=(0, 0, 0, 1)))
                jour = ""  # Pour éviter de répéter le jour

        programme_tab.add_widget(programme_layout)
        tab_panel.add_widget(programme_tab)

        return tab_panel

if __name__ == '__main__':
    PresentationApp().run()
