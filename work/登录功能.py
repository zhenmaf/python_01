def from_file_get_data(file_name):
    try:
        f = open(file_name, 'r')
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()
