def stringanagram(str1,str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    if(s1==s2):
        print("anagram")
    else:
        print("not anagram")

stringanagram("raj","jar")