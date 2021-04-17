# Author: Cory O'Donoghue
# Graph Theory Project
# Reference Dr.Ian McLoughlin https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54

import thompsonConstruction
import shuntingre

if __name__ == "__main__":
    tests = [  ["(a.b|b*)",   ["ab", "b", "bb", "a"]]
             , ["a.(b.b)*.a", ["aa", "abba", "aba"]]
             , ["1.(0.0)*.1", ["11", "100001", "11001"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompsonConstruction.re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()




