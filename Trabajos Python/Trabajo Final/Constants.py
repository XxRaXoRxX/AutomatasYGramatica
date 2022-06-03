import pandas as pd

class Main():

    def Start(self):
        self.ReadCsv()

    def ReadCsv(self):
        archive = pd.read_excel("Usuarios WiFi.xlsx", "Sheet1", index_col=None, na_values=["NA"])
        print(archive)

main = Main()
main.Start()