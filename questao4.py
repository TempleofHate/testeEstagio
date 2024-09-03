def next_in_sequence_a(seq):
    return seq[-1] + 2

def next_in_sequence_b(seq):
    return seq[-1] * 2

def next_in_sequence_c(seq):
    n = len(seq)
    return n ** 2

def next_in_sequence_d(seq):
    n = (len(seq) + 1 ) * 2
    return n ** 2

def next_in_sequence_e(seq):
    return seq[-1] + seq[-2]

def next_in_sequence_f(seq):
    if seq[-1] % 2 == 0:
        return seq[-1] + 1
    else:
        return seq[-1] + 1

seq_a = [1, 3, 5, 7]
seq_b = [2, 4, 8, 16, 32, 64]
seq_c = [0, 1, 4, 9, 16, 25, 36]
seq_d = [4, 16, 36, 64]
seq_e = [1, 1, 2, 3, 5, 8]
seq_f = [2, 10, 12, 16, 17, 18, 19]

print("Próximo elemento de a):", next_in_sequence_a(seq_a))
print("Próximo elemento de b):", next_in_sequence_b(seq_b))
print("Próximo elemento de c):", next_in_sequence_c(seq_c))
print("Próximo elemento de d):", next_in_sequence_d(seq_d))
print("Próximo elemento de e):", next_in_sequence_e(seq_e))
print("Próximo elemento de f):", next_in_sequence_f(seq_f))
