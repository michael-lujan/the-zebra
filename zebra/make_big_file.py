import uuid
num_of_records = 90000
num_of_columns = 10

record = ','.join([str(uuid.uuid1()) for i in range(num_of_columns)])
print(len(record))
with open('big_file.csv', 'w') as f:
    f.write('Provider Name,CampaignID,Phone Number,Redirect Link,Zipcode,Address,Cost Per Ad Click,TestColumn')
    for i in range(num_of_records):
        record = ','.join(['Hello', str(i), '512-555-5555', 'example.com/whoops', '12345-6789', 'Some street', '1.23', 'test' ])
        f.write(''.join([record, '\n']))
    