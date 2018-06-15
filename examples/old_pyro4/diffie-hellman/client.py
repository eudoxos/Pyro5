from Pyro5.compatibility import Pyro4
import Pyro4
import Pyro4.errors
from diffiehellman import DiffieHellman


dh = DiffieHellman(group=14)

with Pyro4.Proxy("PYRONAME:example.dh.keyexchange") as keyex:
    print("exchange public keys...")
    other_key = keyex.exchange_key(dh.public_key)
    print("got server public key, creating shared secret key...")
    dh.make_shared_secret_and_key(other_key)
    print("shared secret key = ", dh.key)
    print("(check the server output to see the same shared private key)")
