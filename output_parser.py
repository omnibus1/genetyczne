input="((-1.340958826283627 + ((X1  * X1 ) + (0.5289602584779773 + ((((((-3.228495735210709 - 3.3019124060777703) - -2.311138209804837) - 2.7857240607925773) + (X1  + (X1  + X1 ))) * X2 ) + (0.5289602584779773 - (((((2.3892466623141173 + -4.556853667365347) * 1.5511076624696916) - -2.311138209804837) / 1.5112937882607094) - (X2  / ((((-3.939298115034826 / 0.8902600404270107) - ((4.191154536327122 / X1 ) + ((-0.5443337557520911 + (((-3.0567591719857523 + 2.7857240607925773) + 4.367510539623293) - (((((((-4.760790126892566 - 2.3181824933950645) - (3.5072825141183763 + 3.7721559422840123)) / (-0.5292114886728614 * -4.742858752770895)) * ((-3.0567591719857523 + 3.7721559422840123) * 4.281580118601839)) / ((((2.3051086156531007 - -3.939298115034826) / -3.000332035778792) + 3.7721559422840123) + ((-3.939298115034826 / ((((((-4.556853667365347 * X2 ) * -1.3756890864667182) - 3.4159330813949325) + (-4.8067653939175 + 2.4286822772235404)) - (-4.550630451811068 * -2.572140679149848)) - (-2.1202803899660227 * (((X2  - -4.445428081608837) * (-1.451654074012728 + -1.3756890864667182)) + (-1.025191826938646 + (X1  - (-0.5292114886728614 * -2.311138209804837))))))) + (-3.228495735210709 * -2.1976240915217526)))) + -4.29746806400353) - 3.7098675359576525))) * ((((((3.083896867116117 - -3.6745675424404345) + -4.556853667365347) - ((0.5692688263865175 + (1.3527952345671626 * 4.555914594994055)) + -4.8067653939175)) * (-3.228495735210709 - -2.278438637725947)) + 4.191154536327122) + 3.7721559422840123)))) * -4.112033373801694) - X1 )))))))) - ((0.10663555102564448 + ((2.4286822772235404 + 3.7721559422840123) * -1.2054422112496344)) / ((-3.0567591719857523 + -4.760790126892566) + X2 )))"



input=input.replace(" ","")
input=input.replace(".",",")
input=input.replace("X1", "W309")
input=input.replace("X2", "X309")

print(input)
print(len(input))