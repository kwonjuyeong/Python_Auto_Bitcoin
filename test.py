import pyupbit

access = "Nia4PY7Y6rigKBV9xE0fHFKfumPmTsXuqDHYPT2M"          # 본인 값으로 변경
secret = "660awV9GFlJBQPFUY4hj9wdxgaNwVVUxNxNdx9qx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XTZ"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW-BTC"))
print(upbit.get_balance("KRW-CVC"))
print(upbit.get_balance("KRW-SAND"))
print(upbit.get_balance("KRW"))         # 보유 현금 조회