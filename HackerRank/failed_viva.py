def flop_list():
    main_list = [1, 2, 3, 4, 5, 7, 8, 9]
    copy_list = main_list
    print(copy_list)
    main_list.append(64)
    print(copy_list)
    copy_list = main_list[0:-1]
    main_list.append(633)
    print(copy_list)


flop_list()