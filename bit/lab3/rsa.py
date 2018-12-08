from itertools import islice

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


plaintext = b"""Known throughout the world, the works of William Shakespeare have been performed in countless hamlets,
 villages, cities and metropolises for more than 400 years.
 And yet, the personal history of William Shakespeare is somewhat a mystery.
 There are two primary sources that provide historians with a basic outline of his life.
 One source is his work - the plays, poems and sonnets - and the other is official documentation
 such as church and court records. However, these only provide brief sketches of specific events in his life and
 provide little on the person who experienced those events.
While it`s difficult to determine the exact chronology of William Shakespeare`s plays,
over the course of two decades, from about 1590 to 1613, he wrote a total of 37 plays revolving around
several main themes: histories, tragedies, comedies and tragicomedies.
With the exception of the tragic love story Romeo and Juliet, William Shakespeare's
first plays were mostly histories. Henry VI (Parts I, II and III), Richard II and Henry V
dramatize the destructive results of weak or corrupt rulers, and have been interpreted
by drama historians as Shakespeare's way of justifying the origins of the Tudor Dynasty.
 Julius Caesar portrays upheaval in Roman politics that may have resonated with viewers at
 a time when England`s aging monarch, Queen Elizabeth I, had no legitimate heir, thus creating
 the potential for future power struggles.
Shakespeare also wrote several comedies during his early period:
 the witty romance A Midsummer Night's Dream, the romantic Merchant of Venice,
  the wit and wordplay of Much Ado About Nothing, the charming As You Like It and Twelfth Night.
Other plays written before 1600 include Titus Andronicus, The Comedy of Errors, The Two Gentlemen of Verona,
 The Taming of the Shrew, Love`s Labour`s Lost, King John, The Merry Wives of Windsor and Henry V.
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