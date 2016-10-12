text= 'WKH HDVLHVW PHWKRG RI HQFLSKHULQJ D WHAW PHVVDJH LV WR UHSODFH HDFK OHWWHU EB DQRWKHU XVLQJ D ILAHG UXOH, VR IRU HADPSOH HYHUB OHWWHU D PDB EH UHSODFHG EB G, DQG HYHUB OHWWHU E EB WKH OHWWHU H DQG VR RQ.'.upper()
for i in range(1,26):
    output = ''
    for c in text:
        if ord(c)<(91-i)and ord(c)>64:
            output += chr(ord(c)+i)
        elif ord(c)<91 and ord(c)>64:
            output += chr(ord(c)+i-26)
        else: output += c
    if "THE" in output:
        print output.lower()
