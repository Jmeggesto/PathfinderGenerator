class Game:
    @staticmethod
    def choose_index_from_options(options):
        print("Choose:")
        for i in range(len(options)):
            print("     {}. {}".format(i, options[i]))
        choice = -1
        while not (0 <= choice < len(options)):
            choice = input("Enter the number of your choice: ")
        return choice
