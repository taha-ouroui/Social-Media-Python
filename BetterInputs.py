class BetterInputs:

    defaultErrorMsg = "Input is not a numeric value."

    # Custom static input method for int
    @staticmethod
    def input_int(msg : str, errMsg : str = defaultErrorMsg) -> int :
        inputFinished = False
        finalInput = 0

        while not inputFinished:
            userInput = input(msg)

            if userInput.isdigit():
                finalInput = int(userInput)
                inputFinished = True
            else:
                print(errMsg)
        
        return finalInput
    
    ##########################################################

    # Custom static input method for float
    @staticmethod
    def input_float(msg : str, errMsg : str = defaultErrorMsg) -> float:
        inputFinished = False
        finalInput = 0

        while not inputFinished:
            userInput = input(msg)
            isFloat = False

            # isdigit is of no use here, so we use error catching instead
            try:
                userInput = float(userInput)
                isFloat = True
            except ValueError:
                isFloat = False

            if isFloat:
                finalInput = userInput
                inputFinished = True
            else:
                print(errMsg)
        
        return finalInput