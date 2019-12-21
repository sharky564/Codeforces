# Chat room
a = input()
b = list(a)
if len(b) < 5:
    print("NO")
else:
    i = 0
    while b[i] != 'h':
        if len(b) > i + 1:
            b.remove(b[i])
        else:
            print("NO")
            break
    else:
        if len(b) < 5:
            print("NO")
        else:
            j = 1
            while b[j] != 'e':
                if len(b) > j + 1:
                    b.remove(b[j])
                else:
                    print("NO")
                    break
            else:
                if len(b) < 5:
                    print("NO")
                else:
                    k = 2
                    while b[k] != 'l':
                        if len(b) > k + 1:
                            b.remove(b[k])
                        else:
                            print("NO")
                            break
                    else:
                        if len(b) < 5:
                            print("NO")
                        else:
                            l = 3
                            while b[l] != 'l':
                                if len(b) > l + 1:
                                    b.remove(b[l])
                                else:
                                    print("NO")
                                    break
                            else:
                                if len(b) < 5:
                                    print("NO")
                                else:
                                    m = 4
                                    while b[m] != 'o':
                                        if len(b) > m + 1:
                                            b.remove(b[m])
                                        else:
                                            print("NO")
                                            break
                                    else:
                                        if len(b) < 5:
                                            print("NO")
                                        else:
                                            print("YES")
