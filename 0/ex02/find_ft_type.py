def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    dict_types = {
        list: "List",
        set: "Set",
        dict: "Dict",
        str: "String",
        tuple: "Tuple",
    }
    if dict_types.get(obj_type) is None:
        print("Type not found")
        return 42
    elif obj_type is str:
        if len(object) == 0:
            object = "Nobody"

        print(object + " is in the kitchen : " + str(obj_type))
    else:
        print(dict_types[obj_type] + " : " + str(obj_type))

    return 0
