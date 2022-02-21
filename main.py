from encoder import generate_key,fast_power,encoding,primality_test,toCode
from decoder import decoding,solve


def main():
    generate_key()
    rule=open("rule.txt","r")
    m=rule.readline()
    k=rule.readline()
    code=encoding()
