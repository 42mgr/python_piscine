def NULL_not_found(object: any) -> int:
    str_buff = ""
    match object:
        case None:
            str_buff = "Nothing: "
        case False:
            str_buff = "Fake: "
        case 0:
            str_buff = "Zero: "
        case "":
            str_buff = "Empty: "
        case float(object) if object != object:
            str_buff = "Cheese: "
        case _:
            print("Type not Found")
            return 1

    print(
        str_buff
        + str(object)
        + (" " if (len(str(object)) > 0) else "")
        + str(type(object))
    )
    return 0


def NULL_not_found_old(object: any) -> int:
    str_buff = ""
    if object is None:
        str_buff = "Nothing: "
    elif object is False:
        str_buff = "Fake: "
    elif object == 0:
        str_buff = "Zero: "
    elif object == "":
        str_buff = "Empty: "
    elif type(object) is float and object != object:
        str_buff = "Cheese: "
    else:
        print("Type not Found")
        return 1
    print(
        str_buff
        + str(object)
        + (" " if (len(str(object)) > 0) else "")
        + str(type(object))
    )
    return 0
