import csv
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen

class SubjectWindow(Screen):
    pass

###         topics          ###

class MathsWindow(Screen):
    
    def goToCard(self,subjectParam,topicParam,screenNameParam):
        global topic
        global subject
        global screenName
        screenName = screenNameParam
        subject = subjectParam
        topic = topicParam
        sm.current = "cardWin"

class FurtherMathsWindow(Screen):
    
    def goToCard(self,subjectParam,topicParam,screenNameParam):
        global topic
        global subject
        global screenName
        screenName = screenNameParam
        subject = subjectParam
        topic = topicParam
        sm.current = "cardWin"


class CompSciWindow(Screen):
    
    def goToCard(self,subjectParam,topicParam,screenNameParam):
        global topic
        global subject
        global screenName
        screenName = screenNameParam
        subject = subjectParam
        topic = topicParam
        sm.current = "cardWin"


class EconomicsWindow(Screen):
    
    def goToCard(self,subjectParam,topicParam,screenNameParam):
        global topic
        global subject
        global screenName
        screenName = screenNameParam
        subject = subjectParam
        topic = topicParam
        sm.current = "cardWin"


###         topics          ###


class CardWindow(Screen):

    def on_enter(self):
        global topic
        global subject

        self.Question_state = True
        self.current = 0

        directory = "Excel/"+subject+"/"+topic+".csv"
        self.theme_list = []
        with open(directory, 'rt') as text_file:
            reader = csv.reader(text_file)
            self.theme_list = list(reader)

        self.listLength = len(self.theme_list)
        self.pageNumber.text = str(self.current+1) + " / " + str(self.listLength)
        self.cardLabel.text = self.theme_list[self.current][0]


    def last(self):

        if self.current == 0 and self.Question_state == True:
            pass

        elif self.Question_state == True:
            self.current -= 1
            self.pageNumber.text = str(self.current+1) + " / " + str(self.listLength)
            answer = list(str(self.theme_list[self.current][1]))

            if answer[0] == 'A':
                self.cardLabel.text = str(self.theme_list[self.current][1])
                self.Question_state = False
            
            else:
                self.cardLabel.text = ""
                self.cardImage.source = str(self.theme_list[self.current][1])
                self.Question_state = False

        elif self.Question_state == False:
            self.cardImage.source = 'Images/card.gif'
            self.cardLabel.text = str(self.theme_list[self.current][0])
            self.Question_state = True


    def next(self):

        if self.current == len(self.theme_list) - 1:
            pass

        elif self.Question_state == False:  # change to question
            self.current += 1
            self.cardImage.source = 'Images/card.gif'
            self.cardLabel.text = str(self.theme_list[self.current][0])
            self.Question_state = True
            self.pageNumber.text = str(self.current+1) + " / " + str(self.listLength)

        elif self.Question_state == True:
            answer = list(str(self.theme_list[self.current][1]))

            if answer[0] == 'A':    # display text
                self.cardLabel.text = str(self.theme_list[self.current][1])
                self.Question_state = False

            else:   # display image
                self.cardLabel.text = ""
                self.cardImage.source = str(self.theme_list[self.current][1])
                self.Question_state = False


    def back(self):
        global screenName
        sm.current = screenName



Builder.load_file("ui.kv")

class MyMainApp(App):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(SubjectWindow(name="SubjectWin"))
        sm.add_widget(MathsWindow(name="MathsWin"))
        sm.add_widget(FurtherMathsWindow(name="FurtherMathsWin"))
        sm.add_widget(CompSciWindow(name="CompSciWin"))
        sm.add_widget(EconomicsWindow(name="EconomicsWin"))
        sm.add_widget(CardWindow(name="cardWin"))
        return sm


if __name__== "__main__":
    MyMainApp().run()