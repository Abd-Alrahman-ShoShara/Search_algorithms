from random import choice

from Magnet import Magnet
from Iron import Iron
from GoalCell import GoalCell
from BlockCell import BlockCell
from Game import Game
from Solver import Solver
def main():
    game1 = Game(4, 4,10)
    magnet1 = Magnet(2, 0, "N")
    iron1 = Iron(1, 2)
    goal1 = GoalCell(1, 1,True)
    goal2 = GoalCell(1, 3, True)
    block1 = BlockCell(3, 0)
    block2 = BlockCell(3, 1)
    block3 = BlockCell(3, 2)
    block4 = BlockCell(3, 3)
    #
    game1.add_object(magnet1, magnet1.x, magnet1.y)
    game1.add_object(iron1, iron1.x, iron1.y)
    game1.add_object(goal1, goal1.x, goal1.y)
    game1.add_object(goal2, goal2.x, goal2.y)
    game1.add_object(block1, block1.x, block1.y)
    game1.add_object(block2, block2.x, block2.y)
    game1.add_object(block3, block3.x, block3.y)
    game1.add_object(block4, block4.x, block4.y)

    # print("Initial Grid:")
    # game1.print_grid()

    # print("\nAfter moving magnet:")
    # game.play(magnet)
    #game.move_magnet(magnet, 2, 1)
    # game1.play_game(magnet)
    #game.move_magnet(magnet, 0, 0)

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////2
    game2 = Game(5, 5, 3)
    magnet2 = Magnet(4, 0, "N")
    iron1 = Iron(1, 2)
    iron2 = Iron(2, 1)
    iron3 = Iron(2, 3)
    iron4 = Iron(3, 2)
    goal1 = GoalCell(0, 2, True)
    goal2 = GoalCell(2, 2, True)
    goal3 = GoalCell(4, 2, True)
    goal4 = GoalCell(2, 0, True)
    goal5 = GoalCell(2, 4, True)

    game2.add_object(magnet2, magnet2.x, magnet2.y)
    game2.add_object(iron1, iron1.x, iron1.y)
    game2.add_object(iron2, iron2.x, iron2.y)
    game2.add_object(iron3, iron3.x, iron3.y)
    game2.add_object(iron4, iron4.x, iron4.y)
    game2.add_object(goal1, goal1.x, goal1.y)
    game2.add_object(goal2, goal2.x, goal2.y)
    game2.add_object(goal3, goal3.x, goal3.y)
    game2.add_object(goal4, goal4.x, goal4.y)
    game2.add_object(goal5, goal5.x, goal5.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////3

    game3 = Game(4, 4, 15)
    magnet3 = Magnet(2, 0, "N")
    iron1 = Iron(1, 2)

    goal1 = GoalCell(0, 3, True)
    goal2 = GoalCell(2, 3, True)

    game3.add_object(magnet3, magnet3.x, magnet3.y)
    game3.add_object(iron1, iron1.x, iron1.y)
    game3.add_object(goal1, goal1.x, goal1.y)
    game3.add_object(goal2, goal2.x, goal2.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    game4 = Game(5, 5, 2)
    magnet4 = Magnet(1, 1, "N")
    iron1 = Iron(1, 1)
    iron2 = Iron(3, 1)
    goal1 = GoalCell(0, 0, True)
    goal2 = GoalCell(0, 2, True)
    goal3 = GoalCell(4, 2, True)

    block1 = BlockCell(0, 3)
    block2 = BlockCell(1, 3)
    block3 = BlockCell(2, 3)
    block4 = BlockCell(3, 3)
    block5 = BlockCell(4, 3)
    block6 = BlockCell(0, 4)
    block7 = BlockCell(1, 4)
    block8 = BlockCell(2, 4)
    block9 = BlockCell(3, 4)
    block10 = BlockCell(4, 4)
    block11 = BlockCell(1, 0)
    block12 = BlockCell(3, 0)

    # Adding objects to the grid
    game4.add_object(magnet4, 2, 0)
    game4.add_object(iron1, 1, 1)
    game4.add_object(iron2, 3, 1)
    game4.add_object(goal1, 0, 0)
    game4.add_object(goal2, 0, 2)
    game4.add_object(goal3, 4, 1)

    game4.add_object(block1, block1.x, block1.y)
    game4.add_object(block2, block2.x, block2.y)
    game4.add_object(block3, block3.x, block3.y)
    game4.add_object(block4, block4.x, block4.y)
    game4.add_object(block5, block5.x, block5.y)
    game4.add_object(block6, block6.x, block6.y)
    game4.add_object(block7, block7.x, block7.y)
    game4.add_object(block8, block8.x, block8.y)
    game4.add_object(block9, block9.x, block9.y)
    game4.add_object(block10, block10.x, block10.y)
    game4.add_object(block11, block11.x, block11.y)
    game4.add_object(block12, block12.x, block12.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    game5 = Game(5, 5, 2)
    magnet5 = Magnet(3, 1, "N")
    iron1 = Iron(1, 0)
    iron2 = Iron(2, 0)
    iron3 = Iron(1, 2)
    iron4 = Iron(2, 2)
    goal1 = GoalCell(0, 0, True)
    goal2 = GoalCell(0, 2, True)
    # goal3 = GoalCell(1, 0, True)
    # goal4 = GoalCell(1, 2, True)
    goal5 = GoalCell(3, 0, True)
    game5.add_object(magnet5, magnet5.x, magnet5.y)
    game5.add_object(iron1, iron1.x, iron1.y)
    game5.add_object(iron2, iron2.x, iron2.y)
    game5.add_object(iron3, iron3.x, iron3.y)
    game5.add_object(iron4, iron4.x, iron4.y)
    game5.add_object(goal1, goal1.x, goal1.y)
    game5.add_object(goal2, goal2.x, goal2.y)
    # game5.add_object(goal3, goal3.x, goal3.y)
    # game5.add_object(goal4, goal4.x, goal4.y)
    game5.add_object(goal5, goal5.x, goal5.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    #1  0  // 0  3
    game6 = Game(5, 5, 2)
    magnet6 = Magnet(2, 0, "N")
    iron1 = Iron(1, 1)
    iron2 = Iron(1, 3)
    goal1 = GoalCell(0, 3, True)
    goal2 = GoalCell(1, 2, True)
    goal3 = GoalCell(2, 3, True)
    game6.add_object(magnet6, magnet6.x, magnet6.y)
    game6.add_object(iron1, iron1.x, iron1.y)
    game6.add_object(iron2, iron2.x, iron2.y)
    game6.add_object(goal1, goal1.x, goal1.y)
    game6.add_object(goal2, goal2.x, goal2.y)
    game6.add_object(goal3, goal3.x, goal3.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    #3  0 // 4  3
    game7 = Game(5, 5, 2)
    magnet7 = Magnet(2, 1, "N")
    iron1 = Iron(1, 0)
    iron2 = Iron(2, 0)
    iron3 = Iron(3, 1)
    iron4 = Iron(3, 2)
    goal1 = GoalCell(0, 0, True)
    goal2 = GoalCell(2, 3, True)
    goal3 = GoalCell(4, 3, True)
    game7.add_object(magnet7, magnet7.x, magnet7.y)
    game7.add_object(iron1, iron1.x, iron1.y)
    game7.add_object(iron2, iron2.x, iron2.y)
    game7.add_object(iron3, iron3.x, iron3.y)
    game7.add_object(iron4, iron4.x, iron4.y)
    game7.add_object(goal1, goal1.x, goal1.y)
    game7.add_object(goal2, goal2.x, goal2.y)
    game7.add_object(goal3, goal3.x, goal3.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    #  2  1 //  0  2

    game8 = Game(4, 4, 2)
    magnet8 = Magnet(2, 0, "N")
    iron1 = Iron(1, 1)
    iron2 = Iron(1, 2)
    goal1 = GoalCell(0, 0, True)
    goal2 = GoalCell(0, 2, True)
    goal3 = GoalCell(2, 2, True)
    game8.add_object(magnet8, magnet8.x, magnet8.y)
    game8.add_object(iron1, iron1.x, iron1.y)
    game8.add_object(iron2, iron2.x, iron2.y)
    game8.add_object(goal1, goal1.x, goal1.y)
    game8.add_object(goal2, goal2.x, goal2.y)
    game8.add_object(goal3, goal3.x, goal3.y)


    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    # 0 4 // 0  3
    game9 = Game(7, 7, 2)
    magnet9 = Magnet(0, 0, "N")
    iron1 = Iron(0, 3)
    iron2 = Iron(0, 5)
    goal1 = GoalCell(0, 1, True)
    goal2 = GoalCell(0, 6, True)
    # goal3 = GoalCell(0, 3, True)
    game9.add_object(magnet9, magnet9.x, magnet9.y)
    game9.add_object(iron1, iron1.x, iron1.y)
    game9.add_object(iron2, iron2.x, iron2.y)
    game9.add_object(goal1, goal1.x, goal1.y)
    game9.add_object(goal2, goal2.x, goal2.y)
    # game9.add_object(goal3, goal3.x, goal3.y)


    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    # 3  2  //  1  3
    game10 = Game(4, 4, 2)
    magnet10 = Magnet(0, 0, "N")
    iron1 = Iron(2, 2)
    iron2 = Iron(2, 3)
    iron3 = Iron(3, 1)
    goal1 = GoalCell(1, 1, True)
    goal2 = GoalCell(1, 3, True)
    goal3 = GoalCell(3, 0, True)
    goal4 = GoalCell(3, 3, True)

    game10.add_object(magnet10, magnet10.x, magnet10.y)
    game10.add_object(iron1, iron1.x, iron1.y)
    game10.add_object(iron2, iron2.x, iron2.y)
    game10.add_object(iron3, iron3.x, iron3.y)
    game10.add_object(goal1, goal1.x, goal1.y)
    game10.add_object(goal2, goal2.x, goal2.y)
    game10.add_object(goal3, goal3.x, goal3.y)
    game10.add_object(goal4, goal4.x, goal4.y)


    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # 0  2
    game11 = Game(5, 5, 2)
    magnet11 = Magnet(1, 2, "S")
    iron1 = Iron(0, 0)
    iron2 = Iron(0, 4)
    goal1 = GoalCell(0, 1, True)
    goal2 = GoalCell(0, 2, True)
    goal3 = GoalCell(0, 3, True)

    game11.add_object(magnet11, magnet11.x, magnet11.y)
    game11.add_object(iron1, iron1.x, iron1.y)
    game11.add_object(iron2, iron2.x, iron2.y)
    game11.add_object(goal1, goal1.x, goal1.y)
    game11.add_object(goal2, goal2.x, goal2.y)
    game11.add_object(goal3, goal3.x, goal3.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    # 4 0
    game12 = Game(5, 5, 2)
    magnet12 = Magnet(3, 1, "S")

    iron1 = Iron(0, 0)
    iron2 = Iron(1, 0)
    iron3 = Iron(4, 3)

    goal1 = GoalCell(2, 0, True)
    goal2 = GoalCell(4, 0, True)
    goal3 = GoalCell(4, 2, True)

    game12.add_object(magnet12, magnet12.x, magnet12.y)
    game12.add_object(iron1, iron1.x, iron1.y)
    game12.add_object(iron2, iron2.x, iron2.y)
    game12.add_object(iron3, iron3.x, iron3.y)
    game12.add_object(goal1, goal1.x, goal1.y)
    game12.add_object(goal2, goal2.x, goal2.y)
    game12.add_object(goal3, goal3.x, goal3.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    # 0 2  //  2  1
    game13 = Game(6, 6, 2)
    magnet13 = Magnet(2, 3, "S")

    iron1 = Iron(0, 0)
    iron2 = Iron(0, 4)
    iron3 = Iron(0, 5)

    goal1 = GoalCell(0, 3, True)
    goal2 = GoalCell(2, 1, True)
    goal3 = GoalCell(1, 1, True)

    game13.add_object(magnet13, magnet13.x, magnet13.y)
    game13.add_object(iron1, iron1.x, iron1.y)
    game13.add_object(iron2, iron2.x, iron2.y)
    game13.add_object(iron3, iron3.x, iron3.y)
    game13.add_object(goal1, goal1.x, goal1.y)
    game13.add_object(goal2, goal2.x, goal2.y)
    game13.add_object(goal3, goal3.x, goal3.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4
    # 0 0 // 2 2
    game14 = Game(4, 4, 2)
    magnet14 = Magnet(3, 3, "S")

    iron1 = Iron(0, 3)
    iron2 = Iron(2, 0)
    iron3 = Iron(3, 0)

    goal1 = GoalCell(1, 0, True)
    goal2 = GoalCell(1, 2, True)
    goal3 = GoalCell(2, 1, True)
    goal4 = GoalCell(2, 2, True)

    game14.add_object(magnet14, magnet14.x, magnet14.y)
    game14.add_object(iron1, iron1.x, iron1.y)
    game14.add_object(iron2, iron2.x, iron2.y)
    game14.add_object(iron3, iron3.x, iron3.y)
    game14.add_object(goal1, goal1.x, goal1.y)
    game14.add_object(goal2, goal2.x, goal2.y)
    game14.add_object(goal3, goal3.x, goal3.y)
    game14.add_object(goal4, goal4.x, goal4.y)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    game15 = Game(5, 5, 15)
    magnet15N = Magnet(1, 2, "N")
    magnet15S = Magnet(2, 2, "S")
    iron1 = Iron(0, 1)
    iron2 = Iron(0, 3)
    goal1 = GoalCell(0, 0, True)
    goal2 = GoalCell(0, 2, True)
    goal3 = GoalCell(1, 4, True)
    goal4 = GoalCell(2, 4, True)

    block1 = BlockCell(3, 0)
    block2= BlockCell(3, 1)
    block3 = BlockCell(3, 2)
    block4 = BlockCell(3, 3)
    block5 = BlockCell(3, 4)
    block6 = BlockCell(4, 0)
    block7 = BlockCell(4, 1)
    block8 = BlockCell(4, 2)
    block9 = BlockCell(4, 3)
    block10 = BlockCell(4, 4)

    # Adding objects to the grid
    game15.add_object(magnet15N, 1, 2)
    game15.add_object(magnet15S, 2, 2)
    game15.add_object(iron1, iron1.x, iron1.y)
    game15.add_object(iron2, iron2.x, iron2.y)
    game15.add_object(goal1, goal1.x, goal1.y)
    game15.add_object(goal2, goal2.x, goal2.y)
    game15.add_object(goal3, goal3.x, goal3.y)
    game15.add_object(goal4, goal4.x, goal4.y)

    game15.add_object(block1,block1.x,block1.y)
    game15.add_object(block2, block2.x, block2.y)
    game15.add_object(block3, block3.x, block3.y)
    game15.add_object(block4, block4.x, block4.y)
    game15.add_object(block5, block5.x, block5.y)
    game15.add_object(block6, block6.x, block6.y)
    game15.add_object(block7, block7.x, block7.y)
    game15.add_object(block8, block8.x, block8.y)
    game15.add_object(block9, block9.x, block9.y)
    game15.add_object(block10, block10.x, block10.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    game16 = Game(5, 5, 3)

    # Define magnets, irons, and goal cells based on the image
    magnet1 = Magnet(2, 4, "N")  # Example position and type
    magnet2 = Magnet(2, 0, "S")  # Example position and type
    iron1 = Iron(1, 2)
    iron2 = Iron(3, 2)

    goal1 = GoalCell(0, 3, True)
    goal2 = GoalCell(0, 4, True)
    goal3 = GoalCell(4, 0, True)
    goal4 = GoalCell(4, 3, True)

    # Adding objects to the grid
    game16.add_object(magnet1, magnet1.x, magnet1.y)
    game16.add_object(magnet2, magnet2.x, magnet2.y)
    game16.add_object(iron1, iron1.x, iron1.y)
    game16.add_object(iron2, iron2.x, iron2.y)
    game16.add_object(goal1, goal1.x, goal1.y)
    game16.add_object(goal2, goal2.x, goal2.y)
    game16.add_object(goal3, goal3.x, goal3.y)
    game16.add_object(goal4, goal4.x, goal4.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    game17 = Game(4, 4, 3)

    # Define magnets, irons, and goal cells based on the image
    magnet17N = Magnet(3, 3, "N")  # Example position and type
    magnet17S = Magnet(0, 0, "S")  # Example position and type
    iron1 = Iron(0, 2)
    iron2 = Iron(2, 0)

    goal1 = GoalCell(1, 1, True)
    goal2 = GoalCell(1, 3, True)
    goal3 = GoalCell(2, 2, True)
    goal4 = GoalCell(3, 1, True)

    # Adding objects to the grid
    game17.add_object(magnet17N, magnet17N.x, magnet17N.y)
    game17.add_object(magnet17S, magnet17S.x, magnet17S.y)
    game17.add_object(iron1, iron1.x, iron1.y)
    game17.add_object(iron2, iron2.x, iron2.y)
    game17.add_object(goal1, goal1.x, goal1.y)
    game17.add_object(goal2, goal2.x, goal2.y)
    game17.add_object(goal3, goal3.x, goal3.y)
    game17.add_object(goal4, goal4.x, goal4.y)
    #///////////////////////////////////////////////////////////////////////////////////////
    game18 = Game(6, 6, 3)

    # Define magnets, irons, and goal cells based on the image
    magnet1 = Magnet(4, 3, "N")  # Example position and type
    magnet2 = Magnet(4, 2, "S")  # Example position and type
    iron1 = Iron(2, 0)
    iron2 = Iron(0, 3)
    iron3 = Iron(2, 5)

    goal1 = GoalCell(2, 1, True)
    goal2 = GoalCell(1, 3, True)
    goal3 = GoalCell(2, 2, True)
    goal4 = GoalCell(2, 3, True)
    goal5 = GoalCell(2, 5, True)

    block1 = BlockCell(0, 0)
    block2 = BlockCell(1, 0)
    block3 = BlockCell(0, 1)
    block4 = BlockCell(1, 1)
    block5 = BlockCell(0, 4)
    block6 = BlockCell(0, 5)
    block7 = BlockCell(1, 5)
    block8 = BlockCell(1, 4)
    block9 = BlockCell(4, 0)
    block10 = BlockCell(4, 1)
    block11 = BlockCell(4, 4)
    block12 = BlockCell(4, 5)
    # Adding objects to the grid
    game18.add_object(magnet1, magnet1.x, magnet1.y)
    game18.add_object(magnet2, magnet2.x, magnet2.y)
    game18.add_object(iron1, iron1.x, iron1.y)
    game18.add_object(iron2, iron2.x, iron2.y)
    game18.add_object(iron3, iron3.x, iron3.y)
    game18.add_object(goal1, goal1.x, goal1.y)
    game18.add_object(goal2, goal2.x, goal2.y)
    game18.add_object(goal3, goal3.x, goal3.y)
    game18.add_object(goal4, goal4.x, goal4.y)
    game18.add_object(goal5, goal5.x, goal5.y)

    game18.add_object(block1, block1.x, block1.y)
    game18.add_object(block2, block2.x, block2.y)
    game18.add_object(block3, block3.x, block3.y)
    game18.add_object(block4, block4.x, block4.y)
    game18.add_object(block5, block5.x, block5.y)
    game18.add_object(block6, block6.x, block6.y)
    game18.add_object(block7, block7.x, block7.y)
    game18.add_object(block8, block8.x, block8.y)
    game18.add_object(block9, block9.x, block9.y)
    game18.add_object(block10, block10.x, block10.y)
    game18.add_object(block11, block11.x, block11.y)
    game18.add_object(block12, block12.x, block12.y)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4


    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////4

    choice = input("enter the number of level from 1 to 18 :")

    if choice == '1':
        print("start level 1")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
        if choice_1 == '1':
            game1.play()
        elif choice_1 == '2':
            solver = Solver(game1)
            # solver.solve_with_dfs()
    elif choice == '2':
        print("start level 2")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game2.play()
        elif choice_1 == '2':
            solver = Solver(game2)
            # solver.solve_with_dfs()
    elif choice == '3':
        print("start level 3")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game3.play()
        elif choice_1 == '2':
            solver = Solver(game3)
            # solver.solve_with_dfs()
    elif choice == '4':
        print("start level 4")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game4.play()
        elif choice_1 == '2':
            solver = Solver(game4)
            # solver.solve_with_dfs()
    elif choice == '5':
        print("start level 5")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game5.play()
        elif choice_1 == '2':
            solver = Solver(game15)
            # solver.solve_with_dfs()
    elif choice == '6':
        print("start level 6")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game6.play()
        elif choice_1 == '2':
            solver = Solver(game15)
            # solver.solve_with_dfs()
    elif choice == '7':
        print("start level 7")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game7.play()
        elif choice_1 == '2':
            solver = Solver(game7)
            # solver.solve_with_dfs()
    elif choice == '8':
        print("start level 8")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game8.play()
        elif choice_1 == '2':
            solver = Solver(game8)
            # solver.solve_with_dfs()
    elif choice == '9':
        print("start level 9")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game9.play()
        elif choice_1 == '2':
            solver = Solver(game9)
            # solver.solve_with_dfs()
    elif choice == '10':
        print("start level 10")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game10.play()
        elif choice_1 == '2':
            solver = Solver(game10)
            # solver.solve_with_dfs()
    elif choice == '11':
        print("start level 11  ")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game11.play()
        elif choice_1 == '2':
            solver = Solver(game11)
            # solver.solve_with_dfs()
    elif choice == '12':
        print("start level 12")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game12.play()
        elif choice_1 == '2':
            solver = Solver(game12)
            # solver.solve_with_dfs()
    elif choice == '13':
        print("start level 12")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game13.play()
        elif choice_1 == '2':
            solver = Solver(game13)
            # solver.solve_with_dfs()
    elif choice == '14':
        print("start level 14")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game14.play()
        elif choice_1 == '2':
            solver = Solver(game14)
            # solver.solve_with_dfs()
    elif choice == '15':
        print("start level 15")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game15.play()
        elif choice_1 == '2':
            solver = Solver(game15)
            # solver.solve_with_dfs()
    elif choice == '16':
        print("start level 16")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game16.play()
        elif choice_1 == '2':
            solver = Solver(game16)
            # solver.solve_with_dfs()

    elif choice == '17':
        print("start level 17")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game17.play()
        elif choice_1 == '2':
            solver = Solver(game16)
            # solver.solve_with_dfs()
    elif choice == '18':
        print("start level 18")
        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game18.play()
        elif choice_1 == '2':
            solver = Solver(game18)
            # solver.solve_with_dfs()
    else:
        print("wrong entring , enter a numper please : .")





main()
