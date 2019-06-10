#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
playing around with string translate
"""

if __name__ == "__main__":
    st = "This is a original  string with spaces and     stuff in it"
    print("This is the original String:\n{}\n".format(st))
    """remove extra spaces"""
    s1 = " ".join(st.split())
    print("removed extra spaces:\n{}\n".format(s1))

    s2 = st.translate(str.maketrans("", "", " "))
    print("removed all spaces:\n{}\n".format(s2))
    """can also just use replace to remove a single character"""
    s7 = st.replace(" ", "")
    print("removed all spaces using replace:\n{}\n".format(s7))

    s3 = st.translate(str.maketrans("", "", "i"))
    print("remove all the i's:\n{}\n".format(s3))

    s4 = st.translate(str.maketrans("ieo", "abc"))
    print("replace i with a, e with b, o with c:\n{}\n".format(s4))

    s5 = " ".join(st.translate(str.maketrans("ieo", "abc")).split())
    print("replace i with a, e with b, o with c and removed extra spaces:\n{}\n".format(s5))
    
    s8 = st.translate(str.maketrans("ieo", "abc", " "))
    print("replace i with a, e with b, o with c and removed all spaces:\n{}\n".format(s8))
    
    s6 = st[::-1]
    print("reversed the string:\n{}\n".format(s6))