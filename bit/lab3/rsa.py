from itertools import islice

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


plaintext = b"""You don’t even need to be in the same room or the same country. Studies show that reading bad news 
or seeing videos of something scary raises your pulse, makes you sweat, and dilates your pupils. Our preprogrammed 
physiological reactions to danger can be triggered by a tweet. That’s why the Oxford Circus panic was so bad: It 
was amplified by social media.
Fear can be transmitted digitally as easily as it can physically—and that’s a problem because digital technologies 
reach everyone. It’s not a few thousand people in a crowd anymore. Three-quarters of adults on earth now have a smartphone, 
which means we’re getting 24-hour access to all the worst stories happening everywhere to 7.6 billion people—all the time.
The speed and tenor of cultural conversation is now mind-bogglingly fast. The moment something bad happens somewhere 
on the planet, fear ripples through the ether. One person armed with a bad story can infect millions of others in a 
few minutes. That’s why, right now, the English-speaking world is in the middle of a fear pandemic.
Every day terrifying stories sweep through the global village, in articles, tweets, and evening broadcasts, and they 
are amplified a million times over until there’s nowhere to hide. Algorithmic bias, mental illness, foreign infidels, 
chronic pain, hooded extremists, robots coming to take our jobs, burning forests, warlike naval maneuvers, marching 
racists, rising waters, surveillance regimes, trade wars, toxic chemicals, predatory capitalism, roaming gangs of 
criminal youths, drug overdoses, benefit-devouring migrant caravans massing at the border… the list goes on and on. 
The fear virus takes hundreds of forms and mutates and spreads every time we click or watch or mutter darkly about 
the future at family dinner.
"""
key = RSA.generate(bits=1024)
cipher = PKCS1_OAEP.new(key)


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


ciphertext = b''
for piece in chunk(plaintext, 40):
    ciphertext += cipher.encrypt(bytes(piece))

print(ciphertext.hex().upper())

decrypted = b''
for piece in chunk(ciphertext, 128):
    decrypted += cipher.decrypt(bytes(piece))
print(decrypted)