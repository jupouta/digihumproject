
# importing the word "pakolainen"

import requests

response_p = requests.get("https://korp.csc.fi/cgi-bin/korp.cgi?command=query&cqp=%5Blemma+%3D+%22pakolainen%22%5D&corpus=KLK_FI_1970,KLK_FI_1971,KLK_FI_1972,KLK_FI_1973,KLK_FI_1974,KLK_FI_1975,KLK_FI_1976,KLK_FI_1977,KLK_FI_1978,KLK_FI_1979,KLK_FI_1980,KLK_FI_1981,KLK_FI_1982,KLK_FI_1983,KLK_FI_1984,KLK_FI_1985,KLK_FI_1986,KLK_FI_1987,KLK_FI_1988,KLK_FI_1989,KLK_FI_1990,KLK_FI_1991,KLK_FI_1992,KLK_FI_1993,KLK_FI_1994,KLK_FI_1995,KLK_FI_1996,KLK_FI_1997,KLK_FI_1998,KLK_FI_1999,KLK_FI_2000,KLK_FI_2011&start=0&end=15000")
json_data_p = response_p.json()
kwic_p = json_data_p["kwic"]

saneet_p = []

# imports only the tokens
for tietue in kwic_p:
    for alkio in tietue["tokens"]:
        for sane in alkio:
            saneet_p.append(alkio[sane])

# saves the tokens in a file
with open("saneet_pakolainen.txt", "w") as out_file_p:
    for s in range(len(saneet_p)):
        out_string = ""
        out_string += str(saneet_p[s]) + " "
        out_file_p.write(out_string)

out_file_p.close()


# importing the word "maahanmuuttaja"

import requests

response_m = requests.get("https://korp.csc.fi/cgi-bin/korp.cgi?command=query&cqp=%5Blemma+%3D+%22maahanmuuttaja%22%5D&corpus=KLK_FI_1970,KLK_FI_1971,KLK_FI_1972,KLK_FI_1973,KLK_FI_1974,KLK_FI_1975,KLK_FI_1976,KLK_FI_1977,KLK_FI_1978,KLK_FI_1979,KLK_FI_1980,KLK_FI_1981,KLK_FI_1982,KLK_FI_1983,KLK_FI_1984,KLK_FI_1985,KLK_FI_1986,KLK_FI_1987,KLK_FI_1988,KLK_FI_1989,KLK_FI_1990,KLK_FI_1991,KLK_FI_1992,KLK_FI_1993,KLK_FI_1994,KLK_FI_1995,KLK_FI_1996,KLK_FI_1997,KLK_FI_1998,KLK_FI_1999,KLK_FI_2000,KLK_FI_2011&start=0&end=15000")
json_data_m = response_m.json()
kwic_m = json_data_m["kwic"]

saneet_m = []

# imports only the tokens
for tietue in kwic_m:
    for alkio in tietue["tokens"]:
        for sane in alkio:
            saneet_m.append(alkio[sane])

# saves the tokens in a file
with open("saneet_maahanmuuttaja.txt", "w") as out_file_m:
    for s in range(len(saneet_m)):
        out_string = ""
        out_string += str(saneet_m[s]) + " "
        out_file_m.write(out_string)

out_file_m.close()

