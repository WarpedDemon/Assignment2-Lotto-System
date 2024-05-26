import os
import random

#SelectionSort
def SelectionSort(Data):
    # Outer loop runs 'n' times, where n is the length of Data
    for l in range(0, len(Data) - 1):  # O(n)
        p = l  # O(1)
        # Inner loop runs 'n' times in the worst case
        for i in range(l+1, len(Data)):  # O(n)
            if Data[i] < Data[p]:  # O(1)
                p = i # O(1)

        if p != l:  # O(1)
            # Swap elements at indices p and l
            Data[p], Data[l] = Data[l], Data[p]  # O(1)

    # Total time complexity: O(n^2) - Quadratic
    # Total space complexity: O(1) - Constant
    return Data # O(1)


#InsertionSort
def InsertionSort(Data):
    # Outer loop runs 'n-1' times, where n is the length of Data
    for l in range(1, len(Data)):  # O(n)
        current_element = Data[l]  # O(1)
        j = l - 1  # O(1)
        # Inner loop may run up to 'n' times in the worst case
        while j >= 0 and Data[j] > current_element:  # O(n)
            Data[j + 1] = Data[j]  # O(1)
            j -= 1 # O(1)

        Data[j + 1] = current_element  # O(1)

    # Total time complexity: O(n^2) - Quadratic
    # Total space complexity: O(1) - Constant
    return Data # O(1)


#Merge Sort
def MergeSort(Data):

    # Merge function to merge two sorted arrays
    def Merge(left, right):
        result = []  # O(1)
        left_index = right_index = 0  # O(1)

        # Merge the two arrays into a single sorted array
        while left_index < len(left) and right_index < len(right):  # O(n)
            if left[left_index] < right[right_index]:  # O(1)
                result.append(left[left_index])  # O(1)
                left_index += 1  # O(1)
            else: # O(1)
                result.append(right[right_index])  # O(1)
                right_index += 1  # O(1)

        # Add any remaining elements from the left and right arrays
        result.extend(left[left_index:])  # O(n)
        result.extend(right[right_index:])  # O(n)

        return result # O(1)

    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(Data) <= 1:  # O(1)
        return Data # O(1)

    # Divide the array into two halves
    mid = len(Data) // 2  # O(1)
    left = Data[:mid]  # O(n)
    right = Data[mid:]  # O(n)

    # Recursively sort the two halves
    left = MergeSort(left)  # T(n/2)
    right = MergeSort(right)  # T(n/2)

    # Merge the sorted halves
    merge_result = Merge(left, right)  # O(n)

    # Time complexity: T(n) = 2T(n/2) + O(n) -> O(n log n) - Linearithmic
    # Space complexity: O(n) - Linear
    return merge_result # O(1)


def BinarySearch(arr, x):

    # Binary search to find x in arr
    left, right = 0, len(arr) - 1  # O(1)

    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == x:  # O(1)
            return True # O(1)
        elif arr[mid] < x:  # O(1)
            left = mid + 1  # O(1)
        else:  # O(1)
            right = mid - 1  # O(1)

    # Time complexity: O(log n) - Logarithmic
    # Space complexity: O(1) - Constant
    return False  # O(1)


def CheckWinners(Lotto, WinNo):
    # Rules for divisions
    # There are a total of 4 classes/levels of lotto winners.
    # 1st class winner is one whose game-numbers match/contain all 6 PWNs;
    # 2nd class winner is one whose game-numbers contain any 5 PWNs;
    # 3rd class winner is one whose game-numbers contain any 4 PWNs;
    # 4th class winner is one whose game-numbers contain any 3 PWNs or contain the two SWNs.

    # Initialize lists to hold winners for each division
    WinnersDivisionOne = []  # O(1)
    WinnersDivisionTwo = []  # O(1)
    WinnersDivisionThree = []  # O(1)
    WinnersDivisionFour = []  # O(1)

    # Extract Primary Winning Numbers (PWNs) and Secondary Winning Numbers (SWNs)
    PrimaryWinningNumbers = WinNo[0:6]  # O(1)
    SecondaryWinningNumbers = WinNo[6:8]  # O(1)

    # Iterate over each player's numbers
    for Player in Lotto:  # O(n)
        Count = 0  # O(1)
        SecondaryCount = 0  # O(1)

        # Check each number against the winning numbers
        for Number in Player:  # O(m)
            for WinningNumber in PrimaryWinningNumbers:  # O(1)
                if Number == WinningNumber:  # O(1)
                    Count += 1  # O(1)
            for SecondaryWinningNumber in SecondaryWinningNumbers:  # O(1)
                if Number == SecondaryWinningNumber:  # O(1)
                    SecondaryCount += 1  # O(1)
                            
        # Determine the division of the player based on the counts
        if Count == 6:  # O(1)
            WinnersDivisionOne.append(Player)  # O(1)
        if Count == 5:  # O(1)
            WinnersDivisionTwo.append(Player)  # O(1)
        if Count == 4:  # O(1)
            WinnersDivisionThree.append(Player)  # O(1)
        if Count == 3:  # O(1)
            WinnersDivisionFour.append(Player)  # O(1)
        if SecondaryCount == 2:  # O(1)
            WinnersDivisionFour.append(Player)  # O(1)

    # Note: As a rule, if a player is a winner, he/she is considered as a winner of his/her highest class only, not a winner of any lower classes (e.g., if p is 1st class winner, p will not be considered as a 2nd, or 3rd, or 4th class winner, although his/her game-numbers may still meet the winning conditions of lower classes)
    
    # Sort the winner lists
    WinnersDivisionOne.sort()  # O(n log n)
    WinnersDivisionTwo.sort()  # O(m log m)
    WinnersDivisionThree.sort()  # O(p log p)
    WinnersDivisionFour.sort()  # O(q log q)

    # Clean Division One
    for DivisionOneWinner in WinnersDivisionOne[:]:  # O(n)
        if BinarySearch(WinnersDivisionTwo, DivisionOneWinner):  # O(log m)
            WinnersDivisionTwo.remove(DivisionOneWinner)  # O(m)

        if BinarySearch(WinnersDivisionThree, DivisionOneWinner):  # O(log p)
            WinnersDivisionThree.remove(DivisionOneWinner)  # O(p)

        if BinarySearch(WinnersDivisionFour, DivisionOneWinner):  # O(log q)
            WinnersDivisionFour.remove(DivisionOneWinner)  # O(q)

    # Clean Division Two
    for DivisionTwoWinner in WinnersDivisionTwo[:]:  # O(m)
        if BinarySearch(WinnersDivisionThree, DivisionTwoWinner):  # O(log p)
            WinnersDivisionThree.remove(DivisionTwoWinner)  # O(p)

        if BinarySearch(WinnersDivisionFour, DivisionTwoWinner):  # O(log q)
            WinnersDivisionFour.remove(DivisionTwoWinner)  # O(q)

    # Clean Division Three
    for DivisionThreeWinner in WinnersDivisionThree[:]:  # O(p)
        if BinarySearch(WinnersDivisionFour, DivisionThreeWinner):  # O(log q)
            WinnersDivisionFour.remove(DivisionThreeWinner)  # O(q)

    # Time complexity: O(n * m) for the loops + O((n + m + p + q) * log(n + m + p + q)) for the sorting and BinarySearch calls
    # Space complexity: O(1) - Constant space used for variables, O(n + m + p + q) for the WinnersDivision lists
    return WinnersDivisionOne, WinnersDivisionTwo, WinnersDivisionThree, WinnersDivisionFour



def MatchValue(A, B):

    # As a sub-task, develop a new algorithm match_value(A, B), that computes
    # the matching values of two sorted integer arrays A and B and returns the
    # total number of matching values of the two arrays.

    # Initialize variables
    i = j = count = 0  # O(1)

    # Compare elements of A and B until one of the arrays is exhausted
    while i < len(A) and j < len(B):  # O(min(len(A), len(B)))
        if A[i] == B[j]:  # O(1)
            count += 1  # O(1)
            i += 1  # O(1)
            j += 1  # O(1)
        elif A[i] < B[j]:  # O(1)
            i += 1  # O(1)
        else:  # O(1)
            j += 1  # O(1)

    # Time complexity: O(min(len(A), len(B))) - Linear
    # Space complexity: O(1) - Constant
    return count  # O(1)


def CheckLottoStatus(PlayerID, Lotto, WinNo):

    # all 6 Primary winning numbers (PWNs), the <Message> is
    # “You win the game, congratulations!”
    # any 5 PWNs, the <Message > is
    # "You are a 2nd class winner, congratulations!”
    # any 4 PWNs, the <Message > is
    # "You are a 3rd class winner, congratulations!”
    # any 3 PWNs, the <Message > is
    # “You are a 4th class winner , congratulations!”
    # less than 3 PWNs, but the game-numbers contain two SWNs, the <Message> is
    # “You won a 4th-class prize with SWNs, congratulations!”
    # less than 3 PWNs and less than two SWNs, the <Message> is
    # “You are not a winner. Thanks for playing lotto. Good luck next time!”
    # (Note that there are two cases where a player could be a 4th class winner).

    # Check how many numbers from the player's chosen numbers match the winning numbers.
    Player = MatchValue(Lotto[PlayerID], WinNo[0:6])  # O(n)
    PlayerSecondary = MatchValue(Lotto[PlayerID], WinNo[6:8])  # O(n)

    # Determine the player's status message based on the number of matches.
    if Player == 6:  # O(1)
        PlayerMessage = "You win the game, congratulations!"  # O(1)
    if Player == 5:  # O(1)
        PlayerMessage = "You are a 2nd class winner, congratulations!"  # O(1)
    if Player == 4:  # O(1)
        PlayerMessage = "You are a 3rd class winner, congratulations!"  # O(1)
    if Player == 3:  # O(1)
        PlayerMessage = "You are a 4th class winner, congratulations!"  # O(1)
    if Player > 3 and PlayerSecondary == 2:  # O(1)
        PlayerMessage = "You won a 4th-class prize with SWNs, congratulations!"  # O(1)
    if Player > 3 and PlayerSecondary > 2:  # O(1)
        PlayerMessage = "You are not a winner. Thanks for playing lotto. Good luck next time!"  # O(1)
    else:  # O(1)
        PlayerMessage = "You are not a winner. Thanks for playing lotto. Good luck next time!"  # O(1)

    # Return the player's ID, chosen numbers, and status message.
    return PlayerID, Lotto[PlayerID], PlayerMessage  # O(1)


def PreProcess(NumberOfPlayers):

    # Data pre-processing stage: This step/stage sorts all data stored in the key arrays (or lists) to
    # facilitate future processes:
    # (i) It sorts game-numbers for all 1000 players. That is, it sorts the array lotto[ i ][0...5] for all
    # i = 0, 1, 2, ..., 999;
    # (ii) It then sorts the PWNs (i.e., data stored in WinNo[0...5]; and finally
    # (iii) It sorts the SWNs (i.e., data stored in WinNo[6...7].

    # a) Sorting (in data pre-processing stage):
    # To reduce the searching costs, all arrays must be sorted in the data pre-processing
    # stage. For practical purpose, you are required to use
    # (i) Insertion-sort algorithm to sort the PWNs (i.e., sub-array WinNo[0...5]);
    # (ii) Selection-sort algorithm to sort the SWNs (i.e., sub-array WinNo[6...7]); and
    # (iii) Merge-sort algorithm to sort all player’s game-numbers (i.e., array lotto[i]
    # [0...5], for i = 0, 1, 2, ..., 999).
    # b) Searching (for Menu option 2 only):

    # Initialize arrays/lists
    Lotto = []  # O(1)
    for NewPlayer in range(NumberOfPlayers):  # O(NumberOfPlayers)
        Lotto.append([])  # O(1)
    WinNoPrimary = []  # O(1)
    WinNoSecondary = []  # O(1)
    WinNo = []  # O(1)

    # Generate random numbers for each player and sort their numbers
    for Player in range(NumberOfPlayers):  # O(NumberOfPlayers)
        while len(Lotto[Player]) < 6:  # O(1) -> Loop runs at most 6 times
            LottoResult = random.randint(1, 30)  # O(1)
            if LottoResult not in Lotto[Player]:  # O(1)
                Lotto[Player].append(LottoResult)  # O(1)

        Lotto[Player] = MergeSort(Lotto[Player])  # O(6 log 6) -> O(1) because the array length is fixed at 6
    
    # Generate and sort Primary Winning Numbers
    for Index in range(1):  # O(1) -> Loop runs only once
        while len(WinNoPrimary) < 6:  # O(1) -> Loop runs at most 6 times
            LottoResult = random.randint(1, 30)  # O(1)
            if LottoResult not in WinNoPrimary:  # O(1)
                WinNoPrimary.append(LottoResult)  # O(1)

        WinNoPrimary = MergeSort(WinNoPrimary)  # O(6 log 6) -> O(1) because the array length is fixed at 6

        # Generate and sort Secondary Winning Numbers
        while len(WinNoSecondary) < 2:  # O(1) -> Loop runs at most 2 times
            LottoResult = random.randint(1, 30)  # O(1)
            if LottoResult not in WinNoSecondary and LottoResult not in WinNoPrimary:  # O(1)
                WinNoSecondary.append(LottoResult)  # O(1)

        WinNoSecondary = SelectionSort(WinNoSecondary)  # O(2^2) -> O(1) because the array length is fixed at 2

        # Combine Primary and Secondary Winning Numbers
        WinNo = WinNoPrimary + WinNoSecondary  # O(1)

    # Time complexity: O(NumberOfPlayers) + O(NumberOfPlayers) + O(NumberOfPlayers) + O(1) + O(1) + O(1) + O(1)
    # Space complexity: O(NumberOfPlayers) + O(6) + O(6) + O(2) + O(1) + O(1) + O(1) = O(NumberOfPlayers)
    return Lotto, WinNo  # O(1)


def MenuOption1(Lotto, WinNo):

    os.system('clear')  # O(1) - Clears the console (assuming Unix-like system)
    print("------------------------------------------")  # O(1)
    print("The following are this lottery's winning numbers: ", WinNo[0:6], " These are the secondary winning numbers: ", WinNo[6:8])  # O(1)
    
    # Print each player's numbers
    for Player in Lotto:  # O(len(Lotto))
        print(Player)  # O(1)

    Ready = input("Press Any Key To Return To The Main Menu")  # O(1)


def MenuOption2(Lotto, WinNo):

    os.system('clear')  # O(1) - Clears the console (assuming Unix-like system)
    WinnersDivisionOne, WinnersDivisionTwo, WinnersDivisionThree, WinnersDivisionFour = CheckWinners(Lotto, WinNo)  # O(len(Lotto))
    print("------------------------------------------")  # O(1)
    print("Display Statistics Of Winners: ")  # O(1)
    print("Winners In Division One: ", len(WinnersDivisionOne))  # O(1)
    print("Winners In Division Two: ", len(WinnersDivisionTwo))  # O(1)
    print("Winners In Division Three: ", len(WinnersDivisionThree))  # O(1)
    print("Winners In Division Four: ", len(WinnersDivisionFour))  # O(1)

    Ready = input("Press Any Key To Return To The Main Menu")  # O(1)


def MenuOption3(Lotto, WinNo):

    os.system('clear')  # O(1) - Clears the console (assuming Unix-like system)
    print("------------------------------------------")  # O(1)
    print("Check My Lotto Status: ")  # O(1)
    PlayerNumber = input("Please input your player number to check your lottery ticket: ")  # O(1)
    PlayerID = int(PlayerNumber)
    PlayerID, PlayerNumbers, PlayerMessage = CheckLottoStatus(PlayerID, Lotto, WinNo)  # O(1)
    os.system('clear')  # O(1)

    # Display player's status
    print("------------------------------------------")  # O(1)
    print("Player's ID: " + str(PlayerID))  # O(1)
    print("Player's Game Numbers: " + str(PlayerNumbers))  # O(1)
    print("Primary Winning Numbers: " + str(WinNo[0:6]))  # O(1)
    print("Secondary Winning Numbers: " + str(WinNo[6:8]))  # O(1)
    print("Player's Status: " + PlayerMessage)  # O(1)
    print("------------------------------------------")  # O(1)

    Ready = input("Press Any Key To Return To The Main Menu")  # O(1)


def MenuOption4(Active):

    Active = False # O(1)


def MainMenu(Active, Lotto, WinNo):
    
    while Active:  # O(1) - The loop runs as long as Active is True, but the number of iterations is not dependent on the input size.
        os.system('clear')  # O(1) - Clears the console (assuming Unix-like system)
        print("------------------------------------------")  # O(1)
        print("Please Pick One Of The Following Options: ")  # O(1)
        print("    - Option 1 : Show Initialized Data")  # O(1)
        print("    - Option 2 : Display Statistics Of Winners")  # O(1)
        print("    - Option 3 : Check My Lotto Status")  # O(1)
        print("    - Option 4 : Exit")  # O(1)
        print("------------------------------------------")  # O(1)
        
        FirstMenuInput = input("Please enter a menu option number: ")  # O(1)
        
        if FirstMenuInput == "1":  # O(1)
            MenuOption1(Lotto, WinNo)  # O(1)
            FirstMenuInput = None  # O(1)
        if FirstMenuInput == "2":  # O(1)
            MenuOption2(Lotto, WinNo)  # O(1)
            FirstMenuInput = None  # O(1)
        if FirstMenuInput == "3":  # O(1)
            MenuOption3(Lotto, WinNo)  # O(1)
        if FirstMenuInput == "4":  # O(1)
            MenuOption4(Active)  # O(1)
            break  # O(1)


def Init():

    NumberOfPlayers = 1000  # O(1)

    Active = True  # O(1)

    # PreProcess has a time complexity of O(NumberOfPlayers) since it involves iterating over the players to generate their lottery numbers.
    Lotto, WinNo = PreProcess(NumberOfPlayers)

    # MainMenu is called with a time complexity of O(1) because it's a single function call with constant time complexity.
    MainMenu(Active, Lotto, WinNo)


Init() # O(1)