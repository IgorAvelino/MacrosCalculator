MEASUREMENTS = {
    "name": "",
    "wei": 0.0,
    "hei": 0,
    "age": 0,
    "sex": "o",
    "bfp": 0.0,
    "lbm": 0.0,
    "lfs": "o",
    "tfr": 0,
    "exp": "o",
    "obj": "o",
    "bmr": 0.0,
    "tcr": 0.0,
    "cal_itk": 0.0,
    "pro": 0.0,
    "pro_c": 0.0,
    "gor": 0.0,
    "gor_c": 0.0,
    "carb": 0.0,
    "carb_c": 0.0,
}


def ask_usr_name():
    try:
        n = str(input('Type your name \033[33m(optional)\033[0;0;0m: '))
        return n
    except ValueError:
        pass


def ask_usr_weight():
    try:
        w = float(input('Type your weight \033[33m(Kg)\033[0;0;0m: '))
        return w
    except ValueError:
        ask_usr_weight()


def ask_usr_height():
    try:
        h = int(input('Type your height \033[33m(cm)\033[0;0;0m: '))
        return h
    except ValueError:
        ask_usr_height()


def ask_usr_age():
    try:
        a = int(input('Type your age \033[33m(years)\033[0;0;0m: '))
        return a
    except ValueError:
        ask_usr_age()


def ask_usr_sex():
    try:
        s = 'o'
        while s not in 'mf':
            print('Select your gender:\n\033[33m[M]\033[0;0;0m Masculine\n\033[33m[F]\033[0;0;0m Feminine')
            s = str(input('Type: ')).strip().lower()
        if s == '':
            ask_usr_sex()
        return s
    except ValueError:
        ask_usr_sex()


def ask_usr_bf():
    try:
        bf = float(input('Type your Body Fat \033[33m(%)\033[0;0;0m: '))
        return bf
    except ValueError:
        ask_usr_bf()


def ask_usr_lbm():
    try:
        lbm = float(input('Type your Lean Body Mass \033[33m(Kg)\033[0;0;0m\033[33m(0 = estimate)\033[0;0;0m: '))
        if lbm == 0:
            lbm = (MEASUREMENTS['wei'] * 2.2046) * ((100 - MEASUREMENTS['bfp']) / 100) / 2.2046
        return lbm
    except ValueError:
        ask_usr_lbm()


def ask_usr_lfs():
    try:
        s = 'o'
        while s not in 'slmh':
            print('Select your lifestyle (outside of lifting):\n\033[33m[S] \033[36mSedentary\033[0;0;0m: Works a desk job, very little activity outside of lifting\n\033[33m[L] \033[36mLightly Active\033[0;0;0m: Works a desk job, takes pet for a walk most days in addition to lifting\n\033[33m[M] \033[36mModerately Active\033[0;0;0m: Works as a full-time waitress, occasionally plays tennis in addition to lifting\n\033[33m[H] \033[36mHighly Active\033[0;0;0m: Works as a construction worker, regular hiking in addition to lifting')
            s = str(input('Type: ')).strip().lower()
        if s == '':
            ask_usr_lfs()
        return s
    except ValueError:
        ask_usr_lfs()


def ask_usr_tfr():
    try:
        s = 0
        while 3 > s or s > 6:
            print('Select your training frequency:\n\033[33m[3]\033[0;0;0m 3x or less per week\n\033[33m[4]\033[0;0;0m 4x per week\n\033[33m[5]\033[0;0;0m 5x per week\n\033[33m[6]\033[0;0;0m 6x or more per week')
            s = int(input('Type: '))
        if s == '':
            ask_usr_tfr()
        return s
    except ValueError:
        ask_usr_tfr()


def ask_usr_exp():
    try:
        s = 'o'
        while s not in 'bia':
            print('Select your training experience:\n\033[33m[B] \033[36mBeginner\033[0;0;0m: Making progressive overload gains on a week to week basis and significant visual changes month to month (usually 0-2 years of lifting)\n\033[33m[I] \033[36mIntermediate\033[0;0;0m: Able to progressively overload on a month to month basis. Physique progress is evident every couple of months (usually 2-5 years of lifting)\n\033[33m[A] \033[36mAdvanced\033[0;0;0m: Takes multiple months or even years to see visual progress and ability to overload lifts is much more difficult (usually 5+ years of serious lifting)')
            s = str(input('Type: ')).strip().lower()
        if s == '':
            ask_usr_exp()
        return s
    except ValueError:
        ask_usr_exp()


def ask_usr_obj():
    try:
        s = 'o'
        while s not in 'lbe':
            print('Select your primary goal:\n\033[33m[L]\033[0;0;0m Lose Fat\n\033[33m[B]\033[0;0;0m Build Muscle\n\033[33m[E]\033[0;0;0m Equally Lose Fat & Build Muscle')
            s = str(input('Type: ')).strip().lower()
        if s == '':
            ask_usr_obj()
        return s
    except ValueError:
        ask_usr_obj()


def space():
    print('-'*30)


def user_questionary():
    print("""\t\t\t\033[33m   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⡄⠀⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⣰⣧⣼⣿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⠀⣿⠿⢿⠻⠿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣾⠿⠢⠄⠁⠀⣬⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⢀⠠⠧⠄⠈⣧⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⢄⣀⠀⠀⣀⣀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡏⠉⠠⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡖⠉⠑⠀⠲⣤⠤⠘⠉⡁⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⡀⠀⡄⠀⠰⠀⠀⠀⢹⡀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢲⢧⣠⣀⣀⠴⢄⣀⣤⣆⠘⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠎⡾⣄⣀⣀⣴⠒⢄⣀⣿⠀⢺⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⢰⣷⣖⠁⠁⢈⡀⠣⣾⢻⣄⡜⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⢳⢉⡏⠃⠠⡀⠀⡏⠉⣼⠸⠙⡀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⢰⠟⣄⢰⠈⢹⠉⢰⣿⣆⡆⠱⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t\t   ⠀⠀⠀⣀⡤⡔⠊⠉⡱⢆⠀⠀⠀⠀⠀⠀⠀⢸⠀⢀⡞⠀⠈⠳⡶⢼⠤⡿⠁⠘⣷⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⣀⠀⠀⠀⠀⠀⠀
\t\t\t   ⢀⡔⢺⠁⠀⡇⠀⠀⢷⠈⢣⠀⠀⠀⠀⠀⢀⣼⢦⣼⣁⣀⠤⠤⠷⠤⠼⠥⠤⢤⣻⣟⣻⡀⠀⠀⠀⠀⠀⡴⠋⠀⢸⠈⠹⠒⢄⡀⠀⠀
\t\t\t  ⡆⢻⠀⢸⠀⠀⢧⠀⠀⠸⣷⡞⢧⢀⡠⠤⠒⠛⣿⡓⣛⣧⣤⠒⡶⢶⣲⡶⠒⠶⣶⠏⠨⣹⣗⠒⠢⠤⣀⡎⠀⠀⠀⡘⠀⢠⠀⠈⡏⢳⡄
\t\t\t ⢸ ⢸⠀⠀⡆⠀⠸⡄⠀⠀⢣⣤⠊⢁⡠⠤⠒⠉⠻⢿⡿⠋⠋⠐⡅⠀⣿⠀⠀⠰⠉⠚⣿⠋⠀⠉⠑⠢⡤⣉⣲⠀⢠⠃⠀⡜⠀⢠⠀⠸⢸
\t\t\t ⢸ ⠀⡆⠀⢹⡀⠀⢳⠀⠀⠈⢏⠋⢳⠀⠀⠀⠀⠀⠸⣇⢄⡖⠀⢸⢸⢿⠰⠀⠀⡟⢰⠇⠀⠀⠀⠀⣸⠀⠀⠀⣰⠏⠀⣰⠃⢀⡎⢀⠇⡸
\t\t\t  ⢸ ⠹⡄⠀⢷⠀⠀⢧⠀⠀⠈⡆⠀⡇⠀⠀⠀⠀⠀⢹⡟⠑⢤⣾⠋⠀⢳⣀⠘⠙⠇⠀⠀⠀⠀⠀⡟⠀⢀⣼⠋⠀⡰⠃⠀⡜⠀⡜⢀⠃
\t\t\t   ⢣⡀⢹⣆⡀⢳⣀⠀⠳⣄⡀⠘⢦⡕⠀⠀⠀⠀⠀⢸⡇⠀⠀⢳⠀⠀⣼⠉⠀⢸⡆⠀⠀⠀⠀⠀⠺⣶⡚⠁⣠⠖⠁⣠⠎⢀⡜⣠⠊⠀
\033[31m    __  ___                              ______      __           __      __            
   /  |/  /___ _______________  _____   / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / /|_/ / __ `/ ___/ ___/ __ \\/ ___/  / /   / __ `/ / ___/ / / / / __ `/ __/ __ \\/ ___/
 / /  / / /_/ / /__/ /  / /_/ (__  )  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_/  /_/\\__,_/\\___/_/   \\____/____/   \\____/\\__,_/_/\\___/\\__,_/_/\\__,_/\\__/\\____/_/  \033[0;0;0m\033[36mby Igor Avelino\033[0;0;0m""")

    print("\n\033[33m[i]\033[0;0;0m Welcome to Macros Calculator! Here we will calculate the macros you need to eat \n"
          "(fats, proteins and carbohydrates) based on some information from you :)\n\n")

    MEASUREMENTS['name'] = ask_usr_name()
    space()
    MEASUREMENTS['wei'] = ask_usr_weight()
    space()
    MEASUREMENTS['hei'] = ask_usr_height()
    space()
    MEASUREMENTS['age'] = ask_usr_age()
    space()
    MEASUREMENTS['sex'] = ask_usr_sex()
    space()
    MEASUREMENTS['bfp'] = ask_usr_bf()
    space()
    MEASUREMENTS['lbm'] = ask_usr_lbm()
    space()
    MEASUREMENTS['lfs'] = ask_usr_lfs()
    space()
    MEASUREMENTS['tfr'] = ask_usr_tfr()
    space()
    MEASUREMENTS['exp'] = ask_usr_exp()
    space()
    MEASUREMENTS['obj'] = ask_usr_obj()
    space()


def calculate_bmr():
    bmr = (10 * MEASUREMENTS['wei']) + (6.25 * MEASUREMENTS['hei']) - (5 * MEASUREMENTS['age'])
    if MEASUREMENTS['sex'] == 'm':
        bmr += 5
    elif MEASUREMENTS['sex'] == 'f':
        bmr -= 161
    return bmr


def calculate_cal_itk():
    if MEASUREMENTS['obj'] == 'l':
        return MEASUREMENTS['tcr'] * 0.8
    elif MEASUREMENTS['obj'] == 'e':
        return MEASUREMENTS['tcr']
    elif MEASUREMENTS['obj'] == 'b' and MEASUREMENTS['exp'] == 'b':
        return MEASUREMENTS['tcr'] * 1.25
    elif MEASUREMENTS['obj'] == 'b' and MEASUREMENTS['exp'] == 'i':
        if MEASUREMENTS['sex'] == 'm':
            # Men
            if MEASUREMENTS['bfp'] >= 12:
                return MEASUREMENTS['tcr'] * 1.2
            elif MEASUREMENTS['bfp'] <= 8:
                return MEASUREMENTS['tcr'] * 1.15
            else:
                return MEASUREMENTS['tcr'] * (1.15 + (1.2 - 1.15) * (MEASUREMENTS['bfp'] - 8) / (12 - 8))
        elif MEASUREMENTS['sex'] == 'f':
            # Woman
            if MEASUREMENTS['bfp'] >= 22:
                return MEASUREMENTS['tcr'] * 1.2
            elif MEASUREMENTS['bfp'] <= 18:
                return MEASUREMENTS['tcr'] * 1.15
            else:
                return MEASUREMENTS['tcr'] * (1.15 + (1.2 - 1.15) * (MEASUREMENTS['bfp'] - 18) / (22 - 18))
    elif MEASUREMENTS['obj'] == 'b' and MEASUREMENTS['exp'] == 'a':
        if MEASUREMENTS['sex'] == 'm':
            # Men
            if MEASUREMENTS['bfp'] >= 12:
                return MEASUREMENTS['tcr'] * 1.15
            elif MEASUREMENTS['bfp'] <= 8:
                return MEASUREMENTS['tcr'] * 1.1
            else:
                return MEASUREMENTS['tcr'] * (1.1 + (1.15 - 1.1) * (MEASUREMENTS['bfp'] - 8) / (12 - 8))
        elif MEASUREMENTS['sex'] == 'f':
            # Woman
            if MEASUREMENTS['bfp'] >= 22:
                return MEASUREMENTS['tcr'] * 1.15
            elif MEASUREMENTS['bfp'] <= 18:
                return MEASUREMENTS['tcr'] * 1.1
            else:
                return MEASUREMENTS['tcr'] * (1.1 + (1.15 - 1.1) * (MEASUREMENTS['bfp'] - 18) / (22 - 18))


def calculate_tcr():
    if MEASUREMENTS['lfs'] == 's':
        return MEASUREMENTS['bmr'] * (1.2 + ((MEASUREMENTS['tfr'] - 3) / 10))
    elif MEASUREMENTS['lfs'] == 'l':
        return MEASUREMENTS['bmr'] * (1.5 + ((MEASUREMENTS['tfr'] - 3) / 10))
    elif MEASUREMENTS['lfs'] == 'm':
        return MEASUREMENTS['bmr'] * (1.8 + ((2 - 1.8) * (MEASUREMENTS['tfr'] - 3) / (6 - 3) / 10))
    elif MEASUREMENTS['lfs'] == 'h':
        return MEASUREMENTS['bmr'] * (2 + ((2.2 - 2) * (MEASUREMENTS['tfr'] - 3) / (6 - 3) / 10))


def calculate_pro():
    if MEASUREMENTS['sex'] == 'm':
        # Men
        if MEASUREMENTS['bfp'] >= 30:
            return (MEASUREMENTS['lbm'] * 2.2046) * 1.2
        elif MEASUREMENTS['bfp'] <= 5:
            return (MEASUREMENTS['lbm'] * 2.2046) * 1.6
        else:
            return (MEASUREMENTS['lbm'] * 2.2046) * (1.2 + (1.6 - 1.2) * (30 - MEASUREMENTS['bfp']) / (30 - 5))
    elif MEASUREMENTS['sex'] == 'f':
        # Woman
        if MEASUREMENTS['bfp'] >= 40:
            return (MEASUREMENTS['lbm'] * 2.2046) * 1.2
        elif MEASUREMENTS['bfp'] <= 8:
            return (MEASUREMENTS['lbm'] * 2.2046) * 1.6
        else:
            return (MEASUREMENTS['lbm'] * 2.2046) * (1.2 + (1.6 - 1.2) * (40 - MEASUREMENTS['bfp']) / (40 - 8))


def calculate_gor():
    if MEASUREMENTS['sex'] == 'm':
        # Men
        if MEASUREMENTS['bfp'] >= 25:
            return (MEASUREMENTS['cal_itk'] * 0.35) / 9
        elif MEASUREMENTS['bfp'] <= 5:
            return (MEASUREMENTS['cal_itk'] * 0.20) / 9
        else:
            return (MEASUREMENTS['cal_itk'] * (0.2 + (0.35 - 0.2) * (MEASUREMENTS['bfp'] - 5) / (25 - 5))) / 9
    elif MEASUREMENTS['sex'] == 'f':
        # Woman
        if MEASUREMENTS['bfp'] >= 40:
            return (MEASUREMENTS['cal_itk'] * 0.35) / 9
        elif MEASUREMENTS['bfp'] <= 10:
            return (MEASUREMENTS['cal_itk'] * 0.20) / 9
        else:
            return (MEASUREMENTS['cal_itk'] * (0.2 + (0.35 - 0.2) * (MEASUREMENTS['bfp'] - 10) / (40 - 10))) / 9


def calculate_carb():
    return (MEASUREMENTS['cal_itk'] - (MEASUREMENTS['gor_c'] + MEASUREMENTS['pro_c'])) / 4


def process_data():
    MEASUREMENTS['bmr'] = calculate_bmr()
    MEASUREMENTS['tcr'] = calculate_tcr()
    MEASUREMENTS['cal_itk'] = calculate_cal_itk()
    MEASUREMENTS['pro'] = calculate_pro()
    MEASUREMENTS['pro_c'] = MEASUREMENTS['pro'] * 4
    MEASUREMENTS['gor'] = calculate_gor()
    MEASUREMENTS['gor_c'] = MEASUREMENTS['gor'] * 9
    MEASUREMENTS['carb'] = calculate_carb()
    MEASUREMENTS['carb_c'] = MEASUREMENTS['carb'] * 4


def show_results():
    if MEASUREMENTS['name'] == '':
        MEASUREMENTS['name'] = "user"

    print(f"""╔═════════ ◆ \033[36m{MEASUREMENTS['name'].upper()}\'s INFORMATION\033[0;0;0m ◆ ═════════╗
║{' '*(38 + len(MEASUREMENTS['name']))}║
║  Weight: \033[36m{MEASUREMENTS['wei']:6.2f} Kg\033[0;0;0m{' '*(19 + len(MEASUREMENTS['name']))}║
║  Height: \033[36m{MEASUREMENTS['hei']:3.0f} cm\033[0;0;0m{' '*(22 + len(MEASUREMENTS['name']))}║
║  Age: \033[36m{MEASUREMENTS['age']:2} years\033[0;0;0m{' '*(23 + len(MEASUREMENTS['name']))}║
║  Sex: \033[36m{MEASUREMENTS['sex'].upper()}\033[0;0;0m{' '*(30 + len(MEASUREMENTS['name']))}║
║  Body Fat: \033[36m{MEASUREMENTS['bfp']:5.2f}%\033[0;0;0m{' '*(20 + len(MEASUREMENTS['name']))}║
║  Lean Body Mass (LBM): \033[36m{MEASUREMENTS['lbm']:6.2f} Kg\033[0;0;0m{' '*(5 + len(MEASUREMENTS['name']))}║
║  Fat Body Mass (FBM): \033[36m{(MEASUREMENTS['wei'] - MEASUREMENTS['lbm']):5.2f} Kg\033[0;0;0m{' '*(7 + len(MEASUREMENTS['name']))}║
║  Basal Metabolism Rate: \033[36m{MEASUREMENTS['bmr']:4.0f} Kcal\033[0;0;0m{' '*(4 + len(MEASUREMENTS['name']))}║
║  Calories Burned per day : \033[36m{MEASUREMENTS['tcr']:4.0f} Kcal\033[0;0;0m{' '*(1 + len(MEASUREMENTS['name']))}║
╚{'═'*(38 + len(MEASUREMENTS['name']))}╝
""")

    print(f"""╔═══════════ ◆ \033[32m{MEASUREMENTS['name'].upper()}\'s MACROS\033[0;0;0m ◆ ═══════════╗
║{' ' * (37 + len(MEASUREMENTS['name']))}║
║  Calories Intake: \033[33m{MEASUREMENTS['cal_itk']:4.0f} Kcal\033[0;0;0m{' ' * (9 + len(MEASUREMENTS['name']))}║
║         Proteins: \033[32m{MEASUREMENTS['pro']:3.0f}g \033[33m({MEASUREMENTS['pro_c']:4.0f} Kcal)\033[0;0;0m{' ' * (2 + len(MEASUREMENTS['name']))}║
║             Fats: \033[32m{MEASUREMENTS['gor']:3.0f}g\033[0;0;0m \033[33m({MEASUREMENTS['gor_c']:4.0f} Kcal)\033[0;0;0m{' ' * (2 + len(MEASUREMENTS['name']))}║
║    Carbohydrates: \033[32m{MEASUREMENTS['carb']:3.0f}g\033[0;0;0m \033[33m({MEASUREMENTS['carb_c']:4.0f} Kcal)\033[0;0;0m{' ' * (2 + len(MEASUREMENTS['name']))}║
╚{'═' * (37 + len(MEASUREMENTS['name']))}╝
""")
    print("""\033[31m    __  ___                              ______      __           __      __            
   /  |/  /___ _______________  _____   / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / /|_/ / __ `/ ___/ ___/ __ \\/ ___/  / /   / __ `/ / ___/ / / / / __ `/ __/ __ \\/ ___/
 / /  / / /_/ / /__/ /  / /_/ (__  )  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_/  /_/\\__,_/\\___/_/   \\____/____/   \\____/\\__,_/_/\\___/\\__,_/_/\\__,_/\\__/\\____/_/  \033[0;0;0m\033[36mby Igor Avelino\033[0;0;0m""")


if __name__ == "__main__":
    try:
        user_questionary()
        process_data()
        show_results()
    except KeyboardInterrupt:
        print('\n\033[31m[!]\033[0;0;0m \033[33mOperation Canceled by the user!\033[0;0;0m')
