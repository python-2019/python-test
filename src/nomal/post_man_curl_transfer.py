if __name__ == '__main__':
    pm="""curl --location --request POST 'localhost:8081/gtmc-lifecycle/dataRelegation/hotToGlacier' \
--header 'Content-Type: application/json' \
--data-raw '{
    "subId": 1
}'"""
    print(pm.replace("--location --request POST","-X POST").replace("--data-raw","-d"))