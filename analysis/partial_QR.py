from tools.binary import Binary
from salsa.QR_function import QR


a = Binary()
b = Binary()
c = Binary()
d = Binary()

a.gen_random(32)
b.gen_random(32)
c.gen_random(32)
d.gen_random(32)

X = (a, b, c, d)

Ys = []

for i in range(100):
    # Generate a new part. c for interesting findings.
    c.gen_random(32)
    X = (a, b, c, d)
    Y = QR(X)
    Ys.append(Y)


partials = []
for i in range(len(Ys)):
    a, b, c, d = Ys[i]
    # Add relevant partial. b for interesting findings.
    partials.append(b)


print('Expected unique values:\t', len(partials))
print('Found unique values:\t', len(set(partials)))
