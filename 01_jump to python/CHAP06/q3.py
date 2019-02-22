from moss_dict import moss_dict

sentence =input("모스부호를 입력하세요 : ").split(" ")
length = (len(sentence))
result = []
key_list = moss_dict.keys()

for i in range(0, length):
    for j in key_list:
        if sentence[i] == "":
            result.append(" ")
            break
        elif sentence[i] == j:
            result.append(moss_dict[j])
            break
        else: pass

print("".join(result))

# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--