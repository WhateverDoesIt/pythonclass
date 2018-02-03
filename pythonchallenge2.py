#thestring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
thestring = "test string"

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

whichone = int(0)

for newstring in thestring:
    print whichone
    newstring = thestring.replace(str(letter [1 + whichone:]), str(letter [3 + whichone:]))
    whichone += 1

print newstring

