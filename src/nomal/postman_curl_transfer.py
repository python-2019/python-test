if __name__ == '__main__':
    pm="""
    curl --location --request POST 'http://172.20.66.166:8090/vehicle-status/internal/condition/getConditionByPagingV2?signt=1619342567204&sign=cab7dba3e0c8adc0740930f3ba8cbc0c&appkey=5732477868' \
--header 'Content-Type: application/json' \
--data-raw '{
    "enableEcu": true,
    "endTime": "1651505147030",
    "fixedInterval": 5,
    "startTime": "1621505147000",
    "vin": "LXWGMPBB000000001",
    "pageIndex": "1",
    "pageSize": "1000"
}'
"""
    print(pm.replace("--location --request POST","-X POST").replace("--data-raw","-d"))