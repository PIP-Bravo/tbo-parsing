number_of_rules = int(input())
grammar = list()


def check_grammar(grammar):
    for prod_rules in grammar:
        if len(prod_rules[0]) != 1 or not (prod_rules[0].isupper()):
            return False
        if len(prod_rules[1]) > 2 or len(prod_rules[1]) == 0:
            return False
        if len(prod_rules[1]) == 1 and not (prod_rules[1][0].islower()):
            return False
        if len(prod_rules[1]) == 2:
            if not (prod_rules[1][0].isupper()) or not (prod_rules[1][1].isupper()):
                return False
    return True


def cyk_funct(string, temp={}, grammar=grammar):
    if string in temp:
        return temp
    else:
        if len(string) == 1:
            temp[string] = ""
            for prod_rules in grammar:
                if prod_rules[1] == string:
                    temp[string] += (prod_rules[0])
            temp[string] = str(sorted(temp[string])).replace("'", "").replace(" ", "")
            return temp
        else:
            temp[string] = ""
            for i in range(1, len(string)):
                Splitted1 = string[:i]
                Splitted2 = string[i:]
                temp1 = cyk_funct(Splitted1, temp)[Splitted1]
                temp2 = cyk_funct(Splitted2, temp)[Splitted2]
                if temp1 != "" and temp2 != "":
                    for Var1 in temp1:
                        for Var2 in temp2:
                            for prod_rules in grammar:
                                if Var1+Var2 in prod_rules[1] and prod_rules[0] not in temp[string]:
                                    temp[string] += (prod_rules[0])
            temp[string] = str(sorted(temp[string])).replace("'", "").replace(" ", "")
            return temp


def print_cyk(string, grammar):
    result = cyk_funct(string, {}, grammar)
    if "S" in result[string]:
        print("\n"+ string + " is a member of language from the grammar!" + "\n")
        for i in range(1, len(string)+1):
            for j in range(len(string) - i):
                if string[j:j+i] in result:
                    print(string[j:j+i]+" : " + result[string[j:j+i]]+" , ", end="")
                else:
                    print(string[j:j+i]+" : "+"[]"+" , ", end="")
            print(string[-i:], " : "+result[string[-i:]])
    else:
        print("\nUnfortunately, "+ string + " is not a member of language from the grammar!")


for i in range(number_of_rules):
    prod_rules = input().split(" -> ")
    grammar.append(prod_rules)

string = input()
if check_grammar(grammar):
    print_cyk(string, grammar)
else:
    print("Wrong Grammar")