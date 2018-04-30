class perusahaan:
    def __init__(self, first, last,) :
        self.first = first
        self.last  = last 
        self.email = first + '.' + last + ' @rocketmail.com'

per_1 = perusahaan('Kami dari', 'MASMISKUN')
print('Berikut adalah Email Kami')
print(per_1.email)

