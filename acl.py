acl = int(input("ingrese el número de la ACL ipv4: "))
#acl estantar 1-99, 1300-1999
#acl extendido 100-199, 2000-2699

if acl <= 1 or acl <=99 or acl <= 1300 or acl <= 1999:
    print("su ACL ipv4 es estándar")
elif acl <= 100 or acl <= 199 or acl <= 2000 or acl <= 2699:
    print("su ACL ipv4 es extendida")
else:
    print("su ACL no es estándar ni extendida")
