import webbrowser
class Tmovies():
    def __init__(self,mtitle,mstoryline,mposter,mtrailer):
        self.title=mtitle
        self.tagline=mstoryline
        self.poster=mposter
        self.trailer_youtube_url=mtrailer
    def trailer_see(self):
        webbrowser.open(self.trailer_youtube_url)
