if __name__ == "__main__":
    destination = []
    source = ["aa", "bb", "cc", "dd"]
    white_list = ["aa", "bb", "cc", "aa"]
    white_list = set(white_list)
    for s in source:
        if s in white_list:
            print(s)
            destination.append(s)
    print(destination)
