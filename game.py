class Game:
    @staticmethod
    def choose_index_from_options(options):
        print("Choose:")
        for i in range(len(options)):
            print("     {}. {}".format(i, options[i]))
        choice = -1
        while not (0 <= choice < len(options)):
            try:
                choice = int(raw_input("Enter the number of your choice: "))
            except ValueError:
                print("Please enter a number.")
        return choice
