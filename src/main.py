import sys
import CommLangParser as parser


print("Welcome to CommLang")
print("(pre-alpha) ver. 1.0.0")
print("")

while True:
    try:
        s = input('CommLang >>')
    except EOFError:
        break
    print("")
    parser.do_parse(s)
    print("")
