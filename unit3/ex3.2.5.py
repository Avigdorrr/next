def read_file(file_name):
    msg = "__CONTENT_START__\n"
    try:
        f = open(file_name, "r")
    except:
        msg += "__NO_SUCH_FILE__\n"
    else:
        msg += f.read()+"\n"
        f.close()
    finally:
        msg += "__CONTENT_END__"
    return msg