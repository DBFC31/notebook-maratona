#include <bits/stdc++.h>
using namespace std;

// Precisao 2 casas decimais de float para impressao
cout << fixed << setprecision(2);

// Criar pair
make_pair(1, 2);

// Criar tupla
make_tuple(1, 2, 3);

// Pegar elemento i da tupla
get<i>(t);

// infinito
#define INF 0x3F3F3F3F

// Operacoes BitWise 
#define BitTest(var, bit) var & (1 << bit)
#define BitSet(var, bit) var |= (1 << bit)
#define BitClear(var, bit) var &= ~(1 << bit)
#define BitFlip(var,bit) var ^= (1<<bit)

// Maximo divisor comum (GCD) O(log10(min(a, b))
std::gcd(a, b);
