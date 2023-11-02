from urllib import request, parse
import json

def thinkspeak_get(api_key_read, channel_ID, fields):
    data = {}  # Tạo một từ điển để lưu trữ dữ liệu của các field
    
    for field_num in fields:
        # Tạo URL yêu cầu để lấy dữ liệu cuối cùng từ mỗi field
        url = "https://api.thingspeak.com/channels/{}/fields/{}/last.json?api_key={}".format(channel_ID, field_num, api_key_read)
        
        # Gửi yêu cầu GET và nhận phản hồi từ Thingspeak
        response = request.urlopen(url)
        response_data = response.read().decode()
        
        # Giải mã dữ liệu JSON và lưu trữ vào từ điển
        field_name = "field{}".format(field_num)
        data[field_name] = json.loads(response_data)[field_name]
    
    return data

# Thay đổi channel_ID, api_key_read và danh sách fields cần đọc
channel_ID = "2295353"
api_key_read = "KKB6HW3VK8PNIRRQ"
fields_to_read = [1, 2, 3, 4, 5, 6, 7]  # Thay đổi danh sách fields cần đọc

data = thinkspeak_get(api_key_read, channel_ID, fields_to_read)

for field_num in fields_to_read:
    field_name = "field{}".format(field_num)


    if(field_name=="field1" and int(data.get(field_name))==1):
        print("sw1 on")
    elif(field_name=="field1" and int(data.get(field_name))==0):
        print("sw1 off")

    if(field_name=="field2" and int(data.get(field_name))==1):
        print("sw2 on")
    elif(field_name=="field2" and int(data.get(field_name))==0):
        print("sw2 off")

    if(field_name=="field3" and int(data.get(field_name))==1):
        print("sw3 on")
    elif(field_name=="field3" and int(data.get(field_name))==0):
        print("sw3 off")

    if(field_name=="field4" and int(data.get(field_name))==1):
        print("Lamp_Status on")
    elif(field_name=="field4" and int(data.get(field_name))==0):
        print("Lamp_Status off")

    if(field_name=="field5" and int(data.get(field_name))==1):
        print("Warning_lights_Status on")
    elif(field_name=="field5" and int(data.get(field_name))==0):
        print("Warning_lights_Status off")

    if(field_name=="field6"):
        print("Temperature: ",int(data.get(field_name)))

    if(field_name=="field7"):
        print("Humidity: ",int(data.get(field_name)))
    