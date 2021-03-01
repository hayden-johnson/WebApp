from user_profile import User


def interface():
    print("Welcome!\nCreate Learner Profile")

    # initial learner profile
    name = input("Enter you name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    user = User(name, int(age), gender)

    # main loop
    while not user.state.is_terminal:
        print(f'\n**********************************************\n'
              f'You are currently {user.state.goal_str()} {user.state.location}\n')
        user.state.print_options()
        response = int(input("\n-> "))
        if user.state.goal == "explore":
            if response == 1:
                user.state.get_wiki()
            if response == 2:
                user.state.get_intro()
            if response == 3:
                user.state.get_local_map()
            if response == 4:
                user.state.redefine_goal()
            if response == 5:
                user.state.rec_next_steps()
            if response == 6:
                user.state.get_path()
            if response == 7:
                user.state.terminate()
        else:  # apply
            if response == 1:
                user.state.get_tutorial()
            if response == 2:
                user.state.get_methods()
            if response == 3:
                user.state.get_tools()
            if response == 4:
                user.state.redefine_goal()
            if response == 5:
                user.state.rec_next_steps()
            if response == 6:
                user.state.get_path()
            if response == 7:
                user.state.terminate()
    print("Goodbye!")
    return


if __name__ == "__main__":
    interface()
