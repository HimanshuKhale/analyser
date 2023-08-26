import json
import certifi
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class Interface(BoxLayout):
    def clear(self):
        self.ids.label.text=""
        self.ids.textInput.text=""
    def fetched(self, req_body, result):
        polarity=result[0]
        subjectivity=result[1]
        self.ids.label.text=f"Polarity: {polarity}\n Subjectivity: {subjectivity} "
    def analyze(self):
        data= json.dumps({"sentence": self.ids.textInput.text})
        UrlRequest(url="https://text-analyser-smoky.vercel.app/analyze/",
                   on_success=self.fetched,
                   req_body=data,
                   req_headers={"Content-Type":"application/json; charset=utf-8"},
                   ca_file=certifi.where(),
                   verify=True)


class AnalyserApp(App):
    pass

AnalyserApp().run()