from scrapper.services import BugsMusic, Melon


class ScrapController(object):
    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)


    @staticmethod
    def menu_2(arg):
        Melon(arg)

