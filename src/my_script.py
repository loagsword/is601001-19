# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
signature = 'Akin recycled this :)'
print(encoder.get_ascii())
print(signature)
