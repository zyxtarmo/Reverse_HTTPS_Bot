from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import cPickle

def readfile(filename):
	fh = open(filename, 'rb')
	string = fh.read()
	fh.close()
	return string

def writefile(filename, string):
	fh = open(filename, 'wb')
	fh.write(string)
	fh.close()

def write_serial(filename, data):
	fh = open(filename, 'wb')
	cPickle.dump(data, fh, protocol=cPickle.HIGHEST_PROTOCOL)
	fh.close()

def genKeypair(writeit=True):
    random_generator = Random.new().read
    RSAkey = RSA.generate(2048, randfunc=random_generator, progress_func=None, e=65537)
    public_key = RSAkey.publickey()
    if writeit:
      writefile('c_pri.pem', RSAkey.exportKey())
      writefile('c_pub.pem', public_key.exportKey())

def getKey(filename='privkey.pem'):
    RSAkey = readfile(filename)
    RSAkey = RSA.importKey(RSAkey)
    return RSAkey

def encdata(data, RSAkey):
    return RSAkey.encrypt(data, '')

def decdata(data, RSAkey):
    return RSAkey.decrypt(data)
