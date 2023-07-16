```shell
curl --location '{address}/people/{email}'
```

```shell
curl --location --request PUT '{address}/people/{email}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "{name}",
    "city": "{city}"
}'
```