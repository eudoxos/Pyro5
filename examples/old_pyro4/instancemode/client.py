from Pyro5.compatibility import Pyro4
import Pyro4
import time

print("Showing the different instancing modes.")
print("The number printed, is the id of the instance that handled the call.")

print("\n-----PERCALL (different number possible every time) -----")
with Pyro4.Proxy("PYRONAME:instance.percall") as p:
    print(p.msg("hello1"))
    print(p.msg("hello1"))
    print(p.msg("hello1"))
with Pyro4.Proxy("PYRONAME:instance.percall") as p:
    print(p.msg("hello2"))
    print(p.msg("hello2"))
    print(p.msg("hello2"))
with Pyro4.Proxy("PYRONAME:instance.percall") as p:
    print(p.msg("hello3"))
    print(p.msg("hello3"))
    print(p.msg("hello3"))

print("\n-----SESSION (same numbers within session) -----")
with Pyro4.Proxy("PYRONAME:instance.session") as p:
    print(p.msg("hello1"))
    print(p.msg("hello1"))
    print(p.msg("hello1"))
print(" ..new proxy..")
with Pyro4.Proxy("PYRONAME:instance.session") as p:
    print(p.msg("hello2"))
    print(p.msg("hello2"))
    print(p.msg("hello2"))

print("\n-----SINGLE (same number always, even over proxies) -----")
with Pyro4.Proxy("PYRONAME:instance.single") as p:
    print(p.msg("hello1"))
    print(p.msg("hello1"))
    print(p.msg("hello1"))
with Pyro4.Proxy("PYRONAME:instance.single") as p:
    print(p.msg("hello2"))
    print(p.msg("hello2"))
    print(p.msg("hello2"))
with Pyro4.Proxy("PYRONAME:instance.single") as p:
    print(p.msg("hello3"))
    print(p.msg("hello3"))
    print(p.msg("hello3"))

