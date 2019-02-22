import json
g_json_big_data=[]
with open("sample.json",encoding='UTF8') as json_file:
    json_object = json.load(json_file) #load
    json_string = json.dumps(json_object)#dumps
    g_json_big_data = json.loads(json_string)#load
print(json_object)
print(json_string)
print(g_json_big_data[0])
print(g_json_big_data[0]['레벨 2-1 키']) #json에서 값을 가져오는 방법
g_json_big_data.append({'레벨 2-4 키':'수박'})#데이터 쓰기
g_json_big_data[0]['레벨 2-1 키'] = "체리" #데이터 업데이트
del g_json_big_data[2]

print(g_json_big_data[1]['레벨 2-3 키']['레벨 3-1키'][0]['레벨 4-1 키'])#자식 레벨의 딕셔너리 값 접근
g_json_big_data[1]['레벨 2-3 키']['레벨 3-1키'][0]['레벨 4-1 키']=24 #값 변경

with open('sample.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
pass
